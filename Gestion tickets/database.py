import mysql.connector
import sys
def Connect():
    conn=None
    try:
        conn=mysql.connector.Connect(
            host='localhost',
            username='root'
            ,password=''
            ,database='gestion_tickets'
        )
        print('connect')
       
    except:
        print('Error',sys.exc_info)
    finally:
        return conn
Connect()