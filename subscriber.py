#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys

#Callback - conexão ao broker

def conectou(client, userdata, flags, rc):
    if rc==0:
        print('Conectado ao broker')
    else:
        print(f'Não conectado, falha na conexão !!! Erro = {rc}')
    client.subscribe('test_queue/inTopic') #assina o tópico

#Callback - mensagem recebida do broker
def chegoou_mensagem(client, userdata, msg):
    dado=msg.payload
    dado = dado.decode()
    dados = str(dado)
    print(f"{msg.topic} {dado}") 

#Programa Principal
try:
    client=mqtt.Client() #Gera um ID de cliente
    client.on_connect=conectou # link para callback - mensagem
    client.on_message=chegoou_mensagem # link para callback - mensagem
    client.connect('broker.mqtt-dashboard.com', 1883, 60) # Realiza conexão com o broker
    client.loop_forever() # Monitora e encaminha os callbakcs
except KeyboardInterrupt:
    print("\n Crtl+C pressionado, encerrando aplicação e saindo...") # Sair do programa 
    sys.exit(0)