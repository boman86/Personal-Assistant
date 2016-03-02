import pyttsx
from gtts import gTTS
import os
from os import system
import sys

# Text-to-speech with pyttsx or gtts (Google Text to Speech).

def voicePyttsx(input):
    engine = pyttsx.init()

    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')

    engine.setProperty('volume', volume-0.5)
    engine.setProperty('rate', rate-65)
    if input != "":
        engine.say(input)
    else: 
        print("there is nothing to say")

    engine.runAndWait()

# TTS implementation using Google TTS API.
def voiceGtts(input):
    tts = gTTS(text=input, lang='en')
    tts.save("temp.mp3")
    os.system("afplay temp.mp3")
    os.system("rm temp.mp3")

# temporary voice for debugging when testing on a Mac
def macVoice(input):
    system('say -v Victoria ' + "'" + input + "'")

# Choose the library to use for TTS:
def voice(input):
    if (sys.platform == "darwin"):
        macVoice(input)
    else:
        voicePyttsx(input)
    