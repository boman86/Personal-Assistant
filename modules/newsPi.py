import json, urllib2
import random
from voicePi import voice

## We use the Reddit json API to retrieve recent headlines for different subreddits.

inquiry = ['What would you like to know more about?']

def getNews():
    try:
        inquire()
    except:
        getNews()

def inquire():
    # voice(random.choice(inquiry))
    # voice("here give me a second")
    category = 'technology'
    response = urllib2.urlopen('http://www.reddit.com/r/' + category + "/top/.json").read()

    headlines = json.loads(response)

    # print json.dumps(headlines, sort_keys=True, indent=4, separators=(',', ': '))

    voice("How many articles would you like to hear about?")

    for i in range(0,5):
        print headlines['data']['children'][i]['data']['title'] + "\n"

    voice(headlines['data']['children'][0]['data']['title'])
    voice("would you like to hear more?")
    voice(headlines['data']['children'][1]['data']['title'])


    # for child in headlines['data']['children']:
    #     print child['data']['title'] + "\n"

    # print headlines['data']['children'][0]['data']['title']

    voice("hello ")


getNews()