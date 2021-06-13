from functions import *
from libraries import *
from libraries import pyautogui as pyt
import pyperclip


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


math = 'https://keep.google.com/u/0/#NOTE/19jlkBFUxUaBX9b9q_-oD2dA15J1Xxa9sWOo8hpSxcAnNucCTf9VmpUfXr-YjXiE8HZc14g'
english = 'https://keep.google.com/u/0/#NOTE/12cJiexjtWPi-Hr84JBhgwVOXOeCRhqFnZjzAry_XweGVyf37m_CNF4RD66Xuj5cWppH5wg'
physical = 'https://keep.google.com/u/0/#NOTE/1c8bo1r7epmwTzULhbJZe4TcQ1bWGOTktuHfH9MgLi8veuG5iPQx0gt5deCPzp2DDQfUh0g'
physics = 'https://keep.google.com/u/0/#NOTE/1T-s0uRH-6kzcFxTlL6hhH2mEbKN5DyJe39XDBgmGkQ5tGXLAj981wGjpLjtXoIw'
chemistry = 'https://keep.google.com/u/0/#NOTE/1Ld0fO_9yI2GVcujxo9plixfWRh4J2eWcZnoKLKGo67UUF-ZidDJ0ofR7ZSuZLztZ'


def openi():
    try:
        while True:
            pyperclip.copy(' ')
            speak('Which subject?')
            ask = main_listen().lower()
            print(ask)
            if 'math' in ask:
                opens(math, 'math')
            elif 'physics' in ask:
                opens(physics, 'physics')
            elif 'physical' in ask:
                opens(physical, 'physical')
            elif 'chemistry' in ask:
                opens(chemistry, 'chemistry')
            elif 'english' in ask:
                opens(english, 'english')
            elif 'end' in ask:
                break
            else:
                speak('Please speak again')
    except Exception:
        pass


if __name__ == '__main__':
    openi()
