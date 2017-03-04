import matplotlib.pyplot as plt
import json
import math

#open songs.json
with open('songs.json','r') as infile:
  songs = json.load(infile)

D={}

# a dictionary where key is the name of song and value is sentiment_index
for song in songs:
  D[song["song"]] = song["sentiment_index"]

plt.bar(range(len(D)), D.values(), align='center')

plt.xticks(range(len(D)), D.keys(),rotation=90)

plt.show()
