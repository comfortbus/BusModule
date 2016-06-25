# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

#pinHallin = 7 # pino do sensor Hall entrada (número GPIO)
#pinHallout =  # pino do sensor Hall saída
inputValuein = 1 # valor lido
inputValueout = 1
i = 0; # contador entrada
o = 0; # contador saída
t = 0; # contador total 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(29, GPIO.IN)

while (1):
    while (inputValuein and inputValueout) == 1:
        inputValuein = GPIO.input(7)
        inputValueout = GPIO.input(29)
        #print("Contagem de Entrada:")

    if inputValuein == 0:
        i = i + 1
        print("Contagem de Entrada:")
        print(i)
        time.sleep(0.3)

    if inputValueout == 0:
        o = o + 1
        print("Contagem de Saida:")
        print(o)
        time.sleep(0.3)
        
    t = i - o
    print(t)
    inputValuein = 1
    inputValueout = 1
