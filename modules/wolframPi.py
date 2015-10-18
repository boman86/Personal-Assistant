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
    interpretation = res
    result = res.pods[1].text.encode('utf-8').strip()

    print result
    # This part is used if you want to format a certain response from the text given 
    # back to you from WolframAlpha. 
    if ('weather' or 'forecast' in response):
        voice(result)

queryWolfram(query1)