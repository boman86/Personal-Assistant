import pyttsx

# A text-to-speech engine using pyttsx. 

def voice123(input):
    engine = pyttsx.init()

    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    
    engine.setProperty('volume', volume-0.5)
    engine.setProperty('rate', rate-65)
    engine.say(input)
    
    engine.runAndWait()

