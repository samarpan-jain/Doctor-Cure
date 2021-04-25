from sqlite3 import *    

conn = connect('my_database.db')

def cursor():
    global conn
    c = conn.cursor()
    return [c,conn]
