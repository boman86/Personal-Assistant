import tungsten
from voicePi import voice

# remember to install xmlutils

# initialize Wolfram Alpha ID
appid = 'YRT5RT-4H23GGJQXG'
client = tungsten.Tungsten(appid)

query1 = "asdalskdmasldkasm"

# for pod in res.pods:
#     print(pod.title)
#     print(pod.text.encode('utf-8').strip())

#xmltodict.parse(res)

def queryWolfram(query):
    response = client.query(query)

    try: 
        print response.pods[1].format['plaintext'][0]
        voice("Do you want on this subject?")
    except:
        voice("I don't understand what you're saying")

        

    # if response.success:
    #     for pod in response.pods:
    #         print pod.title
    #         print "==============="
    #         print pod.format['plaintext'][0]



queryWolfram(query1)