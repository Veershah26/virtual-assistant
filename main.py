from modules.Apicommand import *
from modules.covid_cases import check_command_is_for_covid_cases
from modules.photo_with_python import *
from modules.ScreenShot import *
from modules.StressBusters import *
from modules.WallpaperScrapper import *
from modules.weather import *
from modules.wiki import *
from modules.YoutubeVideoDownloader import *
import pyttsx3
import datetime

from modules.net_speed import download_speed, ping, upload_speed
from modules.price import price
from modules.quotes import *
import speech_recognition as sr
from modules.mp3 import *
from modules.send_mail import *
from modules.shopping_list_maker import *
ttsengine = pyttsx3.init()

def speak(audio):
    ttsengine.say(audio)
    ttsengine.runAndWait()

def getvoices(voice):
    voices = ttsengine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        ttsengine.setProperty('voice', voices[0].id)

    if voice == 2:
        ttsengine.setProperty('voice', voices[1].id)

    speak("Hello Darkness My Old Friend")

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The Current Time Is")
    speak(Time)
    # print(Time)

def date():
    today = datetime.datetime.now()
    today_date = today.strftime("%m/%d/%Y")
    speak("The Current Date Is ")
    speak(today_date)

# while True:
#     voice = int(input("Enter 1 or 2: "))
#     speak(audio)
#     getvoices(voice)
# time()

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12 :
        speak("Good Morning Sir !")
    elif hour >=12 and hour <18 :
        speak("Good Afternoon Sir !")
    else :
        speak("Good Evening Sir !")


def wishme():
    speak("Welcome Back Sir!")
    greeting()
    time()
    date()
    speak("How May I Help You")

# wishme()

def takecmd():
    query = input("Please Tell Me How May I Help You ? \n")
    return query

def takecmdmic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-IN")
        print(query) 
    except Exception as e:
        print(e)
        speak("Pardon Me Sir. Can you say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    
    wishme()
    api()
    photo_with_python()
    playmusic()
    email_send()
    take_command() # to make shoppinf list
    StressBusters()
    
    WallpaperScrapper() 
    #weather function which doesnt work because of non existent api key
    # temp()
    # detail()
    # rain()
    # pressure()
    # wind()
    # humidity()
    # clouds()
    wiki('Python')
    downloadYtMp4('https://www.youtube.com/watch?v=lHhRhPV--G0') #random video to test functionality
    while True:
        query = takecmdmic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'active cases of covid' in query:
            cases=check_command_is_for_covid_cases(query)
            print(cases)
            speak(cases)

        elif "download speed" in query:
            speak(f'Download Speed is {download_speed()} MB/s')

        elif "upload speed" in query:
            speak(f'Uplaod Speed is {upload_speed()} MB/s')

        elif "ping" in query:
            speak(f'Ping is {ping()}')

        elif "depressed" in query:          # There are many quotes available in quotes.py file
            quote=random_quote()
            print(quote)
            speak(quote)
        elif "bitcoin" in query and "price" in query:       # Not only Bitcoin , you can try other currencies also: reffer price.py file
            r=price('bitcoin')
            print(r)
            speak(r)
        
        elif "currency price" in query:
            coin=str(takecmdmic().lower())
            p=price(coin)
            print(p)
            speak(p)

        elif 'bye' in query or 'else' in query:
            exit()
