from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
Image.MAX_IMAGE_PIXELS=10000000000
fontpath = 'font.ttf'
f = open(r'text.txt', 'r', encoding='utf-8').read()


wordcloud=WordCloud(font_path=fontpath,background_color="white",width=1800,height=2400,margin=2,scale=2,repeat=True,prefer_horizontal=1.0).generate(f)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('a.png')