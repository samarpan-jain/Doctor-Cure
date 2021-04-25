from sqlite3 import *
import tkinter as tk
import mainquery

c1 = mainquery.cursor()
mycursor=c1[0]
conn=c1[1]

def YogaTableInitialize():
    global mycursor
    mycursor.execute("create table IF NOT EXISTS yoga(patientname text,patientphno int, patientdate date,imagepath text)")
    mycursor.execute("create table IF NOT EXISTS yoga1(patientname1 text,patientphno1 int, patientdate1 date,noofimage text)")

def SelectQuery(p,_entry=None):
    global mycursor
    if(p=="1"):
        mycursor.execute("select * from yoga1 order by patientdate1 desc")
        return(mycursor)
    if(p=="2"):
        w=mycursor.execute("select * from record").fetchall()[-1]
        return(w)
    if(p=="3"):
        mycursor.execute("select * from yoga1 order by patientdate1 desc")
        return(mycursor)
    if(p=="4"):
        mycursor.execute('select * from yoga1 where patientname1 like "%{0}%" order by patientdate1 desc'.format(_entry))
        return(mycursor)
    if(p=="5"):
        mycursor.execute('select * from yoga1 where patientphno1 like "%{0}%" order by patientdate1 desc'.format(_entry))
        return(mycursor)
    if(p=="6"):
        mycursor.execute("select * from yoga1 where patientdate1 like '%{0}%' order by patientdate1 desc".format(_entry))
        return(mycursor)
    
def SelectQuerywithp(a,b,c,p):
    global mycursor
    if(p=="1"):
        z=[]
        mycursor.execute("select * from yoga WHERE patientname=? AND patientphno=? AND patientdate=?",(a,b,c))
        for b in mycursor:
            z.append(b)
        return(z)
    if(p=="2"):
        r=[]
        mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(a,b,c))
        for w in mycursor:
            r.append(w)
        return(r)
    if(p=="3"):
        x=[]
        mycursor.execute("select imagepath from yoga WHERE patientname=? AND patientphno=? AND patientdate=? ",(a,b,c))
        for i in mycursor:
          x.append(i)
        return(x)

def InsertQuerywithp(a,b,c,d,p):
    global mycursor,conn
    if(p=="1"):
        mycursor.execute("INSERT INTO yoga VALUES(?,?,?,?)",(a,b,c,d))
        conn.commit()
    if(p=="2"):
        mycursor.execute("INSERT INTO yoga1 VALUES(?,?,?,?)",(a,b,c,d))
        conn.commit()

def DeleteQuerywithp(a,b,c,d):
    global mycursor,conn
    mycursor.execute("DELETE FROM yoga WHERE patientname=? AND patientphno=? AND patientdate=? ",(a,b,c))
    mycursor.execute("DELETE FROM yoga1 WHERE patientname1=? AND patientphno1=? AND patientdate1=? AND noofimage=?",(a,b,c,d))
    conn.commit()
