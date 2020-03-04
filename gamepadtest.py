import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event7')

xBtn = 304
oBtn = 305
sqBtn = 308
triBtn = 307

lTrB = 312
lTrT = 310
rTrB = 313
rTrT = 311

lAlgLR = ecodes.ABS_X
lAlgUD = ecodes.ABS_Y
rAlgLR = ecodes.ABS_RX
rAlgUD = ecodes.ABS_RY

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.value == 1:
            if event.code == xBtn:
                print("X")
            elif event.code == oBtn:
                print("O")
            elif event.code == sqBtn:
                print("Square")
            elif event.code == triBtn:
                print("Triangle")
            elif event.code == 314:
                print("Share")
            elif event.code == 315:
                print("Options")
            elif event.code == rTrT:
                print("Right Top BTN ")
            elif event.code == rTrB:
                print("Right Bottom BTN ")
            elif event.code == lTrT:
                print("Left Top BTN ")
            elif event.code == lTrB:
                print("Left Bottom BTN ")
            elif event.code == 316:
                print("PS BTN")
                
    if event.type == evdev.ecodes.EV_ABS:
        if event.value < 110:
            if event.code == lAlgUD:
                print('Left Analog Up '+str(event.value))
            elif event.code == lAlgLR:
                print("Left Analog Left "+str(event.value))
            elif event.code == rAlgUD:
                print("Right Analog Up "+str(event.value))
            elif event.code == rAlgLR:
                print("Right Analog Left "+str(event.value))
        if event.value > 146:
            if event.code == lAlgUD:
                print("Left Analog Down "+ str(event.value))
            elif event.code == lAlgLR:
                print("Left Analog Right "+str(event.value))
            elif event.code == rAlgUD:
                print("Right Analog Down "+str(event.value))
            elif event.code == rAlgLR:
                print("Right Analog Right "+str(event.value))
