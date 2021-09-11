import pyttsx3

ttsengine = pyttsx3.init()

def speak(audio):
    ttsengine.say(audio)
    ttsengine.runAndWait()

while True:
    audio = input("Enter Text To Be Spoken: ")
    speak(audio)