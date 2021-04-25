#history Query
from PIL import ImageTk,Image
from sqlite3 import *
import mainquery

c1 = mainquery.cursor()
c=c1[0]
conn=c1[1]

c.execute("CREATE TABLE IF NOT EXISTS record(name TEXT,weight real,height TEXT,date TEXT,phn_no INT,bp TEXT,ong_disease TEXT,add_disease TEXT,precaution TEXT,bmi TEXT,age INT)")
conn.commit()



def save(*r):
      global c,conn
      if(len(r)==1):
            c.execute("SELECT * FROM record")
            L=c.fetchall()
            return L
      elif(len(r)==11):
            c.execute('INSERT INTO record(name,weight,height,date,phn_no,bp,ong_disease,add_disease,precaution,bmi,age) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10]))
            conn.commit()
      elif(len(r)==7):
            c.execute("UPDATE record SET ong_disease=?,add_disease=?,precaution=?,bp=? WHERE name=? and date=? and phn_no=?",(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
            conn.commit()
def listboxclear():
      global c
      c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record order by date")
      z=c.fetchall()
      return z
def listboxsearch(q2):
      global c
      c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record WHERE name LIKE '%"+q2+"%'")
      z=c.fetchall()
      return z
def delrecord(d1,d2,d3):
      global c,conn
      c.execute("DELETE FROM record WHERE date=? and name=? and phn_no=?",(d1,d2,d3))
      conn.commit()
      
#========medicine database==========

def addmedicine(*r):
      global c,conn
      c.execute('INSERT INTO medicine_table(name,date,phn_no,medicine,dosage,timings,days) VALUES(?,?,?,?,?,?,?)',(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
      conn.commit()
      
def delmedicine(*r):
      global c,conn
      c.execute("DELETE FROM medicine_table WHERE date=? and name=? and phn_no=? and medicine=? and dosage=? and timings=? and days=?",(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
      conn.commit()
def viewmedicine(*r):
      global c
      z=c.execute("select medicine,dosage,timings,days from medicine_table where name=? and date=? and phn_no=?",(r[0],r[1],r[2]))
      return z
def listboxadd(*r):
      global c
      z=c.execute("select medicine,dosage,timings,days from medicine_table where medicine=? and dosage=? and timings=? and days=?",(r[0],r[1],r[2],r[3]))
      return z
def medclear():
      global c
      c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record ")
      z=c.fetchall()
      return z
def searchmed():
      global c
      c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record WHERE name LIKE '%"+q2+"%'")
      z=c.fetchall()
      return z
def medlistbox():
      global c
      c.execute("select date,name,phn_no,weight,height,bp,bmi from record ORDER BY date")
      z=c.fetchall()
      return z

def Himage(screen):
      screen.bg=ImageTk.PhotoImage(file="images/l1.jpg")
      return(screen.bg)
