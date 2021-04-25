import datetime as dt
from tkinter import *
import medicinequery
import tkinter.ttk as tt
from tkinter import messagebox

    
med1=None
q1=None
listBox=None
t1=None
t2=None
t3=None
t4=None
med2=None
med3=None
listBox1=None
rows=None
s11=None
s22=None
s33=None
s44=None
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        


#=======================   patient medicine   =================================
def del_med():
    selected_item1=listBox1.selection()
    cur_item1=listBox1.focus()
    k1=listBox1.item(cur_item1)["values"]
    if k1=="":
        messagebox.showerror("warning","select the field",parent=med3)
    
    else:
        if messagebox.askyesno("confirm delete","are you sure patient medicine will be deleted permenantly",parent=med3):
            selected_item=listBox.selection()
            cur_item=listBox.focus()
            k=listBox.item(cur_item)["values"]
            #====query========
            medicinequery.delmedicine(k[0],k[1],k[2],k1[0],k1[1],k1[2],k1[3])
      
            #=================
            x=listBox1.selection()[0]
            listBox1.delete(x)
            messagebox.showinfo("Success","Deleted Successfully",parent=med3)
    
def f1(k):
    global s11,s22,s33,s44
    s11.set(k[1])
    s22.set(k[5])
    s33.set(k[0])
    s44.set(k[2])
        
def view_back():
    med3.destroy()


def view_medicine():
    global listBox,s11,s22,s33,s44
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    
    if k=="":
      messagebox.showerror("warning","select the field",parent=med1)
    else:
      #==query===
      r=medicinequery.viewmedicine(k[1],k[0],k[2])
      #==========
      l=[]
      for i in r:
        l.append(i)
      global med3
      med3=Toplevel(med1)
      x, y =med3.winfo_screenwidth(),med3.winfo_screenheight()
      med3.geometry("%dx%d+0+0" %(x,y))
      med3.config(bg='#d6e0f0')
      selected_item=listBox.selection()
      cur_item=listBox.focus()
      #k=listBox.item(cur_item)["values"]
      s11=StringVar()
      s22=StringVar()
      s33=StringVar()
      s44=StringVar()
      
      
      Label(med3, text = "Patient name",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=150,y=33)
      patient_name=Entry(med3,justify='center',textvariable=s11,state='readonly')
      patient_name.place(x=310,y=30, height=40,width=150)
      patient_name.configure(background="white")
      patient_name.configure(font="-family {Palatino Linotype} -size 15")
      patient_name.configure(foreground="#000000")

      Label(med3, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=480,y=33)
      patient_bp = Entry(med3,justify='center',state='readonly',textvariable=s22)
      patient_bp.place(x=530,y=30, height=40,width=150)
      patient_bp.configure(background="white")
      patient_bp.configure(font="-family {Palatino Linotype} -size 15")
      patient_bp.configure(foreground="#000000")

      Label(med3, text = "Date",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=700,y=33)
      patient_date = Entry(med3,justify='center',state='readonly',textvariable=s33)
      patient_date.place(x=770,y=30, height=40,width=150)
      patient_date.configure(background="white")
      patient_date.configure(font="-family {Palatino Linotype} -size 15")
      patient_date.configure(foreground="#000000")

      Label(med3, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=950,y=33)
      patient_n = Entry(med3,justify='center',state='readonly',textvariable=s44)
      patient_n.place(x=1090,y=30, height=40,width=150)
      patient_n.configure(background="white")
      patient_n.configure(font="-family {Palatino Linotype} -size 15")
      patient_n.configure(foreground="#000000")

      f1(k)
      

      
      cols = ('Medicine Name','dosage' ,'timings' ,'days')
      global listBox1
      listBox1 = tt.Treeview(med3, columns=cols, show='headings', selectmode='browse',height=25)
      listBox1.place(relx=0.046, rely=0.120, relheight=0.550, relwidth=0.896)
      for col in cols:
          listBox1.heading(col, text=col)
      vsb = tt.Scrollbar(med3, orient="vertical", command=listBox1.yview)
      vsb.place(relx=0.935, rely=0.120, relheight=0.550, relwidth=0.012)
      #=====query========
      r=medicinequery.viewmedicine(k[1],k[0],k[2])
      #==================
      for i in r:
          listBox1.insert("", "end", values=i)
      Button(med3,text="DELETE",bg="#61c0bf",fg="black",bd=3,height="2",width="25",font=("times new roman",13),command=del_med).place(x=570,y=600)
      Button(med3,text="BACK",bg="#61c0bf",fg="black",bd=3,height="2",width="25",font=("times new roman",13),command=view_back).place(x=870,y=600)
      Button(med3,text="ADD MEDICAL PRESCRIPTION",bg="#61c0bf",fg="black",bd=3,height="2",width="28",font=("times new roman",13),command=add_medicine).place(x=260,y=600)
  
    

