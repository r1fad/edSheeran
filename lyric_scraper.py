import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import json 
import unicodedata
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
openurl = MyOpener().open

url = "https://www.directlyrics.com/ed-sheeran-artist.html"
base = "https://www.directlyrics.com"

soup = BeautifulSoup(openurl(url).read(),'html.parser')

listOfLyrics = soup.find('ul',attrs={'class':'scrolled'})

lyricsList = []

for details in listOfLyrics.find_all('a',href=True):

  lyricsInfo = {}
  lyricURL = base + details['href']

  lyricSoup = BeautifulSoup(openurl(lyricURL).read(),'html.parser',
       parse_only=SoupStrainer('div',{'class':'lyrics lyricsselect'}))

  dodgyLyrics = lyricSoup.text.strip().split('\n')

  for i in dodgyLyrics:
    if '{' in i:
      dodgyLyrics.remove(i)

  properLyrics = '\n'.join(dodgyLyrics)

  lyricsInfo['url'] = lyricURL
  lyricsInfo['lyrics'] = properLyrics

  lyricsList.append(lyricsInfo)
  
  
with open('edSheeranLyrics.json', 'w') as outfile:
  json.dump(lyricsList,outfile,sort_keys = True, indent = 4)
