
def controller():
    import evdev
    from evdev import InputDevice, categorize, ecodes

    #creates object 'gamepad' to store the data
    #you can call it whatever you like
    #To see the list of events
    #Connect controller
    #Run: python -m evdev.evtest
    #Look to see what event number the controller is
    #Mine reads '.../input/event7/  Sony Entertainment Wireless Controller...'
    #Type '0' and hit enter. You should see tons of data relating to button presses

    #The event number should be typed in below., again, mine was event7
    gamepad = InputDevice('/dev/input/event7')

    #Here are some user defined buttons | These were found manually
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
    #print(gamepad)

    #loop and filter by event code and print the mapped label
    for event in gamepad.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 1:
                if event.code == xBtn:
                    return "X"
                elif event.code == oBtn:
                    return("O")
                elif event.code == sqBtn:
                    return("Square")
                elif event.code == triBtn:
                    return("Triangle")
                elif event.code == 314:
                    return("Share")
                elif event.code == 315:
                    return("Options")
                elif event.code == rTrT:
                    return("Right Top BTN ")
                elif event.code == rTrB:
                    return("Right Bottom BTN ")
                elif event.code == lTrT:
                    return("Left Top BTN ")
                elif event.code == lTrB:
                    return("Left Bottom BTN ")
                elif event.code == 316:
                    return("PS BTN")
                
        if event.type == evdev.ecodes.EV_ABS:
            if event.value < 110:
                if event.code == lAlgUD:
                    return('Left Analog Up ')#+str(event.value))
                elif event.code == lAlgLR:
                    return("Left Analog Left ")#+str(event.value))
                elif event.code == rAlgUD:
                    return("Right Analog Up ")#+str(event.value))
                elif event.code == rAlgLR:
                    return("Right Analog Left ")#+str(event.value))
            if event.value > 146:
                if event.code == lAlgUD:
                    return("Left Analog Down ")#+ str(event.value))
                elif event.code == lAlgLR:
                    return("Left Analog Right ")#+str(event.value))
                elif event.code == rAlgUD:
                    return("Right Analog Down ")#+str(event.value))
                elif event.code == rAlgLR:
                    return("Right Analog Right ")#+str(event.value))
