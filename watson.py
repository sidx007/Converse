import pyaudio
import wave
from array import array
from struct import pack

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = '5P4CRx9VUK_BOVsE1YrtJgzzL1mZpciTLn0SXSeUauOJ'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/f137357a-62ea-4cbf-8ad0-223d16f99e84'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)


def record(output_file):
    #getting audio
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print('Recording')
    frames = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



class Microphone(AudioSource):
    """
    Creates a new ``Microphone`` instance, which represents a physical microphone on the computer. Subclass of ``AudioSource``.

    This will throw an ``AttributeError`` if you don't have PyAudio 0.2.11 or later installed.

    If ``device_index`` is unspecified or ``None``, the default microphone is used as the audio source. Otherwise, ``device_index`` should be the index of the device to use for audio input.

    A device index is an integer between 0 and ``pyaudio.get_device_count() - 1`` (assume we have used ``import pyaudio`` beforehand) inclusive. It represents an audio device such as a microphone or speaker. See the `PyAudio documentation <http://people.csail.mit.edu/hubert/pyaudio/docs/>`__ for more details.

    The microphone audio is recorded in chunks of ``chunk_size`` samples, at a rate of ``sample_rate`` samples per second (Hertz). If not specified, the value of ``sample_rate`` is determined automatically from the system's microphone settings.

    Higher ``sample_rate`` values result in better audio quality, but also more bandwidth (and therefore, slower recognition). Additionally, some CPUs, such as those in older Raspberry Pi models, can't keep up if this value is too high.

    Higher ``chunk_size`` values help avoid triggering on rapidly changing ambient noise, but also makes detection less sensitive. This value, generally, should be left at its default.
    """
    def __init__(self, device_index=None, sample_rate=None, chunk_size=1024):
        assert device_index is None or isinstance(device_index, int), "Device index must be None or an integer"
        assert sample_rate is None or (isinstance(sample_rate, int) and sample_rate > 0), "Sample rate must be None or a positive integer"
        assert isinstance(chunk_size, int) and chunk_size > 0, "Chunk size must be a positive integer"

        # set up PyAudio
        self.pyaudio_module = self.get_pyaudio()
        audio = self.pyaudio_module.PyAudio()
        try:
            count = audio.get_device_count()  # obtain device count
            if device_index is not None:  # ensure device index is in range
                assert 0 <= device_index < count, "Device index out of range ({} devices available; device index should be between 0 and {} inclusive)".format(count, count - 1)
            if sample_rate is None:  # automatically set the sample rate to the hardware's default sample rate if not specified
                device_info = audio.get_device_info_by_index(device_index) if device_index is not None else audio.get_default_input_device_info()
                assert isinstance(device_info.get("defaultSampleRate"), (float, int)) and device_info["defaultSampleRate"] > 0, "Invalid device info returned from PyAudio: {}".format(device_info)
                sample_rate = int(device_info["defaultSampleRate"])
        except Exception:
            audio.terminate()
            raise

        self.device_index = device_index
        self.format = self.pyaudio_module.paInt16  # 16-bit int sampling
        self.SAMPLE_WIDTH = self.pyaudio_module.get_sample_size(self.format)  # size of each sample
        self.SAMPLE_RATE = sample_rate  # sampling rate in Hertz
        self.CHUNK = chunk_size  # number of frames stored in each buffer

        self.audio = None
        self.stream = None

    @staticmethod
    def get_pyaudio():
        """
        Imports the pyaudio module and checks its version. Throws exceptions if pyaudio can't be found or a wrong version is installed
        """
        try:
            import pyaudio
        except ImportError:
            raise AttributeError("Could not find PyAudio; check installation")
        from distutils.version import LooseVersion
        if LooseVersion(pyaudio.__version__) < LooseVersion("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio

    @staticmethod
    def list_microphone_names():
        """
        Returns a list of the names of all available microphones. For microphones where the name can't be retrieved, the list entry contains ``None`` instead.

        The index of each microphone's name is the same as its device index when creating a ``Microphone`` instance - indices in this list can be used as values of ``device_index``.
        """
        audio = Microphone.get_pyaudio().PyAudio()
        try:
            result = []
            for i in range(audio.get_device_count()):
                device_info = audio.get_device_info_by_index(i)
                result.append(device_info.get("name"))
        finally:
            audio.terminate()
        return result

    def __enter__(self):
        assert self.stream is None, "This audio source is already inside a context manager"
        self.audio = self.pyaudio_module.PyAudio()
        try:
            self.stream = Microphone.MicrophoneStream(
                self.audio.open(
                    input_device_index=self.device_index, channels=1,
                    format=self.format, rate=self.SAMPLE_RATE, frames_per_buffer=self.CHUNK,
                    input=True,  # stream is an input stream
                )
            )
        except Exception:
            self.audio.terminate()
            raise
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.stream.close()
        finally:
            self.stream = None
            self.audio.terminate()

    class MicrophoneStream(object):
        def __init__(self, pyaudio_stream):
            self.pyaudio_stream = pyaudio_stream

        def read(self, size):
            return self.pyaudio_stream.read(size, exception_on_overflow=False)

        def close(self):
            try:
                # sometimes, if the stream isn't stopped, closing the stream throws an exception
                if not self.pyaudio_stream.is_stopped():
                    self.pyaudio_stream.stop_stream()
            finally:
                self.pyaudio_stream.close()
sr = Microphone()


with sr as i:
    res = stt.recognize(audio=i, content_type='audio/mp3', model='en-US-NarrowbandModel', continuous=True).get_result()

# print(res)

