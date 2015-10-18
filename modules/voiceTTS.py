import pyttsx

# A text-to-speech engine using pyttsx. 

def voice(input):
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

