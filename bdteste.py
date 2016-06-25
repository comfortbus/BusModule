  #Server Connection to MySQL:
#nome do bd ess
#nome das tabelas tabela_lot
#colunas numveiculo e linha
#ip do host 172.22.65.17

import MySQLdb as db
HOST = '192.168.43.75'
PORT = 3306
USER = 'gasj'
PASSWORD = '123456'
DB = 'ess'

try:
    connection = db.Connection(host=HOST, port=PORT,
                               user=USER, passwd=PASSWORD, db=DB)

    dbhandler = connection.cursor()
    dbhandler2 = connection.cursor()
    dbhandler.execute('SELECT * from tabela_lot')
    result = dbhandler.fetchall()
    num = 29
    sql_st = "INSERT INTO tabela_lot(lot,numveiculo,linha,teste) VALUES(%d,%d,%d,%d)"%(188,90,13,num)
    dbhandler2.execute(sql_st)
    
    #dbhandler2.execute("INSERT INTO tabela_lot(lot,numveiculo,linha,teste) VALUES(%s,%s,%s,%s);" %(188,90,13,69))
    #dbhandler2.execute("INSERT INTO tabela_lot VALUES(188,90,13,9);")
    
    for item in result:
        print item

except Exception as e:
    print e

finally:
    connection.commit()
    connection.close()



