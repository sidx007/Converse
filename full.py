import pyttsx3
import pyautogui
import speech_recognition as sr
from time import sleep
import datetime
import os
import webbrowser
from win32gui import *
import wikipedia
from joke.jokes import geek, icanhazdad, chucknorris, icndb
import random
from random import choice
from PyDictionary import *
import psycopg2
import pywhatkit
from numba import jit

questions = [
    'how are you',
    'what can you do',
    'what is your name',
    'thank you',
    'wassup',
    'who made you',
    'wake up'
]

songs = ['https://www.youtube.com.//watch?v=TI7RQO2cuh0&feature=youtu.be&t=41',
         'https://www.youtube.com.//watch?v=4Ay5OOxRTTE&feature=youtu.be&t=44',
         'https://www.youtube.com.//watch?v=cl0a3i2wFcc&feature=youtu.be&t=72',
         ' https://www.youtube.com.//watch?v=2L6gsn7rGqI&feature=youtu.be&t=209',
         ' https://www.youtube.com.//watch?v=hpVNMjpjiJc&feature=youtu.be&t=166 ']
answers = [
    'I am good',
    "I can do your daily tasks and open application just by recognizing your speech",
    'My name is Converse',
    'Yeah,no problem',
    'I am cool',
    "I was made by Siddharth.",
    "I'm already Up"
]

arguments = [
    'Sorry please speak again',
    'How may i help you?',
]

links = [
    'https://www.google.com/search?q=',
    'https://www.youtube.com/results?search_query=',
    'https://mail.google.com/mail/u/0/#inbox?compose=new',
    'https://www.youtube.com/watch?v=1ExdPa00uz4&list=PL-oM5qTjmK2vxdTsj2Xghu5fjxhtuMaxo'
]

mail_args = [
    'Whom do you want to send the mail?',
    'What is the subject?',
    'What is the content?to end speak i am done',
    'Do you want to attach any file?',
    'Select the file you want to attach',
    'Please select your file',
    'Do you want to send the file',
    'I cannot understand, please try again later'
]
affirmative = [
    'yes',
    'asolutely',
    'yo',
    'yup',
    'of course',
    'exactly',
    'sure'
]

replies = [
    'Yes',
    'Yup',
    'At your service',
    'Yes boss',
]
ms = [
    'microsoft word',
    'microsoft excel',
    'microsoft powerPoint',
    'microsoft oneNote',
    'microsoft outlook',
    'microsoft publisher',
    'microsoft access',
]

def close_all():
    speak('Closing')
    pyautogui.hotkey('alt', 'f4')


def speak(command: str):
    engine = pyttsx3.init()
    engine.say(command.capitalize())
    print('Cyber:' + command)
    engine.runAndWait()


def speak_int(command):
    engine = pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
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
    key1 = 'Go3WlE0LkHrw0rCA4wL0dQ=='
    key2 = 'KUKi7zbqk6snZm8xDociSUP8qwL4jipwIYPrVTZmsvSxiKktsRryd_hdQ1zedVed43f3NARNH1WUZZiRYS3rbA=='
    r = sr.Recognizer()
    source: Microphone
    with sr.Microphone() as source:
        print("Listening...........")
        try:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source, duration=1)
            text: str = r.recognize_houndify(audio, key1, key2)
            print('User:' + text)
            return text
        except Exception:
            pass


def main_listen_sleep():
    key1 = 'Go3WlE0LkHrw0rCA4wL0dQ=='
    key2 = 'KUKi7zbqk6snZm8xDociSUP8qwL4jipwIYPrVTZmsvSxiKktsRryd_hdQ1zedVed43f3NARNH1WUZZiRYS3rbA=='
    r = sr.Recognizer()
    source: Microphone
    with sr.Microphone() as source:
        print("Listening(Sleeping)...........")
        try:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source, duration=1)
            text: str = r.recognize_houndify(audio, key1, key2)
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
    key1 = 'Go3WlE0LkHrw0rCA4wL0dQ=='
    key2 = 'KUKi7zbqk6snZm8xDociSUP8qwL4jipwIYPrVTZmsvSxiKktsRryd_hdQ1zedVed43f3NARNH1WUZZiRYS3rbA=='
    r = sr.Recognizer()
    source: Microphone
    with sr.Microphone() as source:
        print("Listening...........")
        try:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source, duration=1)
            text: str = r.recognize_houndify(audio, key1, key2)
            print('User:' + text)
            return text
        except Exception:
            pass



