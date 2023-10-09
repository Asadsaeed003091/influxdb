import serial.tools.list_ports
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

ports= serial.tools.list_ports.comports()
serialInst= serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input ("select Port: COM")

for x in range (0,len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar = "COM" + str (val)
        print(portList[x])

serialInst.baudrate = 57600
serialInst.port = portVar
serialInst.open()


client=mqttclient.Client("MQTT")
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker,port=port)
client.loop_start()
while connected!=True:
    time.sleep(0.2)

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n'))
        client.publish("mqtt/testcode",packet)
        client.loop_stop()