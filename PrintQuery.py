from sqlite3 import *
import tkinter as tk
from PIL import ImageTk
import mainquery

c1 = mainquery.cursor()
mycursor=c1[0]
conn=c1[1]

def Printquerry(x1,x2,x3,z):
    global mycursor
    w=mycursor.execute("select * from record").fetchall()[-1]
    if(z=="1"):
        return(w)
    b1=mycursor.execute("select fname,lname,contact_no from credentials").fetchall()[-1]
    if(z=="2"):
        return(b1)
    b2=mycursor.execute("select age from record where name=? AND date=? AND phn_no=?",(x1.get(),x3.get(),x2.get())).fetchall()
    if(z=="3"):
        return(b2)
    
    #PATIENT MEDICINE
    l1=[]
    h=()
    mycursor.execute("select medicine,dosage,timings,days from medicine_table where name=? AND phn_no=? AND date=?",(str(x1.get()),str(x2.get()),str(x3.get())))
    for i in mycursor:
        m=list(i)
        d=[]
        for j in m:
            r=j.replace(" ","\n")
            d.append(r)
        h=tuple(d)
        l1.append(h)                
    if(z=="4"):
        return(l1)
    
    #PATIENT DIET
    l2=[]
    mycursor.execute("select nameoffooditem3,foodgroup3,Quantity3,Dimensions3,Timetoeat3 from patientdiet where pname=? AND pphno=? AND pdate=?",(str(x1.get()),str(x2.get()),str(x3.get())))
    for i in mycursor:
        m=list(i)
        d=[]
        for j in m:
            r=(str(j)).replace(" ","\n")
            d.append(r)
        h=tuple(d)
        l2.append(h)
    if(z=="5"):
        return(l2)
    
    #PATIENT YOGA
    l3=[]
    mycursor.execute("select imagepath from yoga where patientname=? AND patientphno=? AND patientdate=?",(str(x1.get()),str(x2.get()),str(x3.get())))
    for i in mycursor:
        l3.append(i[0])
    if(z=="6"):
        return(l3)

def Printimage(z):
    photo=tk.PhotoImage(file="images/Whatsapp-icon.png")
    photo1=tk.PhotoImage(file="images/Gmail-icon.png")
    if(z=="7"):
        return(photo)
    if(z=="8"):
        return(photo1)
    

def Pimage(screen,z):
    screen.bg=ImageTk.PhotoImage(file="images/201.jpg")
    if(z=="9"):
        return(screen.bg)
