from sqlite3 import *    
import mainquery

c1 = mainquery.cursor()
c=c1[0]
conn=c1[1]

def create():
    global c,conn
    c.execute("CREATE TABLE IF NOT EXISTS credentials(fname TEXT,lname TEXT, contact_no TEXT UNIQUE,email_id TEXT UNIQUE,question TEXT,answer TEXT,password TEXT,confirm_password TEXT)")
    conn.commit()

def call2():
    global c
    p=c.execute("select count(*) from credentials")
    return p

def call1():
    global c
    e1=c.execute("Select email_id from credentials")
    return e1

def call():
    global c
    c.execute("SELECT * FROM credentials")
    r=c.fetchall()
    return r

def ins(*x):
    global c,conn
    c.execute('INSERT INTO credentials VALUES(?,?,?,?,?,?,?,?)',(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
    conn.commit()

def upd():
    global c,conn
    c1.execute("UPDATE credentials SET password=?,confirm_password=? WHERE email_id=?",(pass1.get(),pass1.get(),email1.get()))
    conn.commit()
