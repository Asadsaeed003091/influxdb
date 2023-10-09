import paho.mqtt.client as mqttclient
import time
def on_connect(client,usedata,flags,rc):
    if rc==0:
            print("client is connected")
            global connected
            connected=True
    else:
            print("connection failed")

connected= False

#hostname
broker="localhost"
#port
port=1883
user="asad"
password="asad123"


client=mqttclient.Client("MQTT")
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker,port=port)
client.loop_start()
while connected!=True:
    time.sleep(0.2)
client.publish("mqtt/testcode","hy asad! how are you")
client.loop_stop()
