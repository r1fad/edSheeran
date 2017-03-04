import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json 

#create spotify object
client_credentials_manager = SpotifyClientCredentials("1000c5ee331b4960b2cf606f2b8cbce6",
                                "a79db61d65454cc7bbf6bde015ba6f5f")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#open songs.json
with open('songs.json','r') as infile:
  songs = json.load(infile)

#analyze each song 
for song in songs:  
  features = spotify.audio_features([song["spotifyID"]])

  print song["song"]
  song["valence"]=features[0]["valence"]
  song ["speechiness"]=features[0]["speechiness"]

  song["sentiment_index"] = ((song["sentiment_score"]*song["sentiment_magnitude"])+song["valence"])/song["speechiness"]

with open('songs.json','w') as outfile:
  json.dump(songs,outfile,sort_keys=True,indent=2)

