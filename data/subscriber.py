import paho.mqtt.client as mqttclient
import time
def on_connect(client,usedata,flags,rc):
    if rc==0:
            print("client is connected")
            global connected
            connected=True
    else:
            print("connection failed")

def on_message(clent,userdata,message):
    print("Message recieved" + str(message.payload.decode("utf-8")))
    print("topic"+str(message.topic))

connected= False
Messagerecieved= False

#hostname
broker="localhost"
#port
port=1883
user="asad"
password="asad123"


client= mqttclient.Client("MQTT")
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker,port=port)

client.subscribe("mqtt/testcode")

while connected!=True:
    time.sleep(0.2)
while Messagerecieved!=True:
    time.sleep(0.20)
client.loop_stop()