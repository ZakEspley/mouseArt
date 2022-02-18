from turtle import pos
from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb
import numpy as np
from numpy import  genfromtxt

filename = "data/lotsOfRisk.log"

def rainbow(lastColor):
    delta = 2
    
    red, green, blue = lastColor
    if green > 255-delta:
        if blue > 255-delta:
            green = 0
            blue = 0
        else:
            blue += 10
    else:
        green += 10
    return (red, green, blue)

def rainbowHSV(lastColor):
    delta = 300
    
    hue, saturation, value = lastColor
    
    return (hue+delta, saturation, value)

data = genfromtxt(filename, delimiter=",")




startX = xSize/2
startY = ySize/2
im = Image.new(mode="RGB", size=(xSize, ySize))
draw = ImageDraw.Draw(im)
rightPoints = 0
leftPoints = 0
positionX = startX
positionY = startY
print(f"LENGTH: {len(data)}")

lastX = positions[0,0]
lastY = positions[0,1]
hue = 0
color = getrgb(f"hsl({hue}, 100%, 100%)")
draw.rectangle([0,0,xSize,ySize], fill=(250,250,250))
for i, position in enumerate(positions):
    if i%50==0:
        px, py = position
        draw.line([(lastX, lastY), (px, py)], fill=color, width=5)
        # draw.point((lastX, lastY), fill=color)
        size = 10
        # draw.ellipse([(px-size,py-size),(px+size,py+size)], fill=color, width=1)
        lastX = px
        lastY = py
        if i%200 == 0:
            hue += 1
        color = getrgb(f"hsl({hue}, 100%, 50%)")
        # size=5
        # draw.ellipse([tuple(event2-size), tuple(event2+size)], fill=color, width=2)
        # positionX+=event[0]
        # positionY+=event[1]

circSize = 30

draw.ellipse([(positions[0,0]-circSize, positions[0,1]-circSize), (positions[0,0]+circSize, positions[0,1]+circSize)], fill=(127,60,40), width=2)
draw.ellipse([(positions[-1,0]-circSize, positions[-1,1]-circSize), (positions[-1,0]+circSize, positions[-1,1]+circSize)], fill=(255,153,0), width=2)
print(f"X Values: {minx}, {maxx}, {xSize} ")
print(f"Y Values: {miny}, {maxy}, {ySize} ")

im.save("test.jpg")