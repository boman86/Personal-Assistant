import urllib2
import json, time
from voiceTTS import voice

## Weather query using AerisWeather's endpoints. Currently only able to search a location.
## TODO: work on adding dates and time functionality.

client_id = "UcCeJM6gd028K9xE05Vow"
client_secret = "FASHb2b3NSjVRMckM2XOwrpZSRItun8jS1jzmJsw"

## Adds to the output a comment on whether to bring a jacket/ umbrella/ etc.
## TODO: NONE.
def weatherComment(temp, precip, snow):
    comment = ""
    # Parse temperature:
    if temp <= 40:
        comment = comment + "Bring a jacket."
    elif temp <= 60: 
        comment = comment + "Bring a light jacket."
    else:
        comment = comment + "The weather is really nice today."
    # parse for precipitation:  
    if precip > 30: 
        if not (temp <= 60):
            comment = comment + " but"
        else: 
            comment = comment + " and"
        comment = comment + " also bring an umbrella."
    # parse for snow
    if snow != 0:
        comment = comment + ""  

    # check to add "remember to..."
    if (comment != ""):
        return "Remember to " + comment
    else: 
        return comment

## Makes a get request to AerisWeather's forecasts endpoint and parses the response to a voice output
## TODO: Add date/time specifications.
def weatherLocation(location):
    response = urllib2.urlopen("http://api.aerisapi.com/forecasts/" + location + "?client_id=" + client_id + "&client_secret=" + client_secret).read()
    weather = json.loads(response)
    if weather['success']:
        period = weather['response'][0]['periods'][0]
        tempAvg = period['avgTempF']
        tempMax = period['maxTempF']
        tempMin = period['minTempF']
        precip = period['pop']
        snow = period['snowIN']
        wind = str(period['windGustMPH'])
        # voice output
        voice("The current weather in " + location + " is " + str(period['weather']))
        voice ("There will be a high of " + str(tempMax) + "and low of " + str(tempMin) + " degrees fahrenheit, with a " + str(precip) + " percent chance of rain.")
        voice(weatherComment(tempAvg, precip, snow))
    else: 
        print("An error has occured:" + weather['error']['description'])

