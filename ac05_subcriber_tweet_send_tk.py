#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys
import tweepy
import autenticacao as aut
from datetime import datetime

# Autenticação Tweepy

auth = tweepy.OAuthHandler(aut.API_key, aut.API_key_secret)
auth.set_access_token(aut.access_token, aut.access_token_secret)


#Callback - conexão ao broker
def conectou(client, userdata, flags, rc):
    if rc==0:
        print('Conectado ao broker')
    else:
        print(f'Não conectado, falha na conexão !!! Erro = {rc}')
    client.subscribe(TOPICO) #assina o tópico

#Callback - mensagem recebida do broker
def chegou_mensagem(client, userdata, msg):
    dado=msg.payload.decode()
    # {msg.topic} para printar url
    print(f"{dado}") 
    api = tweepy.API(auth)
    date_time = datetime.now()

    #Envia o tweet
    tweet = f'Alarme da região {dado} acionado na data: {date_time.strftime("%d/%m/%Y %H:%M:%S")}'
    api.update_status(tweet)
    print('Enviado com sucesso')

#Programa Principal

# Read_API_Key = 'R5AA6J9LNPLP0812'

TOPICO = f"channels/{aut.channel}/subscribe/fields/field1/" #{Read_API_Key}
broker = 'mqtt.thingspeak.com'

try:
    
    client=mqtt.Client() #Gera um ID de cliente
    client.on_connect=conectou # link para callback - mensagem
    client.on_message=chegou_mensagem # link para callback - mensagem
    client.username_pw_set('mychannel', aut.MQTT_API_Key)
    client.connect(broker, 1883) # Realiza conexão com o broker
    client.loop_forever() # Monitora e encaminha os callbakcs
            
except KeyboardInterrupt:
    print("\n Crtl+C pressionado, encerrando aplicação e saindo...") # Sair do programa 
    sys.exit(0)

except tweepy.TweepError as e:
    print(e.reason)