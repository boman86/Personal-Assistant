import wit, json

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"

    wit.init()

    response = wit.voice_query_auto(WIT_AI_KEY)
    parsed_response = json.loads(response)
    print('response: {}'.format(response))
    print(parsed_response['intent'])

    wit.close()
    
if __name__ == '__main__':
        main()


