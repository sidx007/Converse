import webbrowser
import pyautogui as pyt
from time import sleep
import pyperclip
import pyttsx3

math = 'https://keep.google.com/u/0/#NOTE/19jlkBFUxUaBX9b9q_-oD2dA15J1Xxa9sWOo8hpSxcAnNucCTf9VmpUfXr-YjXiE8HZc14g'
english = 'https://keep.google.com/u/0/#NOTE/12cJiexjtWPi-Hr84JBhgwVOXOeCRhqFnZjzAry_XweGVyf37m_CNF4RD66Xuj5cWppH5wg'
physical = 'https://keep.google.com/u/0/#NOTE/1c8bo1r7epmwTzULhbJZe4TcQ1bWGOTktuHfH9MgLi8veuG5iPQx0gt5deCPzp2DDQfUh0g'
physics = 'https://keep.google.com/u/0/#NOTE/1T-s0uRH-6kzcFxTlL6hhH2mEbKN5DyJe39XDBgmGkQ5tGXLAj981wGjpLjtXoIw'
chemistry = 'https://keep.google.com/u/0/#NOTE/1Ld0fO_9yI2GVcujxo9plixfWRh4J2eWcZnoKLKGo67UUF-ZidDJ0ofR7ZSuZLztZ'

subjects = [math, english, physical, physics, chemistry]
math_index = 0


def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def extraction(invite):
    invite = invite.split()
    invite_length = len(invite)
    for i in range(invite_length):
        length = len(invite[i])
        if length >= 30:
            pyt.hotkey('ctrl', 'a')
            webbrowser.open(invite[i])
            sleep(2)
        else:
            pass


def opens(subject, name):
    webbrowser.open(subject)
    speak('joining ' + name + ' class')
    sleep(10)
    pyt.hotkey('ctrl', 'a')
    pyt.hotkey('ctrl', 'c')
    copied = pyperclip.paste()
    extraction(copied)


def opening():
    while True:
        pyperclip.copy(' ')
        ask = input('Which subject?')
        if ask == 'math':
            opens(math, 'math')
        elif ask == 'physics':
            opens(physics, 'physics')
        elif ask == 'physical':
            opens(physical, 'physical')
        elif ask == 'chemistry':
            opens(chemistry, 'chemistry')
        elif ask == 'english':
            opens(english, 'english')
        elif ask == 'end':
            break
        else:
            print('Please write again')


opening()
