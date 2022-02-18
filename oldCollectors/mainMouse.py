from tarfile import RECORDSIZE
from turtle import screensize
from pynput.keyboard import Listener as KeyboardListener
import mouse
from pynput.keyboard import Key
from PIL import Image, ImageDraw
import numpy as np
import time
import json

moveEvents = np.empty(shape=(0,3))
clickEvents = np.empty(shape=(0,5))
scrollEvents = np.empty(shape=(0,5))
filterEvents = np.empty(shape=(0,6))
global run
run = True
global record
record = False

global timeGap
timeGap = 0.1

global lastTime
lastTime=0


def release(key):
    # print(key)
    global record
    global run
    if key == Key.f1:
        if not record:
            # mouseListener.start()
            record = True
            print("Recording Started")
        else:
            # mouseListener.stop()
            keyboardListener.stop()
            record = False
            run = False
            mouse.click(mouse.RIGHT)
            print("Recording Stopped")

def moveList(*args):
    global moveEvents
    # print(events.shape)
    # print(np.array([[args[0], args[1]]]).shape)
    # if time.monotonic() - lastTime >= timeGap:
        # events = np.append(events, np.array([[args[0], args[1]]]), axis=0)
    args = list(args)
    args.append(time.monotonic())
    moveEvents = np.append(moveEvents, np.array([args]), axis=0)

def clickList(*args):
    global clickEvents
    args = list(args)
    args.append(time.monotonic())
    clickEvents = np.append(clickEvents, np.array([args]), axis=0)
def scrollList(*args):
    global scrollEvents
    args = list(args)
    args.append(time.monotonic())
    scrollEvents = np.append(scrollEvents, np.array([args]), axis=0)

def filterList(*args):
    global filterEvents
    global lastTime
    # args = [str(arg) for arg in args]
    info = [args[0]]
    info += [str(args[1].dwExtraInfo), str(args[1].flags), str(args[1].mouseData), str(args[1].pt), str(args[1].time)]
    # args.append(time.monotonic())
    filterEvents = np.append(filterEvents, np.array([info]), axis=0)
    if lastTime == int(args[1].time):
        print("REJECTED")
        return False
    lastTime = int(args[1].time)
    return True

# mouseListener = MouseListener(on_move=moveList, on_click=clickList, on_scroll=scrollList, win32_event_filter=filterList)
keyboardListener =  KeyboardListener(on_release=release)

keyboardListener.start()
# mouseListener.start()


while run:
    if record:
        events = mouse.record()
xSize = 3440
ySize = 1440
xScreen = 3440
yScreen = 1440

# screenPositionX = int((xSize-xScreen)/2)
# screenPositionY = int((ySize-yScreen)/2)
# events += np.array([[screenPositionX, screenPositionY]])
# events = events.flatten()
# events = list(events)
# # print(events)
# im = Image.new(mode="RGB", size=(xSize, ySize))
# draw = ImageDraw.Draw(im)
# # draw.line(events, fill=(0,255,0), width=10)
# draw.point(events, fill=(0,255,0))
# im.save("test.jpg")
# for click in clickEvents:
    # click[2] = str(click[2])

moves = []
for event in events:
    if isinstance(event, mouse.ButtonEvent):
        continue
    moves.append([event.x, event.y, event.time])
data = {"moves": moves}

with open("data.json", "w") as fb:
    json.dump(data, fb)
