#Welcome to my code

#Begin by importing dependencies
#sys is for exiting the code 'cleanly'
#paho is the mqtt subscription dependency
#time is for a delay function
import sys
import paho.mqtt.subscribe as subscribe
from time import sleep

#Set a dummy constant for looping
rc = 0

#User Defined MQTT Value.
url='tailor.cloudmqtt.com'
portnumber = 10608
username = 'gujunebq'
password = '7jKRFQxKHQcO'
topic = 'laptop'

#Enter a forever loop
while rc == 0:
	#Perform this loop, unless user input a keyboard interrupt
	try:
		#subscribe.simple is a function that initiates a subscription to the MQTT server
		msg = subscribe.simple(topic, hostname=url, port=portnumber, auth={'username':username,'password':password})
		#Print the message on screen
		print("%s %s" % (msg.topic, msg.payload))
		#Delay for a second
		sleep(1)
	#Perform this when a keyboard interrupt is input
	except KeyboardInterrupt:
		#Shift down to a new line
		print('\n')
		#Exit the program
		sys.exit(0)
