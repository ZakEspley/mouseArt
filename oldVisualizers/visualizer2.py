import json
from PIL import Image, ImageDraw
import numpy as np

filename = "data.json"

with open(filename) as fb:
    data = json.load(fb)


xSize = 3440
ySize = 1440
xScreen = 3440
yScreen = 1440

screenPositionX = int((xSize-xScreen)/2)
screenPositionY = int((ySize-yScreen)/2)

shiftX =100
shiftY =100
centerX = xScreen/2+shiftX
centerY = yScreen/2+shiftY
# centerX = 1717
# centerY =719
center = np.array([centerX, centerY])
radius = 6



offset = [0,0]
previousPoint = None
maxMovement = .01*xScreen

def magnitude(point1, point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

moveEvents = np.array(data["moves"])
print(f"MOVEVENTS: {moveEvents.shape}")
moveEvents = np.delete(moveEvents, 2, axis=1)
print(f"MOVEVENTS: {moveEvents.shape}")
print(f"TOTAL POINTS: {len(moveEvents)}")
print(center)

changedMoves = np.empty((0,2))
offsetUpdatedCounter = 0
for event in moveEvents:
    event = np.array([event[0], event[1]])
    if previousPoint is None:
        previousPoint = event
        continue
    if magnitude(center, event+offset) < radius:
        # print(f"OFFSET INFO {event}, {previousPoint}, {offset}")
        offsetUpdatedCounter += 1
        offset = np.array([-event[0]-offset[0] + previousPoint[0], -event[1]-offset[1] + previousPoint[1]])
        # offset = previousPoint
        continue
    # if magnitude(previousPoint, event+offset) > maxMovement:
    #     # print(f"OFFSET INFO {event}, {previousPoint}, {offset}")
    #     offsetUpdatedCounter += 1
    #     offset = np.array([-event[0]-offset[0] + previousPoint[0], -event[1]-offset[1] + previousPoint[1]])
    #     continue
    
    # print(event)
    event = event + offset
    previousPoint = event
    # print(event)
    changedMoves = np.append(changedMoves, [event], axis=0)
    
    
# moveEvents += np.array([[screenPositionX, screenPositionY]])
# moveEvents = moveEvents.flatten()
# events = moveEvents.tolist()
changedMoves = changedMoves + np.array([[screenPositionX, screenPositionY]])
# changedMoves = changedMoves.flatten()
# changedMoves = changedMoves/5000
# events = changedMoves.tolist()
# print(events)
im = Image.new(mode="RGB", size=(xSize, ySize))
draw = ImageDraw.Draw(im)
event1 = None
rightPoints = 0
leftPoints = 0
for event in changedMoves:
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
# draw.line(events, fill=(0,255,0), width=1)
draw.ellipse([centerX-radius, centerY-radius, centerX+radius, centerY+radius], outline=(255,0,0), width=1)
draw.ellipse([centerX-radius-shiftX, centerY-radius-shiftY, centerX+radius-shiftX, centerY+radius-shiftY], outline=(255,255,255), width=1)
# draw.point(events, fill=(0,255,0))
im.save("test.jpg")
print(f"POINT REJECTED: {offsetUpdatedCounter}")
print(f"FINAL OFFSET: {offset}")
print(f"RIGHTLINES: {rightPoints}")
print(f"LEFTLINES: {leftPoints}")