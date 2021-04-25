#========medicine database==========
from sqlite3 import *
import mainquery

c1 = mainquery.cursor()
c=c1[0]
conn=c1[1]

c.execute("CREATE TABLE IF NOT EXISTS medicine_table(name TEXT,date TEXT,phn_no TEXT,medicine TEXT,dosage TEXT,timings TEXT,days TEXT)")
conn.commit()

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
def searchmed(q2):
      global c
      c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record WHERE name LIKE '%"+q2+"%'")
      z=c.fetchall()
      return z
def medlistbox():
      global c
      c.execute("select date,name,phn_no,weight,height,bp,bmi from record ORDER BY date")
      z=c.fetchall()
      return z
      

