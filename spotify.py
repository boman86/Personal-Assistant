import requests, spotipy

username = "11120727761"
token = "BQDHonvdAR7ciSOVnDMKLlZA7M9leNtYFwS3WXEMOWy841NLkq6-XcQFCYyicvlvtvL83rDWxOF3CVxux7JaTh0JAC2vTP_XQlgRn1khrSuUStKnuivZmJxJG6HC93Uzff2k0W5OjcTjiNLc4opE_BEODWoS8QwCsY8x"
payload = {"Authorization": token}

# Added implementation for extracting Urls and information from Spotify, using the Spotify HTTP requests 
# and Spotipy functions. In the current state, a user token and username is hardcoded. Further 
# implementations will fix this.

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
