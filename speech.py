import wit, json, time
import os, pygame
from voiceTTS import voice123

# Main function simulates an always-on microphone waiting for a voice command
# given by a keyword read through a configuration file.

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"
            
    # initialize WIT.AI
    wit.init()

    wit.voice_query_start(WIT_AI_KEY)

    time.sleep(4)

    response = wit.voice_query_stop()

    # case for the keyword voice command
    chooseIntent(getIntent(response))
    wit.close()

def mainQuery():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"
            
    # initialize WIT.AI
    wit.init()

    response = wit.voice_query_auto(WIT_AI_KEY)

    ##DEBUG##
    print('response: {}'.format(response))
    print(getIntent(response))

    wit.close()


def getIntent(response):
    # convert returned api call to json object
    parsed_response = json.loads(response)
    # check for null response from server
    if(parsed_response['_text'] == None):
        return 'errorparse' 
    return parsed_response['outcomes'][0]['intent']
    
def chooseIntent(intent):
    # convert all responses to universal lower-case
    intent = intent.lower()

    # if intent is to "startup" we call to the initiate function
    if(intent == 'startup'):
        os.system('aplay -D plughw:1 ~/Repos/Personal-Assistant/sounds/initialization_beep.wav')
        voice123('what is up richard?')
        print('@THIS IS WHEN APOLLO TAKES QUESTIONS@')
        mainQuery()
    # if there is no intent we have no command and we wait for another one
    else:
        main()

    
if __name__ == '__main__':
        main()


