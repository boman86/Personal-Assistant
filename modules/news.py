import json, urllib2
import random
from voiceTTS import voice

## We use the Reddit json API to retrieve recent headlines for different subreddits.

inquiry = ['What would you like to know more about?']

def inquire():
    # voice(random.choice(inquiry))
    # voice("here give me a second")
    category = 'technology'
    response = urllib2.urlopen('http://www.reddit.com/r/' + category + "/top/.json").read()

    headlines = json.loads(response)

    # for i in range(1,10):
    #     print headlines['data']['children'][i]['data']['title'] + "\n"

    for child in headlines['data']['children']:
        print child['data']['title'] + "\n"


