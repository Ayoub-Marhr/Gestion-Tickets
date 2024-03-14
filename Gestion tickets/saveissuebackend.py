from database import Connect
import sys

def save(issue):
    conn = None
    sql = """INSERT INTO tickets (Nom, category,problem,description) VALUES (%s, %s,%s,%s)"""
    values = (issue.getNom(), issue.getPassword())
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