# load libraries
import imaplib
import email
import speech_recognition as sr
import pyttsx3
from modules.shopping_list_maker import text_to_speech
from datetime import date
r = sr.Recognizer()

def emain_opener():
    # start of program
    text_to_speech("Hello USer..I am your Email opener")

    text_to_speech("Do you like to open your Inbox")
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio=r.listen(source)
            response=r.recognize_google(audio)
            response=response.lower()
            if response=="yes":
                text_to_speech("This is only valid for Gmail-user")
                res=1
                # looping till it not get right input
                while(res==1):
                    try:
                        # Enter credentials
                        text_to_speech("Enter you Gmail-ID")
                        username =input("Email-id: ")
                        text_to_speech("Enter your password")
                        app_password= input("Password: ")
                        host_server='imap.gmail.com'
                        mail = imaplib.IMAP4_SSL(host_server)
                        mail.login(username, app_password)
                        res=0
                    except:
                        text_to_speech("Wrong Email_ID or password..I hope you alredy given access to the gmail to use third party access")
                        text_to_speech("Enter credentials again")
                        
                
                mail.select("INBOX")
                today_date=str(date.today())
                result1, selected_mails = mail.search(None,'UNSEEN')
                selected_mail2=selected_mails[0].split()
                selected_mail2=sorted(selected_mail2,reverse=True)
                text_to_speech("There are total "+str(len(selected_mail2))+" unseen mails")
                text_to_speech("Do I read it for you")
                audio=r.listen(source)
                response=r.recognize_google(audio)
                response=response.lower()
                # display only top 10 unseen emails
                if response=="yes":
                    counter=0
                    for num in selected_mail2:
                        if counter==10:
                            text_to_speech("I am done with newest 10 emails.So I am exiting")
                            break
                        else:
                            counter+=1
                        result2,data=mail.fetch(num , '(RFC822)')
                        result3, bytes_data = data[0]
                        email_message = email.message_from_bytes(bytes_data)
                        print("\n*********************************************")
                        print("Subject: ",email_message["subject"])
                        print("To:", email_message["to"])
                        print("From: ",email_message["from"])
                        print("Date: ",email_message["date"])
                        text_to_speech("There is a mail from "+email_message['from']+" to you"+"on "+ email_message["date"]+"with subject "+email_message["subject"])
                        text_to_speech("")
                        for part in email_message.walk():
                            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                                message = part.get_payload(decode=True)
                                print("Message: \n", message.decode())
                                print("************************************************\n")
                                break
                    return

                else:
                    text_to_speech("okk fine. So I am exiting")
                    return
            # exit if you dont want
            else:
                text_to_speech("Okk no problem..Tell me when you need me")
                return
    # exit condition if any thing wrong in the above function.
    except sr.RequestError as e:
        text_to_speech("There is some problem. Try after some time")
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        text_to_speech("There is some problem. Try after some time")
        print("unknown error occured")


if __name__=="__main__":
    emain_opener()
