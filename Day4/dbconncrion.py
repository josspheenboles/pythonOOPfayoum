import psycopg2
import sys
#global var represntaion connection configuration
host='localhost'
user='iti'
password='123'
dbname='fayoumdemo'
#connect()
def connect():
    try:
        connection=psycopg2.connect(host=host,password=password,user=user,dbname)
        return connecting
    except:
        print('connection valid')
def createtable(query):
    conn=connect()        
    try:
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
    except:
        print('exception')
def selectfromtable(tablename):
    conn=connect()    
    query=f'select * from {tablename};'
    try:
        cur=conn.cursor()
        cur.execute(query)
        traineedata=cur.fetchall()
        return traineedata
    except:
        print('exception')

#insert()
def inserttrainee(id,name,track):
    conn=connect()    
    query=f'insert into traineedata values({id},{name},{track});'
    try:
        cur=conn.cursor()
        cur.execute(query)
        traineeid=cur.fetchone()[0]
        conn.commit()
    except:
        print('exception')
#select 
def selectalltrainee():
    conn=connect()    
    query=f'select * from traineedata;'
    try:
        cur=conn.cursor()
        cur.execute(query)
        traineedata=cur.fetchall()
        return traineedata
    except:
        print('exception')
#update
def updatetrainee(id,name,track):
    conn=connect()    
    query=f'update traineedata set name={name},track={track};'
    try:
        cur=conn.cursor()
        cur.execute(query)
        updatetraineeid=cur.fetchone()[0]
        conn.commit()
    except:
        print('exception')

