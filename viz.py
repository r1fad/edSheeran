from wordcloud import WordCloud, STOPWORDS
from os import path
from PIL import Image
import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt

songs = pd.read_json("edSheeranLyrics.json", encoding='utf-8')

ed = songs['lyrics']

cs = ""
for i in ed:
    cs = cs + " " + i

img = Image.open("ed.png")
img = img.resize((303, 505), Image.ANTIALIAS)
hcmask = np.array(img)

wc = WordCloud(background_color="white", max_words=2000, mask=hcmask, stopwords=STOPWORDS)
wc.generate(cs)
wc.to_file("edwc.png")
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(hcmask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()