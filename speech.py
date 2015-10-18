import wit, json, time
import os, pygame
import sys
sys.path.append('/home/pi/Repos/Personal-Assistant/modules')
from spotifyPi import *
from voiceTTS import voice
from weatherPi import weatherLocation

## ------------------------------------------------------------------------------
## Main function simulates an always-on microphone waiting for a voice command
## given by a keyword read through a configuration file.
## ------------------------------------------------------------------------------

# Initialize API keys and speech recognition
WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"
# Initialize global MPD Client
mpdInit()

## Main function that just loops and waits for user to say keyword.
## Status: TODO: flexibility (maybe merge with checkStartup), switch to PocketSphinx
def main():            
    # initialize WIT.AI
    wit.init()

    wit.voice_query_start(WIT_AI_KEY)

    time.sleep(3)

    response = wit.voice_query_stop()
    wit.close()

    # case for the keyword voice command
    checkStartup(getIntent(response))

## This main query is for the user command called after the user activates the personal assistant
## casing on the various intents WIT.AI returns.
## Status: TODO: null checks
def mainQuery():            
    # initialize WIT.AI
    wit.init()

    try:
        response = wit.voice_query_auto(WIT_AI_KEY)
        chooseIntent(response)
    except TypeError:
        main()
        wit.close()
        return

    wit.close()

## Retrieves the user's intents from the WIT.AI Json response.
## Status: DONE.
def getIntent(response):
    # convert returned api call to json object
    parsed_response = json.loads(response)
    # check for null response from server
    if(parsed_response['_text'] == None):
        return 'errorparse' 
    else:
        return parsed_response['outcomes'][0]['intent']

## Retrieves the user's entities from the returned json
## Status: DONE.
def getEntities(response):
    # convert returned api call to json object
    parsed_response = json.loads(response)
    # check for null response from server
    if(parsed_response['_text'] == None):
        return 'errorparse' 
    else:
        return parsed_response['outcomes'][0]['entities']
    
## Checks if the user has called the name of the personal assistant
## Status: TODO- retrives pa name from file
def checkStartup(intent):
    # convert all responses to uniform lower-case
    intent = intent.lower()

    # if intent is to "startup" we call to the initiate function
    if(intent == 'startup'):
        os.system('aplay -D plughw:1 ~/Repos/Personal-Assistant/sounds/initialization_beep.wav')
        voice('what is up richard?')
        mainQuery()
        return
    elif (intent == 'appreciation'):
        voice("no problem")
        main()
        return
    elif (intent == 'terminate'):
        voice("farewell Richard")
        return
    # if there is no intent we have no command and we wait for another one
    else:
        main()
        return

## Chooses which module to call with the intent given back from WIT.AI
## Status: Heavily WIP.
def chooseIntent(response):
    # convert all responses to uniform lower-case
    intent = getIntent(response)
    intent = intent.lower()

    print(intent)

    # parse for commands:
    if (intent == 'playaudio'):
        mpdCommands("playPlaylist", "welcome to the house") # default hype playlist
        mpdCommands("playSong", None)
    elif (intent == 'playplaylist'):
        voice("playing the playlist " + getEntities(response)['playlist'][0]['value'])
        mpdCommands("playPlaylist", getEntities(response)['playlist'][0]['value'])
        mpdCommands("playSong", None)
    elif (intent == 'stopsong'):
        print("this should stop the song")
        mpdCommands('pauseSong', None)
        print("no?")
    elif (intent == 'nextsong'):
        mpdCommands('nextSong', None)
    elif (intent == 'appreciation'):
        voice("no problem")
    elif (intent == 'weather'):
        loc = getEntities(response)['location']['value']
        weatherLocation(loc)
    else: 
        main()
        return
    main()


main()









