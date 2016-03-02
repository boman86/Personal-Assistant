import requests, json, time
from mpd import MPDClient
from voicePi import voice

# Connects to the MPD Server running on the Raspberry Pi and calls functions to complete certain tasks.
# Currently has limited capabilities due to inadequate understanding of the API.
# TODO: query song from Spotify, better voice output, removing of playlist, restart song.


def mpdInit():
    global client
    client = MPDClient()                        
    client.timeout = 10                          
    client.idletimeout = None                   
    client.connect("localhost", 6600)   
    client.password("1234")
    client.setvol(20)
    return client

# Takes in a function call from the main file that can also take in a query parameter 
# for use in querying songs/playlists as well as other variable inputs.
def mpdCommands(command, query):
    # Plays the next song
    if command == 'playSong':
        voice("playing song")
        client.play()
    elif command == 'nextSong':
        voice("playing next song")
        client.next()
    # Plays the previous song
    elif command == 'prevSong':
        client.previous()
        voice("playing previous song")
    # Pauses/Plays the current song
    elif command == 'pauseSong':
        data = client.status()
        state = data['state']
        if state == 'pause':
            voice("song resumed")
            client.pause()
        else: 
            client.pause()
            voice("song paused")
    # Voices the current song playing
    elif command == 'currentSong':
        client.setvol(5)
        data = client.currentsong()
        currentSong = data['title']
        artist = data['artist']
        voice("the current song is" + currentSong + " by " + artist)
        client.setvol(20)
    # Sets the volume for the MPD: 
    # NOT IMPLEMENTED
    elif command == 'setVolume':
        if query == 'less':
            client.volume(-10)
        elif query == 'more':
            client.volume(10)
        else:
            return
    # QUERY FUNCTIONS
    # query
    elif command == 'querySong':
        return
        # NOT IMPLEMENTED
    # Loads a playlist the user queries
    elif command == 'playPlaylist':
        client.load(query)
    else: 
        #do nothing
        return

def doubleChargeMeFoDat():
    voice("Ohhhhhhh, don't double charge me fo dat")

# closes the mpd client connection.
def mpdTerminate():
    client.close()                              
    print("client has closed")
    client.disconnect()   

mpdInit()
