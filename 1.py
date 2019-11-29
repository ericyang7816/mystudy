from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
Image.MAX_IMAGE_PIXELS=10000000000
fontpath = 'font.ttf'
f = open(r'text.txt', 'r', encoding='utf-8').read()
aimask=np.array(Image.open('1.png'))
color=ImageColorGenerator(aimask)

wordcloud=WordCloud(font_path=fontpath,background_color="white",mask=aimask,color_func=color,width=800,height=600,margin=2,repeat=True,mode="RGBA").generate(f)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('a.png')
