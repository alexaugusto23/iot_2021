#!/usr/bin/env python3

import time
import subprocess
import psutil

def temperatura():
    #Obtém informação da frequ~encia do processador
    url = "$cat /sys/class/thermal/thermal_zone0/temp"
    temp = subprocess.check_output(url, shell=True)
    temp = float(temp) / 1000
    return temp

def cpu():
    #Obtém informação da frequ~encia do processador
    uso_cpu = psutil.cpu_percent()
    return uso_cpu

string = '=' * 30 
temp = temperatura()
uso = cpu()

while True:
    print('\nOlá seja bem vindo ao monitor de temperatura\n')
    print()
    print('Temperatura do processaro: {} °C\nUso da CPU: {} %'.format(temp, uso))
    print(string)
    time.sleep(3)