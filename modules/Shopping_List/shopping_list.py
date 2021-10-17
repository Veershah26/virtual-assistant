import speech_recognition as sr
import pyttsx3

ttsengine = pyttsx3.init()

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

def speak(audio):
    ttsengine.say(audio)
    ttsengine.runAndWait()



def shplist():
    query = takecmdmic
    if 'shopping list' in query:
        speak("what would you like to add to the shopping list?")
        query = takecmdmic
        l=query.split()
        print(l)
        my_list = open("shopping_list.txt","w")
        count=1
        for i in l:
            my_list.write(str(count) + ") " + i + "\r\n")
            count+=1
        my_list.close()
        speak("Your list was made and save in a text file named Shopping List")

shplist()





