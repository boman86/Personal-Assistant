import pyaudio, os, subprocess
import speech_recognition as sr
from os import system

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"
    r = sr.Recognizer()
    r.pause_threshold = 0.5
        
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)

        # Case on keyword "APOLLO"
        try: 
            # Try to recognize audio
            user = r.recognize_wit(audio, key=WIT_AI_KEY)
            
            # DEBUGGING PURPOSES

            if user.lower() == "banana":
                # Simulate taking in a command by beeping
                audio_file = "/Users/richard/Desktop/Repos/PersonalAssistant/sounds/initialization_beep.wav"
                return_code = subprocess.call(["afplay", audio_file])
                system('say what''s up?')
                break
        except:
            print("");
            # error debugging


if __name__ == '__main__':
        main()


