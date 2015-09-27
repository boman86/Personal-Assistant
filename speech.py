import wit, json, time

# Main function simulates an always-on microphone waiting for a voice command
# given by a keyword read through a configuration file.

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"

    # initialize WIT.AI
    wit.init()

    wit.voice_query_start(WIT_AI_KEY)

    # sleep 5 seconds to chop voice queries to manageable sections
    time.sleep(5)
    # retrieve reponse from server
    response = wit.voice_query_stop()

    ##DEBUG##
    print('response: {}'.format(response))
    print(getIntent(response))

    # case for the keyword voice command
    chooseIntent(getIntent(response))
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
        print('@THIS IS WHEN APOLLO TAKES QUESTIONS@')
    # if there is no intent we have no command and we wait for another one
    main()

    
if __name__ == '__main__':
        main()


