import evdev
from evdev import InputDevice, categorize, ecodes
import sys
import paho.mqtt.client as paho
from time import sleep

# creates object 'gamepad' to store the data
# you can call it whatever you like
# To see the list of events
# Connect controller
# Run: python -m evdev.evtest
# Look to see what event number the controller is
# Mine reads '.../input/event7/  Sony Entertainment Wireless Controller...'
# Type '0' and hit enter. You should see tons of data relating to button presses

# The event number should be typed in below., again, mine was event7
gamepad = InputDevice('/dev/input/event7')

# Here are some user defined buttons | These were found manually
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

#MQTT Globals
topic = "controller"

url='tailor.cloudmqtt.com:10608'

mqttc = paho.Client()
# Connect
mqttc.username_pw_set( "gujunebq", "7jKRFQxKHQcO")
#mqttc.username_pw_set(url.username, url.password)
mqttc.connect("tailor.cloudmqtt.com", 10608)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "Connected")


def mqttPublish(data):
    mqttc.publish(topic, str(data))

# prints out device info at start
print(gamepad)

# loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.value == 1:
            if event.code == xBtn:
                data =  "X"
                mqttPublish(data)
            elif event.code == oBtn:
                data = ("O")
                mqttPublish(data)
            elif event.code == sqBtn:
                data = ("Square")
                mqttPublish(data)
            elif event.code == triBtn:
                data = ("Triangle")
                mqttPublish(data)
            elif event.code == 314:
                data = ("Share")
                mqttPublish(data)
            elif event.code == 315:
                data = ("Options")
                mqttPublish(data)
            elif event.code == rTrT:
                data = ("Right Top BTN")
                mqttPublish(data)
            elif event.code == rTrB:
                data = ("Accel On")
                mqttPublish(data)
            elif event.code == lTrT:
                data = ("Left Top BTN")
                mqttPublish(data)
            elif event.code == lTrB:
                data = ("Left Bottom BTN")
                mqttPublish(data)
            elif event.code == 316:
                data = ("PS BTN")
                mqttPublish(data)
        if event.value == 0:
            if event.code == rTrB:
                data = ("Accel Off")
                mqttPublish(data)

    if event.type == evdev.ecodes.EV_ABS:
        if event.value < 10:
            if event.code == lAlgUD:
                data = ('Left Analog Up')  # +str(event.value))
                mqttPublish(data)
            elif event.code == lAlgLR:
                data = ("Left Analog Left")  # +str(event.value))
                mqttPublish(data)
            elif event.code == rAlgUD:
                data = ("Right Analog Up")  # +str(event.value))
                mqttPublish(data)
            elif event.code == rAlgLR:
                data = ("Right Analog Left")  # +str(event.value))
                mqttPublish(data)
        if event.value > 245:
            if event.code == lAlgUD:
                data = ("Left Analog Down")  # + str(event.value))
                mqttPublish(data)
            elif event.code == lAlgLR:
                data = ("Left Analog Right")  # +str(event.value))
                mqttPublish(data)
            elif event.code == rAlgUD:
                data = ("Right Analog Down")  # +str(event.value))
                mqttPublish(data)
            elif event.code == rAlgLR:
                data = ("Right Analog Right")  # +str(event.value))
                mqttPublish(data)
