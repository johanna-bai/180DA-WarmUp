# When run at the same time as mqtt_ping_1.py, the two programs ping-pong each other 
# a counter that increments each time they receive a message 
# mqtt_ping_2.py sets off this chain and sends the initial message
import paho.mqtt.client as mqtt
import time
import numpy as np

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("ece180d/test/johanna/#", qos=1)
    client.publish("ece180d/test/johanna/3", 0, qos=1)

# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
# client.subscribe("ece180d/test")
# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')


def on_message(client, userdata, message):
    time.sleep(1)
    topic = int(message.topic.split('/')[-1])
    if topic != 3:
        print('Received message: "' + str(message.payload) + '" on topic "' + message.topic + '" with QoS ' + str(message.qos))
        #if (message.payload).isnumeric:  
        num = int((message.payload)) + 1
        client.publish("ece180d/test/johanna/3", num , qos=1)
        print("sent message: " + str(num))

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
#client.publish("ece180d/test/team6", "hi this is johanna", qos=1)

# 4. use subscribe() to subscribe to a topic and receive messages.
while True: 
    pass


# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.

# 6. use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()