def add():
    
    global t1,t2,t3,t4,med2
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    if t1.get()=="" or t2.get()=="":
        messagebox.showerror("warning","fill the fields",parent=med2)

    else:
        #===query=====
        medicinequery.addmedicine(k[1],k[0],k[2],t1.get(),t2.get(),t3.get(),t4.get())

        #query=============
        r=medicinequery.listboxadd(t1.get(),t2.get(),t3.get(),t4.get())
        #==================
        for i in r:
            listBox1.insert("", "end", values=i)
        messagebox.showinfo("Success","medicine Added",parent=med2)
        t1.set("")
        t2.set("")
        t3.set("")
        t4.set("")
        
    
def add_medicine():
    global t1,t2,t3,t4,med2
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    if k=="":
        messagebox.showerror("warning","select the field",parent=med1)

    else:
        med2=Toplevel(med1)
        med2.title("ADD MEDICAL PRESCRIPTION")
        med2.config(bg='#d6e0f0')
        med2.geometry('500x400+300+100')
       
        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        t4=StringVar()
        Label(med2, text = "Medicine name",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=50)
        patient_name=Entry(med2,justify='center',textvariable=t1)
  

        patient_name.place(x=250,y=50, height=40,width=170)
        patient_name.configure(background="white")
        patient_name.configure(font="-family {Palatino Linotype} -size 15")
        patient_name.configure(foreground="#000000")

        Label(med2, text = "dosage",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=100)
        patient_bp=Entry(med2,justify='center',textvariable=t2)
        patient_bp.place(x=250,y=100, height=40,width=170)
        patient_bp.configure(background="white")
        patient_bp.configure(font="-family {Palatino Linotype} -size 15")
        patient_bp.configure(foreground="#000000")

        Label(med2, text = "timings",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=150)
        patient_date=Entry(med2,justify='center',textvariable=t3)

        patient_date.place(x=250,y=150, height=40,width=170)
        patient_date.configure(background="white")
        patient_date.configure(font="-family {Palatino Linotype} -size 15")
        patient_date.configure(foreground="#000000")

        Label(med2, text = "days",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=200)
        patient_n=Entry(med2,justify='center',textvariable=t4)

        patient_n.place(x=250,y=200, height=40,width=170)
        patient_n.configure(background="white")
        patient_n.configure(font="-family {Palatino Linotype} -size 15")
        patient_n.configure(foreground="#000000")
    
        HoverButton(med2,text="ADD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=add).place(x=280,y=280, height=40, width=100)
    

def med_back():
    med1.destroy()
def update_med(rows):
  listBox.delete(*listBox.get_children())
  for i in rows:
    listBox.insert("", "end", values=i)

def clear_med():
  #====query==
  r=medicinequery.medclear()
  #===========
  update_med(r)
  q1.set("")
  



def search_med():
  global rows
  q2=q1.get()
  #====query=====
  rows=medicinequery.searchmed(q2)
  #==============
  update_med(rows)
  


def medicine(t):
    global med1
    med1=Toplevel(t)
    x, y =med1.winfo_screenwidth(),med1.winfo_screenheight()
    med1.geometry("%dx%d+0+0" %(x,y))
    med1.config(bg='#d6e0f0') 
    global q1,listBox
    q1=StringVar()
    cols = ('DATE','NAME' ,'PHONE NO' ,'WEIGHT','HEIGHT','BP','BMI')
    listBox = tt.Treeview(med1, columns=cols, show='headings', selectmode='browse',height=25)
    listBox.place(relx=0.020, rely=0.180, relheight=0.680, relwidth=0.750)
    for col in cols:
        listBox.heading(col, text=col)
    vsb = tt.Scrollbar(med1, orient="vertical", command=listBox.yview)
    vsb.place(relx=0.770, rely=0.180, relheight=0.680, relwidth=0.012)
    vsb1 = tt.Scrollbar(med1, orient="horizontal", command=listBox.xview)
    vsb1.place(relx=0.020, rely=0.860, relheight=0.025, relwidth=0.745)
    listBox.configure(xscrollcommand=vsb1.set)
    #====query======
    r=medicinequery.medlistbox()
    
    #===============
    
    for i in r:
        listBox.insert("", "end", values=i)

    Label(med1,text="PATIENT MEDICINE",font=("times new roman",30),bg="#d6e0f0").place(x=500,y=25)
    Label(med1,text="Enter name",font=("times new roman",18),bg="#d6e0f0").place(x=60,y=30)
    e1=Entry(med1,textvariable=q1).place(x=200,y=25,height=35,width=230)
    
    Button3 = HoverButton(med1,text="VIEW MEDICAL PRESCRIPTION",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=view_medicine)
    Button3.place(relx=0.800, rely=0.400, height=60, width=250)
    Button4= HoverButton(med1,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=med_back)
    Button4.place(relx=0.800, rely=0.550, height=60, width=250)

    Button2 = HoverButton(med1,text="search",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=search_med)
    Button2.place(x=200,y=80, height=40, width=100)
    Button5 = HoverButton(med1,text="clear",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=clear_med)
    Button5.place(x=330,y=80, height=40, width=100)
    

#medicine()
