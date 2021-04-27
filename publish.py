#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys
from time import sleep

TOPICO = 'test_queue/outTopic'
client = mqtt.Client()
client.connect('broker.mqtt-dashboard.com', 1883, 60)

try:
    while True:
        mensagem = ""
        for i in range(0,11):
            mensagem = str(i)
            payload = mensagem.encode('utf-8')
            client.publish(TOPICO, payload, qos=0)
            payload = payload.decode()
            print(f'Mensagem: {TOPICO} {payload}')
            sleep(5)
        mensagem = "Fim do For"            
        payload = mensagem.encode('utf-8')
        client.publish(TOPICO, payload, qos=0)
        payload = payload.decode()
        print(f'Mensagem: {TOPICO} {payload}')
        sleep(5)
        

except KeyboardInterrupt:
    print("\n Crtl+C pressionado, encerrando aplicação e saindo...") # Sair do programa 
    sys.exit(0)



