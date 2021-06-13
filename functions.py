import pyautogui
from speech_recognition import Microphone
import libraries as lib
import lists as li
from libraries import jit

color2 = 'black'
color = "red4"


@jit(nopython=True)
def close_all():
    speak('Closing')
    lib.pyautogui.hotkey('alt', 'f4')


def speak(command: str):
    engine = lib.pyttsx3.init()
    engine.say(command.capitalize())
    print('Cyber:' + command)
    engine.runAndWait()


def speak_int(command):
    engine = lib.pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()


def wishme():
    hour = int(lib.datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


def listen():
    while True:
        newstatement: str = main_listen()
        check_statement = bool(newstatement)
        if not check_statement:
            pass
        else:
            return newstatement
            break


def main_listen():
    r = lib.sr.Recognizer()
    source: lib.sr.Microphone
    with lib.sr.Microphone() as source:
        print("Listening...........")
        try:
            audio = r.listen(source)
            text: str = r.recognize_google(audio)
            print('User:' + text)
            return text
        except Exception:
            pass



def main_listen_sleep():
    r = lib.sr.Recognizer()
    source: lib.sr.Microphone
    with lib.sr.Microphone() as source:
        print("Listening...........")
        try:
            audio = r.listen(source)
            text: str = r.recognize_google(audio)
            print('User:' + text)
            return text
        except Exception:
            pass


def listen_sleep():
    while True:
        newstatement: str = main_listen_sleep()
        check_statement = bool(newstatement)
        if not check_statement:
            pass
        else:
            return newstatement
            break


def listen_mail():
    while True:
        newstatement: str = listen_type()
        check_statement = bool(newstatement)
        if not check_statement:
            pass
        else:
            return newstatement
            break


def listen_type():
    r = lib.sr.Recognizer()
    source: lib.sr.Microphone
    with lib.sr.Microphone() as source:
        print("Listening...........")
        try:
            audio = r.listen(source)
            text: str = r.recognize_google(audio)
            print('User:' + text)
            return text
        except Exception:
            pass


def get():
    win = lib.GetWindowText(lib.GetForegroundWindow()).lower()
    if 'chrome' in win:
        pass
    elif 'brave' in win:
        pass
    else:
        speak('sorry please open chrome and try again later')
        exit()


def get1():
    win = lib.GetWindowText(lib.GetForegroundWindow()).lower()
    return win


def open_app(name):
    speak('opening' + name)
    lib.pyautogui.press('win')
    lib.sleep(0.3)
    lib.pyautogui.typewrite(name)
    lib.sleep(1)
    lib.pyautogui.press('enter')
    lib.sleep(2.5)
    wind = lib.GetWindowText(lib.GetForegroundWindow()).lower()
    if 'search' in wind:
        lib.pyautogui.press('win', presses=2, interval=0.25)
        speak('Sorry,cannot find this app on your pc')

    else:
        pass


def open_website(website, name):
    speak('opening ' + name)
    lib.webbrowser.open(website)


def close_tab():
    speak('Closing')
    lib.pyautogui.hotkey('ctrl', 'w')


def close():
    speak('Closing')
    lib.pyautogui.hotkey('alt', 'f4')


def search(query):
    try:
        speak('searching')
        sum = (lib.wikipedia.summary(query, sentences=1))
        speak(sum)
    except Exception:
        lib.webbrowser.open(li.links[0] + query)
        speak('showing results on google')


def tab():
    lib.pyautogui.press('tab')


def search_google(query):
    speak('searching on google')
    lib.webbrowser.open(li.links[0] + query)


def typewrite(content):
    content.capitalize()
    lib.pyautogui.typewrite(content)


def search_youtube(query):
    speak('searching on youtube')
    lib.webbrowser.open(li.links[1] + query)





def whatkit():
    print('hello world ,')
    pyautogui.hotkey()


def mail():
    try:
        speak('sending mail')
        lib.webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=new')
        lib.sleep(5)
        while True:
            got: str = get1()
            got = got.lower()
            if 'inbox' in got:
                lib.sleep(8)
                break
            else:
                pass
        speak("Whom do you want to send the mail")
        newstatement = listen_mail()
        typewrite(newstatement)
        lib.sleep(2)
        tab()
        speak('what is the subject? ')
        tab()
        subject = listen_mail()
        typewrite(subject)
        speak('what is the content? to end please speak i am done.')
        tab()
        while True:
            content = listen_mail()
            if 'I am done' in content:
                content1 = content.replace('I am done', '')
                typewrite(content1)
                typewrite('.')
                lib.pyautogui.press('space')
                speak('Do you want to attach a file?')
                attachment = listen_mail()
                if attachment in li.affirmative:
                    speak('please select the file you want to attach')
                    tab()
                    tab()
                    tab()
                    lib.pyautogui.press('enter')
                    speak('please select your file')
                    lib.sleep(3)
                    while True:
                        wind = lib.GetWindowText(lib.GetForegroundWindow()).lower()
                        if 'open' in wind:
                            pass
                        else:
                            break
                    speak('do you want to send this mail?')
                    send = listen_mail()
                    if send in li.affirmative:
                        speak('ok, sending the mail')
                        lib.pyautogui.hotkey('ctrl', 'enter')
                        speak('done')
                        break
                    else:
                        speak('i cannot understand please try again later.')
                else:
                    speak('Ok, then should i send the mail?')
                    send_final = listen_mail()
                    if send_final in li.affirmative:
                        speak('Ok, sending')
                        lib.pyautogui.hotkey('ctrl', 'enter')
                        break
                    else:
                        speak('ok stopping the procedure')
            else:
                typewrite(content + '. ')
                pass
        else:
            pass

    except Exception:
        pass


def reply():
    num = lib.random.randint(0, 3)
    speak(li.replies[num])


def type_mode():
    speak('okay to stop type mode speak disconnect,starting type mode in 3  2  1 ')
    while True:
        try:
            tye = listen_type()
            if 'disconnect' in tye:
                tye1 = tye.replace('disconnect', '')
                typewrite(tye1 + '. ')
                speak('okay,Stopping type mode')
                break
            else:
                typewrite(tye + '. ')

                pass

        except Exception:
            pass


def songs_random():
    number = lib.random.randint(0, 4)
    speak('Let me show you!')
    lib.webbrowser.open_new(li.songs[number])


def entry(row: object, column: object) -> object:
    enter_class = lib.Entry(borderwidth=15, width=35, bg="white")
    enter_class.grid(row=row, column=column)
    return object


def label(text: object, row: object, column: object) -> object:
    lab = lib.Label(text=text, bg=color, fg=color2, height=1, width=10, font='sid')
    lab.grid(row=row, column=column)
    return object


def current_window():
    current_speak: str = get1()
    current_speak.capitalize()
    speak('The current window is ' + current_speak)


def zoom():
    open_app(' zoom')
    tab()
    tab()
    tab()
    tab()
    lib.pyautogui.press('space')


def meaning(word):
    engine = lib.pyttsx3.init()
    dictionary = lib.PyDictionary()
    print(dictionary.meaning(word))
    engine.getProperty('rate')
    engine.setProperty('rate', 135)
    engine.say(dictionary.meaning(word))
    engine.runAndWait()


def synonym(word):
    engine = lib.pyttsx3.init()
    dictionary = lib.PyDictionary()
    print(dictionary.synonym(word))
    # engine.getProperty('rate')
    # engine.setProperty('rate', 135)
    engine.say(dictionary.synonym(word))
    engine.runAndWait()


def antonym(word):
    engine = lib.pyttsx3.init()
    dictionary = lib.PyDictionary()
    anto = dictionary.antonym(word)
    print(anto)
    # engine.getProperty('rate')
    # engine.setProperty('rate', 135)
    engine.say(anto)
    engine.runAndWait()


def hotkey(btn1, btn2):
    lib.pyautogui.hotkey(btn1, btn2)


def show():
    hotkey('win', 'tab')
    lib.sleep(3)
    hotkey('win', 'tab')


def play():
    tab()
    lib.pyautogui.press('enter')
    lib.sleep(3)
    lib.pyautogui.press('t')


def switch():
    lib.pyautogui.hotkey('alt', 'tab', presses=2)


def switch_tab():
    lib.pyautogui.hotkey('ctrl', 'tab')


# def to_do_items():
#     root = lib.Tk()
#     for i in range(5):
#         getdata = get_data()
#         tas = getdata[i]
#         fin: str = tas[2]
#         if fin == 'false':
#             Label = label(root, column=1, row=1, text=tas[1])
#             Label.pack()
#         else:
#             pass
#     root.mainloop()


if __name__ == '__main__':
    show()
