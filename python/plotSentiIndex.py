import matplotlib.pyplot as plt
import json
import math

#open songs.json
with open('./JSONs/songs.json','r') as infile:
  songs = json.load(infile)

D={} 

graph = []

# a dictionary where key is the name of song and value is sentiment_index
for song in songs:
  forgraph={}
  D[song["song"]] = math.log(song["sentiment_index"]**2)
  forgraph["name"] = song["song"]
  forgraph["sentiment_index"] = math.log(song["sentiment_index"]**2)
  graph.append(forgraph)
  
plt.bar(range(len(D)), D.values(), align='center')

plt.xticks(range(len(D)), D.keys(),rotation=90)

with open('./JSONs/graph.json','w') as outfile:
  json.dump(graph,outfile,sort_keys=True,indent=2)

plt.show()
