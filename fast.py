import pyautogui

students = {'1064': True, '1067': True, '1191': True, '1210': True, '1218': True, '1230': True, '1249': True,
            '1251': True,
            '1257': True, '1272': True, '1281': True, '1293': True, '1299': True,
            '1305': True, '1306': True, '1334': True, '1352': True, '1357': True,
            '1368': True, '1370': True, '1377': True, '1389': True, '1393': True, '1423': True}


# 1357

def present():
    pyautogui.typewrite('P')
    pyautogui.press('Enter')


def absent():
    pyautogui.typewrite('A')
    pyautogui.press('Enter')


def iterate(gm):
    gm = gm.split()
    for i in gm:
        students[i] = False
    for i in students:
        if students[i]:
            present()
        elif not students[i]:
            absent()
        else:
            pass


def pressup(no):
    for i in range(no):
        pyautogui.press('Up')


def final(student):
    iterate(student)
    pyautogui.press('right')
    pressup(24)
    iterate(student)
    pyautogui.press('right')
    pressup(24)
    iterate(student)

