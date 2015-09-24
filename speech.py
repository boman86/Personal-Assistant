import pyaudio, os, subprocess
import wit

def main():
    # Initialize API keys and speech recognition
    WIT_AI_KEY = "45SK2K6B7EUC6GOJY26N2REG7LRJF4BT"

    wit.init()

    response = wit.voice_query_auto(WIT_AI_KEY)
    print('response: {}'.format(response))

    wit.close()
    
if __name__ == '__main__':
        main()


