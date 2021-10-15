# load libraries
import smtplib
from tkinter import *
import sys
# function to send mail
def send_mail()-> None:

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    #try with login by user credentials
    try:
        s.login(sender_email.get(),password.get())
        s.sendmail(sender_email.get(),receiver_email.get(),inputtxt.get("1.0","end-1c"))
        s.quit()
        return
    # if Email not send or not able to login
    except:
        response.place(relx=0.0,rely=0.85)
        response.config(text="Wrong Email or Password. Verify that you have access",font=15)
        print("There is issue with your email id or password\n")
        print("If you think your email or password is right..please make sure that give access to the third part or not using 2-Authentication\n")
        print("If you are using google account\nFollow these steps to make give access")
        print("Step1: Go to account setting")
        print("Step2: Go to Security tab")
        print("Go to  [Less secure app access]  and turn ON.    ")
        print("This is just for trial version of software")

# GUI program
def email_send():
    global response,label1_entry,label2_entry,label3_entry,inputtxt
    global message,sender_email,password,receiver_email,root

    root=Tk()
    root.geometry("500x500")
    message=StringVar()
    sender_email=StringVar()
    password=StringVar()
    receiver_email=StringVar()
    
    
    label1=Label(root,text="From",font=30)
    label1.place(relx=0.05,rely=0.05)

    label2=Label(root,text="Password",font=30)
    label2.place(relx=0.05,rely=0.15)

    label3=Label(root,text="To",font=30)
    label3.place(relx=0.05,rely=0.25)

    label1_entry=Entry(root,width=40,textvariable=sender_email)
    label1_entry.place(relx=0.35,rely=0.05)

    label2_entry=Entry(root,width=40,textvariable=password,show='*')
    label2_entry.place(relx=0.35,rely=0.15,)

    label3_entry=Entry(root,width=40,textvariable=receiver_email)
    label3_entry.place(relx=0.35,rely=0.25)

    inputtxt = Text(root, height = 11,width = 50,bg = "white")
    inputtxt.place(relx=0.08,rely=0.35)

    send_button= Button(root,text="Send",command=lambda:send_mail())
    send_button.place(relx=0.48,rely=0.75)

    response=Label(root,text="",font=30)
    response.place(relx=0.45,rely=0.85)

    root.mainloop()

if __name__ == "__main__":
    email_send()
