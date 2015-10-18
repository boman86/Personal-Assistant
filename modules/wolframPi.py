import wolframalpha
import xmltodict
from voiceTTS import voice

# initialize Wolfram Alpha ID
appid = 'YRT5RT-4H23GGJQXG'
client = wolframalpha.Client(appid)

query1 = 'weather tomorrow in Pittsburgh, PA'

# for pod in res.pods:
#     print(pod.title)
#     print(pod.text.encode('utf-8').strip())

#xmltodict.parse(res)

def queryWolfram(query):
    res = client.query(query)

    # This part is used if you want to format a certain response from the text given 
    # back to you from WolframAlpha. 
    if ('weather' or 'forecast' in res.pods[0].text.encode('utf-8').strip()):
        print("hey u got here nice!")
        voice("good job dude")
        return
    else:
        return

queryWolfram(query1)