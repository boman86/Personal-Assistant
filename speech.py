import wit, json, time
import os, pygame
from voiceTTS import voice

## ------------------------------------------------------------------------------
## Main function simulates an always-on microphone waiting for a voice command
## given by a keyword read through a configuration file.
## ------------------------------------------------------------------------------

# Initialize API keys and speech recognition
WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"

## Main function that just loops and waits for user to say keyword.
## Status: TODO: flexibility (maybe merge with checkStartup), switch to PocketSphinx
def main():            
    # initialize WIT.AI
    wit.init()

    wit.voice_query_start(WIT_AI_KEY)

    time.sleep(4)

    response = wit.voice_query_stop()

    # case for the keyword voice command
    checkStartup(getIntent(response))
    wit.close()

## This main query is for the user command called after the user activates the personal assistant
## casing on the various intents WIT.AI returns.
## Status: TODO: null checks
def mainQuery():            
    # initialize WIT.AI
    wit.init()

    query = wit.voice_query_auto(WIT_AI_KEY)

    chooseIntent(getIntent(query))

    wit.close()
    main()

## Retrieves the user's intents from the WIT.AI Json response.
## Status: DONE.
def getIntent(response):
    # convert returned api call to json object
    parsed_response = json.loads(response)
    # check for null response from server
    if(parsed_response['_text'] == None):
        return 'errorparse' 
    return parsed_response['outcomes'][0]['intent']
    
## Checks if the user has called the name of the personal assistant
## Status: TODO- retrives pa name from file
def checkStartup(intent):
    # convert all responses to universal lower-case
    intent = intent.lower()

    # if intent is to "startup" we call to the initiate function
    if(intent == 'startup'):
        os.system('aplay -D plughw:1 ~/Repos/Personal-Assistant/sounds/initialization_beep.wav')
        voice123('what is up richard?')
        mainQuery()
    # if there is no intent we have no command and we wait for another one
    else:
        main()

## Chooses which module to call with the intent given back from WIT.AI
## Status: Heavily WIP.
def chooseIntent(intent):