def get():
    win = GetWindowText(lib.GetForegroundWindow()).lower()
    if 'chrome' in win:
        pass
    elif 'brave' in wind:
        pass
    else:
        speak('sorry please open chrome and try again later')
        exit()


def get1():
    win = GetWindowText(lib.GetForegroundWindow()).lower()
    return win


def open_app(name):
    speak('opening' + name)
    pyautogui.press('win')
    sleep(0.3)
    pyautogui.typewrite(name)
    sleep(1)
    pyautogui.press('enter')
    sleep(2.5)
    wind = GetWindowText(lib.GetForegroundWindow()).lower()
    if 'search' in wind:
        pyautogui.press('win', presses=2, interval=0.25)
        speak('Sorry,cannot find this app on your pc')

    else:
        pass


def open_website(website, name):
    speak('opening ' + name)
    webbrowser.open(website)


def close_tab():
    speak('Closing')
    pyautogui.hotkey('ctrl', 'w')


def close():
    speak('Closing')
    pyautogui.hotkey('alt', 'f4')


def search(query):
    try:
        speak('searching')
        sum = (wikipedia.summary(query, sentences=1))
        speak(sum)
    except Exception:
        webbrowser.open(links[0] + query)
        speak('showing results on google')


def tab():
    pyautogui.press('tab')


def search_google(query):
    speak('searching on google')
    webbrowser.open(links[0] + query)


def typewrite(content):
    content.capitalize()
    pyautogui.typewrite(content)


def search_youtube(query):
    speak('searching on youtube')
    webbrowser.open(links[1] + query)


def jokes():
    speak(choice([geek, icanhazdad, chucknorris, icndb])())


def whatkit():
    print('hello world ,')
    pyautogui.hotkey()


def mail():
    try:
        speak('sending mail')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=new')
        sleep(5)
        while True:
            got: str = get1()
            got = got.lower()
            if 'inbox' in got:
                sleep(8)
                break
            else:
                pass
        speak("Whom do you want to send the mail")
        newstatement = listen_mail()
        typewrite(newstatement)
        sleep(2)
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
                pyautogui.press('space')
                speak('Do you want to attach a file?')
                attachment = listen_mail()
                if attachment in affirmative:
                    speak('please select the file you want to attach')
                    tab()
                    tab()
                    tab()
                    pyautogui.press('enter')
                    speak('please select your file')
                    sleep(3)
                    while True:
                        wind = GetWindowText(GetForegroundWindow()).lower()
                        if 'open' in wind:
                            pass
                        else:
                            break
                    speak('do you want to send this mail?')
                    send = listen_mail()
                    if send in affirmative:
                        speak('ok, sending the mail')
                        pyautogui.hotkey('ctrl', 'enter')
                        speak('done')
                        break
                    else:
                        speak('i cannot understand please try again later.')
                else:
                    speak('Ok, then should i send the mail?')
                    send_final = listen_mail()
                    if send_final in affirmative:
                        speak('Ok, sending')
                        pyautogui.hotkey('ctrl', 'enter')
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
    num = random.randint(0, 3)
    speak(replies[num])


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
    number = random.randint(0, 4)
    speak('Let me show you!')
    webbrowser.open_new(songs[number])


def entry(row: object, column: object) -> object:
    enter_class = Entry(borderwidth=15, width=35, bg="white")
    enter_class.grid(row=row, column=column)
    return object


def label(text: object, row: object, column: object) -> object:
    lab = Label(text=text, bg=color, fg=color2, height=1, width=10, font='sid')
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
    pyautogui.press('space')


