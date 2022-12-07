import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/light")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.240.202", 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("home/light")
    client.disconnect()