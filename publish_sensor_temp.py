#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys
from iot_temperatura_cpu import temperatura, cpu
from time import sleep

TOPICO = 'temp_cpu/outTopic'
client = mqtt.Client()
client.connect('broker.mqtt-dashboard.com', 1883, 60)

try:
    while True:
        uso_cpu = cpu()
        temp = "100°"
        mensagem = '\nUso da CPU: {} %'.format(uso_cpu)            
        payload = mensagem.encode('utf-8')
        client.publish(TOPICO, payload, qos=0)
        payload = payload.decode()
        print(f'Mensagem: {TOPICO} {payload}')
        sleep(5)
        

except KeyboardInterrupt:
    print("\n Crtl+C pressionado, encerrando aplicação e saindo...") # Sair do programa 
    sys.exit(0)



