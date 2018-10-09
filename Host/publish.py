# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

print("please enter msg:")
msg = raw_input()
publish.single("mqtt/test", msg, hostname="test.mosquitto.org")
publish.single("mqtt/topic", "World!", hostname="test.mosquitto.org")
print("Done")
 
