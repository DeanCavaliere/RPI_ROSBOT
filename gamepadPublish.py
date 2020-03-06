import gamepadtest as game
import paho.mqtt.client as paho
from time import sleep
topic = "controller"
rc = 0

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + accelerometer_data)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = paho.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#url_str = os.environ.get('CLOUDMQTT_URL', 'm12.cloudmqtt.com:19757')
#url = urlparse.urlparse(url_str)
url='tailor.cloudmqtt.com:10608'

# Connect
mqttc.username_pw_set( "gujunebq", "7jKRFQxKHQcO")
#mqttc.username_pw_set(url.username, url.password)
mqttc.connect("tailor.cloudmqtt.com", 10608)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "Connected")

# Continue the network loop, exit when an error occurs
while rc == 0:
        rc = mqttc.loop()
        controllerData = game.controller()
        mqttc.publish(topic, str(controllerData))
        sleep(0.5)
print("rc: " + str(rc))

