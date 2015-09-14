import pyaudio,os
import speech_recognition as sr

def excel():
        print("excel started");

def internet():
        print("internet started");

def media():
        print("media started");

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio, key="")
    print(user)
    if user == "Excel":
        excel()
    elif user == "Internet":
        internet()
    elif user == "music":
        media()

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)



