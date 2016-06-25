# -*- coding: utf-8 -*-

import MySQLdb as db
import RPi.GPIO as GPIO
import time

HOST = '192.168.43.75'
PORT = 3306
USER = 'gasj'
PASSWORD = '123456'
DB = 'ess'
num_veiculo = 111 #fixo para um mesmo onibus, funciona como primary key 
num_linha = 2 #fixo para uma mesma linha


def insert_db(cont):
    try:
        connection = db.Connection(host=HOST, port=PORT,
                                   user=USER, passwd=PASSWORD, db=DB)

        dbhandler = connection.cursor()
        #sql_st = "INSERT INTO tabela_lot(lot,numveiculo,linha,teste) VALUES(%d,%d,%d,%d)"%(cont,num_veiculo,num_linha,num_veiculo)
        sql_st = "UPDATE tabela_lot SET lot = %d WHERE teste = %d"%(cont,num_veiculo)
        dbhandler.execute(sql_st)
    except Exception as e:
        print e

    finally:
        connection.commit()
        connection.close()

def modulo_cont():
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
        insert_db(t)
        inputValuein = 1
        inputValueout = 1


def main():
    modulo_cont()

if __name__ == '__main__':
    main()
