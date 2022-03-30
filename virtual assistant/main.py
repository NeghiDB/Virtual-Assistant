import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_cmd, open_notepad, open_browser
from pprint import pprint
#from functions.jarvis import speak, greet_user, take_user_input
from AIByName import *
# for keyboard mode
import pyautogui

USER = config('USER')
BOTNAME = config('BOTNAME')

if __name__ == '__main__':
    '''if 'activate' in query'''
    speak(f"I am alive, aren't I. Well it doesn't matter now. Hey boss. All systems activated")
    print('All systems activated')
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open browser' in query:
            open_browser()

        elif 'open calculator' in query:
            open_calculator()
        
        elif 'introduce yourself' in query:
            speak(f"Hi! I'm {BOTNAME} and I'm an Artificial Intelligence created by Mister {USER} here. I should tell you more but\
                I have not been given instructions to say more than this. You're however welcome to this event.")
        
        elif 'hello' in query:
            speak(f"Hi Nosa, what can I do for you today")
                        
        elif 'next' in query:
            pyautogui.press('right')

        elif 'previous' in query:
            pyautogui.press('left')

        elif 'select' in query:
            pyautogui.press('enter')

        elif 'do the presentation' in query:
            speak(f"Ladies and genlemen, I would transfer the presentation back to my boss, I'm too scared to do this")


        elif 'typing mode' in query:
            speak(f"I'm waiting for your input sir")
            print('Waiting for your input...')
            sentence = take_user_input().capitalize()
            pyautogui.write(sentence, interval=0.2)

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'say goodbye' in query:
            speak(f"Sanjooma")
            speak(f"Sai Gobe!")
            speak(f"Sai wata rana!")
            speak(f"For those of you that do not understand what I have just said")
            speak(f"I'll interprete it'")
            speak(f"Bye")
            speak(f"Till tommorrow")
            speak(f"Till we meet again")

#2170