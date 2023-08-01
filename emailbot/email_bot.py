from smtplib import SMTP
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

engine=pyttsx3.init()
listener=sr.Recognizer()

email_list={
    "deepak":"ds1817165@gmail.com",
    "vishnu":"vishnu27902@gmail.com",
    "nishan":"kracojohn220103@gmail.com",
    "arun":"arunkumar.pece2020@sece.ac.in"
}
#to talk for getting the user response
def talk(text):
    engine.say(text)
    engine.runAndWait()

#to recognize what user is talking and converts it into text
def get_info():
    try:
        with sr.Microphone() as src:
            listener.adjust_for_ambient_noise(src, duration=1)
            print("Listening....")
            voice=listener.listen(src,0,10)
            info=listener.recognize_google(voice)
            return info.lower()
    except Exception as e:
        print(e)

#actually to send an email
def send_email(receiver,subject,message):
    server=SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("deepak.b2020ece@sece.ac.in","Deepak2003@")

    email=EmailMessage()
    email['From']="deepak.b2020ece@sece.ac.in"
    email['To']=receiver
    email["Subject"]=subject
    email.set_content(message)
    server.send_message(email)
def get_email_info():
    talk("to whom you want to send email")
    name=get_info()
    receiver=email_list[name]
    talk("what is the subject of your email")
    subject=get_info()
    talk("Tell me the text in your email")
    message=get_info()
    send_email(receiver,subject,message)

get_email_info()

