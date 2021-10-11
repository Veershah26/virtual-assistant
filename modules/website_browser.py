import webbrowser
import os

def website():
    user = input()
    if 'open website' in user or 'open site' in user:
        website = input('Which website do you want to open? For example - youtube.com, gmail.com, etc: ')
        webbrowser.open(website)
        print(f"I have opened {website}")

def edge():
    user = input()
    if 'open edge' in user or 'open microsoft edge' in user:
        try:
            edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edge)
            print("I have opened MicroSoft Edge")

        except Exception as e:
            print("Looks like you don't have Microsoft Edge on your system")


def chrome():
    user = input()
    if 'open chrome' in user or 'open google' in user:
        try:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
            print("I have opened Google Chrome")

        except Exception as e:
            print("Looks like you don't have Google Chrome on your system")
