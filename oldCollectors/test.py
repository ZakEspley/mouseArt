from rawinputdata import RawInputReader
import numpy as np
import json
global mouseEvents
moveEvents = np.empty(shape=(0,3))
global run
run = False

def mouse_callback( event ):
    # if event.action == winput.WM_LBUTTONDOWN:
    #     print("Left mouse button press at {}".format( event.position ))
    # print(event)
    global moveEvents
    if event.additional_data != []:
        moveEvents = np.append(moveEvents, np.array([[event.position[0], event.position[1],  event.time]]), axis=0)
    
def keyboard_callback( event ):
    global run
    # print(event.action)
    # print(run)
    if event.vkCode == winput.VK_F1 and event.action == winput.WM_KEYUP:
        # print("Inside")
        if not run:
            print("Starting Recording")
            print("Press F1 to end recording")
            winput.hook_mouse( mouse_callback )
            run = True
        else:
            print("Recording Stopped")
            winput.stop()
        
print("Press F1 to start recording.")
    
rir = RawInputReader(None)
rir.start()


# data = {"moves": moveEvents.tolist()}

# with open("data.json", "w") as fb:
#     json.dump(data, fb)