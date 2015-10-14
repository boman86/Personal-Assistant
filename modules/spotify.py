import requests, json
from mpd import MPDClient
from voiceTTS import voice

username = "11120727761"
token = "BQDHonvdAR7ciSOVnDMKLlZA7M9leNtYFwS3WXEMOWy841NLkq6-XcQFCYyicvlvtvL83rDWxOF3CVxux7JaTh0JAC2vTP_XQlgRn1khrSuUStKnuivZmJxJG6HC93Uzff2k0W5OjcTjiNLc4opE_BEODWoS8QwCsY8x"
payload = {"Authorization": token}

# Added implementation for extracting Urls and information from Spotify, using the Spotify HTTP requests 
# and Spotipy functions. In the current state, a user token and username is hardcoded. Further 
# implementations will fix this.

client = MPDClient()                        # create client object
client.timeout = 10                          # network timeout in seconds (floats allowed), default: None
client.idletimeout = None                   # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("192.168.0.103", 6600)       # connect to localhost:6600
client.password("1234")
client.setvol(10)

def main():
    getArtistUrl("Jason Mraz")


def getArtistUrl(name):
    sp = spotipy.Spotify()
    artists = sp.search(name, 10, 0, 'artist')

    # print artists['artists']['items'][0]['external_urls']['spotify']

    return artists;


def listPlaylist(name):
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(name)

    # for playlist in playlists['items']:
    #     if playlist['owner']['id'] == username:
    #         print
    #         print playlist['name']

    return playlists


def mpdCommands(command, query):
    if command == 'nextSong':
        client.next()
        voice("playing next song")
    elif command == 'prevSong':
        client.previous()
        voice("playing previous song")
    elif command == 'pauseSong':
        data = client.status()
        state = data['state']
        if state == 'pause':
            voice("song resumed")
            client.pause()
        else: 
            client.pause()
            voice("song paused")
    elif command == 'playPlaylist':
        client.load(query)
    elif command == 'currentSong':
        client.setvol(3)
        data = client.currentsong()
        currentSong = data['title']
        artist = data['artist']
        voice("the current song is" + currentSong + " by " + artist)
        client.setvol(10)
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
        client.searchAdd
    
    else: 
        #do nothing
        return
    
# print(client.listplaylists())
mpdCommands("currentSong", None)
mpdCommands("setVolume", 'more')

client.close()                              # send the close command
print("client has closed")
client.disconnect()   