def meaning(word):
    engine = pyttsx3.init()
    dictionary = PyDictionary()
    print(dictionary.meaning(word))
    engine.getProperty('rate')
    engine.setProperty('rate', 135)
    engine.say(dictionary.meaning(word))
    engine.runAndWait()


def synonym(word):
    engine = pyttsx3.init()
    dictionary = PyDictionary()
    print(dictionary.synonym(word))
    # engine.getProperty('rate')
    # engine.setProperty('rate', 135)
    engine.say(dictionary.synonym(word))
    engine.runAndWait()


def antonym(word):
    engine = pyttsx3.init()
    dictionary = PyDictionary()
    anto = dictionary.antonym(word)
    print(anto)
    # engine.getProperty('rate')
    # engine.setProperty('rate', 135)
    engine.say(anto)
    engine.runAndWait()


def hotkey(btn1, btn2):
    pyautogui.hotkey(btn1, btn2)


def show():
    hotkey('win', 'tab')
    sleep(3)
    hotkey('win', 'tab')


def play():
    tab()
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('t')


def switch():
    pyautogui.hotkey('alt', 'tab', presses=2)


def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')



if __name__ == '__main__':
    wishme()
    speak(arguments[1])
    while True:
        try:
            wake_up = listen_sleep()
            if 'wake up' in wake_up:
                reply()
                while True:
                    Listen = listen()
                    check = Listen in questions
                    if 'open' in Listen:
                        app = Listen.replace('open', '')
                        if 'youtube' in app:
                            open_website('www.youtube.com', 'youtube')
                        elif 'instagram' in app:
                            open_website('www.instagram.com', 'instagram')
                        elif 'twitter' in app:
                            open_website('www.twitter.com', 'twitter')
                        elif 'facebook' in app:
                            open_website('www.facebook.com', 'facebook')
                        elif 'whatsapp' in app:
                            speak('opening WhatsApp')
                            webbrowser.open_new('https://web.whatsapp.com/')
                        elif 'amazon' in app:
                            open_website('www.amazon.com', 'amazon')
                        else:
                            if 'website' in Listen:
                                open_web = Listen.replace('open', '')
                                open_web = open_web.replace('website', '')
                                search_google(open_web)
                            else:
                                open_app(app)
                    elif 'results ' in Listen:
                        q = Listen.replace("show", '')
                        q1 = q.replace("search", '')
                        q2 = q1.replace("results for", '')
                        speak('Showing results for' + q2)
                    elif 'search' in Listen:
                        query = Listen.replace('search', '')
                        if 'google' in query:
                            new_query1 = query.replace('on google', '')
                            search_google(new_query1)
                        elif 'youtube' in query:
                            new_query = Listen.replace('search', '')
                            new_query1 = new_query.replace('on youtube', '')
                            search_youtube(new_query1)
                            sleep(3)
                            play_listen = listen_mail()
                            if 'play' in play_listen:
                                play_check = get1()
                                if 'youtube' in play_check:
                                    speak('Playing!!')
                                    play()
                                    break
                                else:
                                    pass
                            else:
                                Listen = play_listen
                                pass
                        else:
                            search(query)
                        pass
                    elif 'meaning' in Listen:
                        print(Listen)
                        if 'meaning of' in Listen:
                            word = Listen.replace('meaning of', '')
                            meaning(word)
                        else:
                            pass
                    elif 'close all' in Listen:
                        close_all()
                        sleep(4)
                        wind1 = lib.GetWindowText(lib.GetForegroundWindow()).lower()
                        check = wind1 in li.ms
                        if check:
                            speak('Do you want to save this?')
                            save = listen()
                            checkin = save in li.affirmative
                            if checkin:
                                speak('Saving')
                                lib.pyautogui.press('enter')
                                speak('What should be the name?')
                                name = listen()
                                typewrite(name)
                                pyautogui.press('enter')
                            else:
                                speak('closing')
                                tab()
                                pyautogui.press('enter')
                        else:
                            pass
                    elif 'synonym' in Listen:
                        if 'synonym' in Listen:
                            synonym1 = Listen.replace('synonym of', '')
                            synonym(synonym1)
                        else:
                            pass
                    elif 'antonym' in Listen:
                        if 'antonym' in Listen:
                            antonym1 = Listen.replace('antonym of', '')
                            antonym(antonym1)
                        else:
                            pass
                    elif "close" in Listen:
                        wind = GetWindowText(GetForegroundWindow()).lower()
                        if 'brave' in wind:
                            close_tab()
                        elif 'chrome' in wind:
                            close_tab()
                        else:
                            close()
                            sleep(4)
                            wind1 = GetWindowText(GetForegroundWindow()).lower()
                            check = wind1 in ms
                            if check:
                                speak('Do you want to save this?')
                                save = listen()
                                checkin = save in affirmative
                                if checkin:
                                    speak('Saving')
                                    pyautogui.press('enter')
                                    speak('What should be the name?')
                                    name = listen()
                                    typewrite(name)
                                    pyautogui.press('enter')
                                else:
                                    speak('closing')
                                    tab()
                                    pyautogui.press('enter')
                            else:
                                pass
                    elif 'play' in Listen:
                        Lisan = Listen.replace('play', '')
                        if 'music' in Lisan:
                            speak("Playing Music on youtube")
                            webbrowser.open_new(li.links[3])
                        else:
                            speak("Playing"+Lisan+" on youtube")
                            pywhatkit.playonyt(Lisan)
                    elif 'youtube' in Listen:
                        speak('playing on youtube!')
                        Listen1 = Listen.replace('play', '')
                        Listen2 = Listen1.replace('search', '')
                        Listen3 = Listen2.replace('on youtube', '')
                        pywhatkit.playonyt(Listen3)
                        break
                    elif 'resume' in Listen:
                        pyautogui.press('space')
                        pass
                    elif 'pause' in Listen:
                        pyautogui.press('space')
                        pass
                    elif 'joke' in Listen:
                        jokes()
                        pass
                    elif check:
                        index = questions.index(Listen)
                        speak(answers[index])
                        pass
                    elif 'what' in Listen:
                        Listen = Listen.replace('what', '')
                        if 'can you do ' in Listen:
                            speak(answers[1])
                        elif 'time' in Listen:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f" the time is {strTime}")
                        else:
                            Listen1 = Listen.replace('what is', '')
                            search(Listen1)
                        pass
                    elif 'current window' in Listen:
                        current_window()
                        pass
                    elif 'time' in Listen:
                        if 'timer' in Listen:
                            search_google(Listen.replace('on google', ''))
                        else:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f" the time is {strTime}")
                            pass
                    elif 'your favourite song' in Listen:
                        songs_random()
                        pass
                    elif 'who' in Listen:
                        Listen1 = Listen.replace('what is', '')
                        search(Listen1)
                        pass
                    elif 'send mail' in Listen:
                        mail()
                        pass
                    elif 'type' in Listen:
                        type_mode()
                        pass
                    elif 'minimize' in Listen:
                        pyautogui.hotkey('win', 'down')
                        pyautogui.hotkey('win', 'down')
                    elif 'full screen' in Listen:
                        pyautogui.press('f11')
                        pass
                    elif 'maximize' in Listen:
                        pyautogui.hotkey('win', 'up')
                        pyautogui.hotkey('win', 'up')
                    elif 'join meeting' in Listen:
                        zoom()
                        pass
                    elif 'sleep' in Listen:
                        speak('Okay!')
                        break
                    elif 'show' in Listen:
                        show()
                        pass
                    elif 'switch' in Listen:
                        Listen = Listen.replace('switch', '')
                        if 'tab' in Listen:
                            switch_tab()
                        else:
                            switch()
                        pass
                    else:
                        if 'google' in Listen:
                            search_google(Listen.replace('on google', ''))
                        else:
                            pass
            elif 'stop' in wake_up:
                speak('Okay')
                break
            else:
                pass
        except Exception:
            pass
