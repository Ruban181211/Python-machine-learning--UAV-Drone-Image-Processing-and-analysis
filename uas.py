import os
from PIL import Image

im = Image.open("odm_orthophoto.tif")
pix = im.load()

r, g, b = 0,0,0
for x in range(im.size[0]):
    for y in range(im.size[1]):
        r = r+pix[x,y][0]
        g = g+pix[x,y][1]
        b = b+pix[x,y][2]

print(r/(im.size[0]*im.size[1]))
print(g/(im.size[0]*im.size[1]))
print(b/(im.size[0]*im.size[1]))
