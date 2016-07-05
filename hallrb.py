# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import json
import urllib2


def insert_db(cont):
    # Utilizando como base ônibus 12419 (T.I CAMARAGIBE - CENTRO)
    data = {}
    data['secret_key'] = 'lE9lIS7dYaKuYpEYC27wrEDtgjHpD9sx'
    data['lotacao'] = cont
    json_data = json.dumps(data)

    url = "http://comfortbus.herokuapp.com/api/veiculo/12419/update/"
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application-json')
    response = urllib2.urlopen(req, json_data)
    print(response)


def modulo_cont():
    inputValuein = 1  # valor lido
    inputValueout = 1
    i = 0  # contador entrada
    o = 0  # contador saída
    t = 0  # contador total

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)
    GPIO.setup(29, GPIO.IN)

    while (1):
        while (inputValuein and inputValueout) == 1:
            inputValuein = GPIO.input(7)
            inputValueout = GPIO.input(29)
            # print("Contagem de Entrada:")

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
        insert_db(t)
        inputValuein = 1
        inputValueout = 1


def main():
    modulo_cont()

if __name__ == '__main__':
    main()
