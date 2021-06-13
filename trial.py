from todo import *
import libraries as lib


if __name__ == '__main__':
    wishme()
    speak(li.arguments[1])
    while True:
        try:
            wake_up = listen_sleep()
            if 'wake up' in wake_up:
                reply()
                while True:
                    Listen = listen()
                    check = Listen in li.questions
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
                            lib.webbrowser.open_new('https://web.whatsapp.com/')
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
                            lib.sleep(3)
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
                        lib.sleep(4)
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
                                lib.pyautogui.press('enter')
                            else:
                                speak('closing')
                                tab()
                                lib.pyautogui.press('enter')
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
                        wind = lib.GetWindowText(lib.GetForegroundWindow()).lower()
                        if 'brave' in wind:
                            close_tab()
                        elif 'chrome' in wind:
                            close_tab()
                        else:
                            close()
                            lib.sleep(4)
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
                                    lib.pyautogui.press('enter')
                                else:
                                    speak('closing')
                                    tab()
                                    lib.pyautogui.press('enter')
                            else:
                                pass
                    elif 'play' in Listen:
                        Lisan = Listen.replace('play', '')
                        if 'music' in Lisan:
                            speak("Playing Music on youtube")
                            lib.webbrowser.open_new(li.links[3])
                        else:
                            speak("Playing"+Lisan+" on youtube")
                            lib.pywhatkit.playonyt(Lisan)
                    elif 'youtube' in Listen:
                        speak('playing on youtube!')
                        Listen1 = Listen.replace('play', '')
                        Listen2 = Listen1.replace('search', '')
                        Listen3 = Listen2.replace('on youtube', '')
                        lib.pywhatkit.playonyt(Listen3)
                        break
                    elif 'resume' in Listen:
                        lib.pyautogui.press('space')
                        pass
                    elif 'pause' in Listen:
                        lib.pyautogui.press('space')
                        pass
                    elif check:
                        index = li.questions.index(Listen)
                        speak(li.answers[index])
                        pass
                    elif 'what' in Listen:
                        Listen = Listen.replace('what', '')
                        if 'can you do ' in Listen:
                            speak(li.answers[1])
                        elif 'time' in Listen:
                            strTime = lib.datetime.datetime.now().strftime("%H:%M:%S")
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
                            strTime = lib.datetime.datetime.now().strftime("%H:%M:%S")
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
                        lib.pyautogui.hotkey('win', 'down')
                        lib.pyautogui.hotkey('win', 'down')
                    elif 'full screen' in Listen:
                        lib.pyautogui.press('f11')
                        pass
                    elif 'maximize' in Listen:
                        lib.pyautogui.hotkey('win', 'up')
                        lib.pyautogui.hotkey('win', 'up')
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
