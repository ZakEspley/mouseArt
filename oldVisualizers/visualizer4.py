from PIL import Image, ImageDraw
import numpy as np
from numpy import  genfromtxt

filename = "data3.log"

data = genfromtxt(filename, delimiter=",")

data = np.delete(data,[0,1,2,5,6], axis=1)

xSize = 3440
ySize = 1440
im = Image.new(mode="RGB", size=(xSize, ySize))
draw = ImageDraw.Draw(im)
event1 = None
rightPoints = 0
leftPoints = 0
for event in data:
    if event1 is None:
        event1 = event
        continue
    event2 = event
    if event1[0] < event2[0]: #went right
        color = (255,0,0)
        rightPoints += 1
    else:
        color = (0,255,0)
        leftPoints += 1
    draw.line([tuple(event1), tuple(event2)], fill=color, width=1)
    size=5
    draw.ellipse([tuple(event2-size), tuple(event2+size)], fill=color, width=2)
    event1 = event
im.save("test.jpg")