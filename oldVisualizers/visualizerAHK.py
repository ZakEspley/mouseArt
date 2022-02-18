from PIL import Image, ImageDraw
import numpy as np
from numpy import  genfromtxt

filename = "data/lotsOfRisk.log"

data = genfromtxt(filename, delimiter=",")

data = np.delete(data,[0,1,2,5,6], axis=1)

xSize = 18440
ySize = 3440
startX = xSize/2
startY = ySize/2
im = Image.new(mode="RGB", size=(xSize, ySize))
draw = ImageDraw.Draw(im)
rightPoints = 0
leftPoints = 0
positionX = startX
positionY = startY
print(f"LENGTH: {len(data)}")
for event in data:
    if event[0] > 0: #went right
        color = (255,0,0)
        rightPoints += 1
    else:
        color = (0,255,0)
        leftPoints += 1
    draw.line([(positionX, positionY), (positionX+event[0], positionY+event[1])], fill=color, width=4)
    # size=5
    # draw.ellipse([tuple(event2-size), tuple(event2+size)], fill=color, width=2)
    positionX+=event[0]
    positionY+=event[1]
im.save("test.jpg")