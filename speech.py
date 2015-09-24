import wit, json, time

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"

    wit.init()

    wit.voice_query_start(WIT_AI_KEY)

    time.sleep(5)

    response = wit.voice_query_stop()
    
    print('response: {}'.format(response))
    print(getIntent(response))

    chooseIntent(getIntent(response))
    wit.close()

def getIntent(response):
    parsed_response = json.loads(response)
    if(parsed_response['_text'] == None):
        return 'errorparse' 
    return parsed_response['outcomes'][0]['intent']
        
    
def chooseIntent(intent):
    intent = intent.lower()
    if(intent == 'startup'):
        print('@THIS IS WHEN APOLLO TAKES QUESTIONS@')
    elif (intent == 'errorparse'):
        main()
    else:
        main()

    
if __name__ == '__main__':
        main()


