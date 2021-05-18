import paho.mqtt.client as mqtt
import autenticacao as aut
import sys
import time
import random


TOPICO = f"channels/{aut.channel}/publish/{aut.API_Key }"
client = mqtt.Client()
client.connect('mqtt.thingspeak.com', 1883, 60)

try:

    while True:
        sensor = random.randint(1, 21)
        payload = "field1=" + str(sensor) 
        payload =  payload.encode('utf-8')
        payload = payload.decode()
        client.publish(TOPICO, payload, qos=0)
        print (f"Sensor {sensor}")
        time.sleep(25)
  
except KeyboardInterrupt:
    print("\nCtrl+C para sair")
    client.disconnect()
    sys.exit(0)