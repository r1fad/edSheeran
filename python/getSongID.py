import spotipy
import json 

#create spotify object
spotify = spotipy.Spotify()

#open songs.json
with open('../JSONs/songs.json','r') as infile:
  songs = json.load(infile)

for song in songs:
  name = song["song"]+ " Ed Sheeran"
  
  results = spotify.search(q=name,limit=1)
  
  dumpID = results["tracks"]["items"][0]["id"]
  dumpArtist = results["tracks"]["items"][0]["artists"][0]["name"]

  song["spotifyID"] = dumpID

  print song["song"]
  print dumpArtist
  print dumpID
  


with open('../JSONs/songs.json','w') as outfile:
  json.dump(songs,outfile,sort_keys=True,indent=2)


 