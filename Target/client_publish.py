# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys, os
import base64

s=" " 

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mqtt/test")
    client.subscribe("mqtt/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "capture":
        print("Received message #1, do something")
	os.system("fswebcam -r 640x480 --jpeg 85 -D 1 webcamshot.jpg")
	with open("webcamshot.jpg", "rb") as imageFile:
		s=base64.encodestring(imageFile.read())
		print(s)

	#import mqtt_publish_demo
	publish.single("mqtt/new", s, hostname="test.mosquitto.org")

	print("Done")

 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
