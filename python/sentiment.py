# Imports the Google Cloud client library
from google.cloud import language
import json
import unicodedata


# Instantiates a client
language_client = language.Client()

#open songs.json
with open('../JSONs/songs.json','r') as infile:
  songs = json.load(infile)

# The text to analyze
for song in songs:
  text = song['lyrics']
  text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
  document = language_client.document_from_text(text)

  # Detects the sentiment of the text
  sentiment = document.analyze_sentiment().sentiment

  song['sentiment_score'] = sentiment.score 
  song['sentiment_magnitude'] = sentiment.magnitude

  print song['song']
  print song['sentiment_score']

with open('../JSONs/songs.json','w') as outfile:
  json.dump(songs,outfile,sort_keys=True,indent=2)
