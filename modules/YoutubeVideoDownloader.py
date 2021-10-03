from pytube import YouTube
import os


def downloadYtMp4(ytURL, dlDir=os.getcwd()):
    yt = YouTube(ytURL)
    try:
        print("Downloading...")
        yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1].download()
    except:
        print("ERROR | Please try again later")
    print(f"Donwload Complete | Saved at {os.getcwd()}")


downloadYtMp4("URL")
