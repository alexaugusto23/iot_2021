import paho.mqtt.client as mqtt
import psutil
import time

TOPICO = "channels/1386377/publish/4NUBQSUB8GYU00AX"
client = mqtt.Client()
client.connect('mqtt.thingspeak.com', 1883, 60)

try:

    while True:

        cpuPercent = psutil.cpu_percent(interval=1)
        ramPercent = psutil.virtual_memory().percent
        payload = "field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)
        payload =  payload.encode('utf-8')
        payload = payload.decode()
        client.publish(TOPICO, payload, qos=0)
        print (" Published CPU = ",cpuPercent," RAM = ", ramPercent)
        time.sleep(15)
  

except KeyboardInterrupt:
    print("Houve um erro ao publicar")