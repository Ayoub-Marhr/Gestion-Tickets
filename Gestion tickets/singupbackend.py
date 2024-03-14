from database import Connect
import sys

def singup(ouvrier):
    conn = None
    sql = """INSERT INTO ouvrier (Nom, Password) VALUES (%s, %s)"""
    values = (ouvrier.getNom(), ouvrier.getPassword())
    result = None
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()  
        result = cursor.fetchone()
        cursor.close()
    except Exception as e:
        print('Error:', e)
    finally:
        if conn:
            conn.close()
        return result

