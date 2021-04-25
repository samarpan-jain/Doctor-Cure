#main import modules
from tkinter import messagebox
import datetime as dt
from tkinter import filedialog
from tabulate import tabulate
import tkinter.ttk as tt
from tkinter import ttk
from tkinter import *
import historyquery  



def delete_win1():
  win1.destroy()
def delete_win2():
  win2.destroy()
def delete_win3():
  win3.destroy()
def delete_win4():
  win4.destroy()
def delete_win1():
  win1.destroy()
def delete_win2():
  win2.destroy()
def delete_win3():
  win3.destroy()
def delete_win4():
  win4.destroy()

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'


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

        
def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)
        
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    
    entry.placeholder_state = state

    return state

def add_patient():
  global win2
  win2=Toplevel(win1)
  win2.title("NEW PATIENT")
  win2.config(bg="#bbded6")
  x, y = win2.winfo_screenwidth(), win2.winfo_screenheight()
  win2.geometry("%dx%d+0+0" % (x, y))
  Label(win2, text = "ENTER DETAILS",font=("times new roman",35,),bg="#bbded6",fg="black").place(x=480,y=10)
  
  #=====var name===============
  global P_name
  global P_wght,P_height,P_date,p_no,bload_pressure,P_BMI,patient_age

  P_name      =StringVar()
  P_wght      =StringVar() 
  P_height    =StringVar()
  P_date      =StringVar()
  p_no        =StringVar()
  bload_pressure=StringVar()
  P_BMI       =StringVar()
  patient_age =StringVar()
  #=============================
  
  Label(win2, text = "PATIENT NAME *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=20,y=150, height=40,width=130)
  patient_name_entry1 = Entry(win2, textvariable = P_name)
  add_placeholder_to(patient_name_entry1, 'Enter Patient Name...')
  

  patient_name_entry1.place(x=180,y=150, height=40,width=250)
  patient_name_entry1.configure(background="white")
  patient_name_entry1.configure(font="-family {Palatino Linotype} -size 15")
  
  
  Label(win2, text = "WEIGHT(kg) *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=230, height=40,width=100)
  weight_entry1 = Entry(win2, textvariable = P_wght)
  add_placeholder_to(weight_entry1, 'Enter weight in kg')
  weight_entry1.place(x=180,y=230, height=40,width=250)
  weight_entry1.configure(background="white")
  weight_entry1.configure(font="-family {Palatino Linotype} -size 15")
  
  Label(win2, text = "HEIGHT(m) *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=310, height=40,width=100)
  HEIGHT_entry1 = Entry(win2, textvariable = P_height)
  add_placeholder_to(HEIGHT_entry1, 'Enter height in metre')
  HEIGHT_entry1.place(x=180,y=310, height=40,width=250)
  HEIGHT_entry1.configure(background="white")
  HEIGHT_entry1.configure(font="-family {Palatino Linotype} -size 15")


  
  Label(win2, text = "DATE *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=20,y=400, height=40,width=150)
  DATE_entry1 = Entry(win2, textvariable =P_date)
  add_placeholder_to(DATE_entry1, 'dd/mm/yy')
  DATE_entry1.place(x=180,y=400, height=40,width=250)
  DATE_entry1.configure(background="white")
  DATE_entry1.configure(font="-family {Palatino Linotype} -size 15")

  
  Label(win2, text = "PHONE NO *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=490, height=40,width=100)
  PHONE_entry1 = Entry(win2,textvariable=p_no)
  add_placeholder_to(PHONE_entry1, 'xxxxxxxxxx')
  PHONE_entry1.place(x=180,y=490, height=40,width=250)
  PHONE_entry1.configure(background="white")
  PHONE_entry1.configure(disabledforeground="#a3a3a3")
  PHONE_entry1.configure(font="-family {Palatino Linotype} -size 15")
 
 

  Label(win2, text = "BP *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=470,y=490, height=40,width=100)
  global BP_entry
  BP_entry=Entry(win2,textvariable=bload_pressure)
  add_placeholder_to(BP_entry, 'Eg 80-120')
  BP_entry.place(x=660,y=490,height=40,width=250)
  BP_entry.configure(background="white")
  BP_entry.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "PROBLEM *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=450,y=150, height=40,width=200)
  global ONGOING_DISEASE
  ONGOING_DISEASE=Text(win2,height=4,width=25)
  ONGOING_DISEASE.place(x=660,y=150)
  ONGOING_DISEASE.configure(background="white")
  ONGOING_DISEASE.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "DISEASE (if any)",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=457,y=300, height=40,width=200)
  global ADDITIONAL_DISEASE
  ADDITIONAL_DISEASE=Text(win2,height=5,width=25)
  ADDITIONAL_DISEASE.place(x=660,y=300)
  ADDITIONAL_DISEASE.configure(background="white")
  ADDITIONAL_DISEASE.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "PRECAUTIONS",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=930,y=150, height=40,width=150)
  global PRECAUTION_entry
  PRECAUTION_entry=Text(win2,height=4,width=25)
  PRECAUTION_entry.place(x=1100,y=150)
  PRECAUTION_entry.configure(background="white")
  PRECAUTION_entry.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_entry.configure(foreground="#000000")

  Label(win2, text = "Age *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=930,y=300, height=40,width=100)
  global age_entry
  age_entry=Entry(win2,textvariable=patient_age)
  add_placeholder_to(age_entry,'Enter patient age')
  age_entry.place(x=1100,y=300,height=40,width=250)
  age_entry.configure(background="white")
  age_entry.configure(font="-family {Palatino Linotype} -size 15")
  
  Label(win2, text = "BMI",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=925,y=400, height=40,width=100)

  BMI_entry=Entry(win2,textvariable=P_BMI)
  BMI_entry.place(x=1100,y=400,height=40,width=250)
  BMI_entry.configure(background="white")
  BMI_entry.configure(font="-family {Palatino Linotype} -size 15")
  BMI_entry.configure(foreground="#000000")
  
  add=HoverButton(win2,text="ADD PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",15),command=savedata).place(x=400,y=590)
  n_back=HoverButton(win2,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",15),command=delete_win2).place(x=700,y=590)
  HoverButton(win2,text="CALCULATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="1",width="12",font=("times new roman",15),command=bmi).place(x=1100,y=450)
  
win2=None
P_name=None
P_wght=None
P_height=None
P_date=None
p_no=None
bload_pressure=None
P_BMI=None
BP_entry=None
ONGOING_DISEASE=None
ADDITIONAL_DISEASE=None
PRECAUTION_entry=None
def bmi():
  if P_wght.get()=="" or P_height.get()=="":
    messagebox.showerror("Enter height and date",parent=win2)
  else:
    b=round(float(P_wght.get())/(float(P_height.get())*float(P_height.get())))
    P_BMI.set(str(b))
    

def savedata():
  if P_name.get()=="" or P_date.get()=="" or P_wght.get()==""or P_height.get()==""or p_no.get()==""or bload_pressure.get()=="" or ONGOING_DISEASE.get("1.0","end-1c")=="":
    messagebox.showerror("Error","Fill necessary Fields",parent=win2)
  elif len(p_no.get())!=10 :
    messagebox.showerror("warning","enter correct no",parent=win2)
    p_no.set("")
  else:
    r=historyquery.save(1)
    a=0
    for i in r:
      if i[4]==p_no.get() and i[0]==P_name.get():
        a=1
        messagebox.showerror("warning","already exists",parent=win2)
        win2.destroy()
    if a==0: 
      try:
        d=dt.datetime.strptime(P_date.get(),"%d/%m/%y")
        historyquery.save(P_name.get(),P_wght.get(),P_height.get(),P_date.get(),p_no.get(),bload_pressure.get(),ONGOING_DISEASE.get("1.0","end-1c"),ADDITIONAL_DISEASE.get("1.0","end-1c"),PRECAUTION_entry.get("1.0","end-1c"),P_BMI.get(),patient_age.get())
        messagebox.showinfo("Success","Patient Added Successfully",parent=win2)
        win2.destroy()
      except:
        messagebox.showerror("warning","enter date in correct format",parent=win2)
  

def inner_add():
  updated_ong=ONGOING_DISEASE_update.get("1.0","end-1c")
  updated_additional=ADDITIONAL_DISEASE_update.get("1.0","end-1c")
  updated_prec=PRECAUTION_update.get("1.0","end-1c")
  no=p_no_display.get()
  date=u4.get()  
  if u4.get()=="":
    messagebox.showerror("warning","enter date",parent=win5)
  elif u4.get()==D_display.get():
    messagebox.showerror("warning","patient already exist for current date go to update menu",parent=win5)
  elif u7.get()=="":
    messagebox.showerror("warning","calculate the bmi",parent=win5)
  elif ONGOING_DISEASE_update.get("1.0","end-1c")=="":
    messagebox.showerror("warning","fill the fields",parent=win5)

  else:
    try:
      d=dt.datetime.strptime(u4.get(),"%d/%m/%y")
      #====query====
      historyquery.save(u1.get(),u2.get(),u3.get(),u4.get(),u5.get(),u6.get(),updated_ong,updated_additional,updated_prec,u7.get(),u8.get())
      #====query====
      messagebox.showinfo("Success","Added Successfully",parent=win5)
      win5.destroy()
      win4.destroy()
      win3.destroy()
    except:
      messagebox.showerror("warning","enter date in correct format",parent=win5)
  
def mod_bmi():
  if u2.get()=="" or u3.get()=="":
    messagebox.showerror("Enter height and weight",parent=win2)
  else:
    b=round(float(u2.get())/(float(u3.get())*float(u3.get())))
    u7.set(str(b))     
def modify():
  global win5
  
  global u1,u2,u3,u4,u5,u6,u7,u8

  u1=StringVar()
  u2=StringVar()
  u3=StringVar()
  u4=StringVar()
  u5=StringVar()
  u6=StringVar()
  u7=StringVar()
  u8=StringVar()
  u1.set(P_display.get())
  u2.set(W_display.get())
  u3.set(H_display.get())
  u5.set(p_no_display.get())
  u6.set(bload_pressure_display.get())
  u8.set(age_display.get())
  win5 = Toplevel(win4)
  win5.config(bg='#d6e0f0')
  win5.title("PATIENT RECORD")
  x, y = win5.winfo_screenwidth(), win5.winfo_screenheight()
  win5.geometry("%dx%d+0+0" % (x, y))
  Label(win5, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=50,y=30, height=40,width=150)
  patient_update = Entry(win5,textvariable=u1,justify='center',state='readonly')
  patient_update.place(x=30,y=80, height=40,width=200)
  patient_update.configure(background="white")
  patient_update.configure(font="-family {Palatino Linotype} -size 15")
  patient_update.configure(foreground="#000000")
  

  Label(win5, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=310,y=30, height=40,width=100)
  weight_update = Entry(win5,textvariable =u2,justify='center')
  weight_update.place(x=260,y=80, height=40,width=200)
  weight_update.configure(background="white")
  weight_update.configure(font="-family {Palatino Linotype} -size 15")
  weight_update.configure(foreground="#000000")


  Label(win5, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=585,y=30, height=40,width=100)
  HEIGHT_update = Entry(win5,textvariable =u3,justify='center')
  HEIGHT_update.place(x=540,y=80, height=40,width=200)
  HEIGHT_update.configure(background="white")
  HEIGHT_update.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_update.configure(foreground="#000000")
  
 
  Label(win5, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1060,y=30, height=40,width=150)
  DATE_update = Entry(win5,textvariable =u4)
  add_placeholder_to(DATE_update, 'dd/mm/yy')
  DATE_update.place(x=1030,y=80, height=40,width=200)
  DATE_update.configure(background="white")
  DATE_update.configure(font="-family {Palatino Linotype} -size 15")
  DATE_update.configure(foreground="#000000")
  

  Label(win5, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=150, height=40,width=100)
  PHONE_update = Entry(win5,textvariable=u5,justify='center',state='readonly')
  PHONE_update.place(x=1030,y=200, height=40,width=200)
  PHONE_update.configure(background="white")
  PHONE_update.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_update.configure(foreground="#000000")
  
  Label(win5, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=550, height=40,width=100)
  BP_update=Entry(win5,textvariable=u6,justify='center')
  BP_update.place(x=1030,y=600,height=40,width=200)
  BP_update.configure(background="white")
  BP_update.configure(font="-family {Palatino Linotype} -size 15")
  BP_update.configure(foreground="#000000")
  
  

  Label(win5, text = "PROBLEM *",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=190,y=200, height=40,width=200)
  global ONGOING_DISEASE_update
  ONGOING_DISEASE_update=Text(win5,height=8,width=32)
  ONGOING_DISEASE_update.place(x=150,y=250)
  ONGOING_DISEASE_update.configure(background="white")
  ONGOING_DISEASE_update.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_update.configure(foreground="#000000")
 

  Label(win5, text = "DISEASE (if any)",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=550,y=200, height=40,width=200)
  global ADDITIONAL_DISEASE_update
  ADDITIONAL_DISEASE_update=Text(win5,height=8,width=32)
  ADDITIONAL_DISEASE_update.place(x=530,y=250)
  ADDITIONAL_DISEASE_update.configure(background="white")
  ADDITIONAL_DISEASE_update.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_update.configure(foreground="#000000")
 

  Label(win5, text = "PRECAUTIONS",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=250, height=40,width=120)
  global PRECAUTION_update
  PRECAUTION_update=Text(win5,height=5,width=20)
  PRECAUTION_update.place(x=1030,y=300)
  PRECAUTION_update.configure(background="white")
  PRECAUTION_update.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_update.configure(foreground="#000000")


  Label(win5, text = "Age *",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=815,y=30, height=40,width=100)
  global age_update
  age_update=Entry(win5,textvariable=u8,justify='center')
  age_update.place(x=770,y=80,height=40,width=200)
  age_update.configure(background="white")
  age_update.configure(font="-family {Palatino Linotype} -size 15")

  Label(win5, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=450, height=40,width=100)
  BMI_update=Entry(win5,textvariable=u7,justify='center')
  BMI_update.place(x=1030,y=500,height=40,width=200)
  BMI_update.configure(background="white")
  BMI_update.configure(font="-family {Palatino Linotype} -size 15")
  BMI_update.configure(foreground="#000000")
  
  HoverButton(win5,text="ADD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="20",font=("times new roman",13),command=inner_add).place(x=400,y=570)
  HoverButton(win5,text="CALCULATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="1",width="12",font=("times new roman",13),command=mod_bmi).place(x=1230,y=504)
  
win5=None
u1=None
u2=None
u3=None
u4=None
u5=None
u6=None
u7=None
u8=None
ONGOING_DISEASE_update=None
ADDITIONAL_DISEASE_update=None
PRECAUTION_update=None

def update_prev_comm():
  updated_prev_ong=ONGOING_DISEASE_update_prev.get("1.0","end-1c")
  updated_prev_additional=ADDITIONAL_DISEASE_update_prev.get("1.0","end-1c")
  updated_prev_prec=PRECAUTION_update_prev.get("1.0","end-1c")
  #===query====
  historyquery.save(updated_prev_ong,updated_prev_additional,updated_prev_prec,bload_pressure_update_prev.get(),P_update_prev.get(),D_update_prev.get(),p_no_update_prev.get())
  #=============
  messagebox.showinfo("Success","updated successully",parent=win10)
  win10.destroy()
  win4.destroy()
  

def update_prev():
  global win10
  win10 = Toplevel(win4)
  win10.config(bg='#d6e0f0')
  win10.title("PATIENT RECORD")
  x, y = win10.winfo_screenwidth(), win10.winfo_screenheight()
  win10.geometry("%dx%d+0+0" % (x, y))
  global P_update_prev,W_update_prev,H_update_prev,D_update_prev,p_no_update_prev,bload_pressure_update_prev,P_BMI_update_prev
  global ONGOING_DISEASE_update_prev,ADDITIONAL_DISEASE_update_prev,PRECAUTION_update_prev,age_field_update
  P_update_prev=StringVar()
  W_update_prev=StringVar()
  H_update_prev=StringVar()
  D_update_prev=StringVar()
  p_no_update_prev=StringVar()
  bload_pressure_update_prev=StringVar()
  P_BMI_update_prev=StringVar()
  age_field_update=StringVar()
  P_update_prev.set(P_display.get())
  W_update_prev.set(W_display.get())
  H_update_prev.set(H_display.get())
  p_no_update_prev.set(p_no_display.get())
  bload_pressure_update_prev.set(bload_pressure_display.get())
  P_BMI_update_prev.set(P_BMI_display.get())
  D_update_prev.set(D_display.get())
  age_field_update.set(age_display.get())

  Label(win10, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=300,y=30, height=40,width=150)
  patient_update_prev = Entry(win10,textvariable=P_update_prev,justify='center',state='readonly')
  patient_update_prev.place(x=270,y=80, height=40,width=200)
  patient_update_prev.configure(background="white")
  patient_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  patient_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=250, height=40,width=100)
  weight_update_prev = Entry(win10,textvariable =W_update_prev,justify='center',state='readonly')
  weight_update_prev.place(x=1100,y=300, height=40,width=200)
  weight_update_prev.configure(background="white")
  weight_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  weight_update_prev.configure(foreground="#000000")


  Label(win10, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=350, height=40,width=100)
  HEIGHT_update_prev = Entry(win10,textvariable =H_update_prev,justify='center',state='readonly')
  HEIGHT_update_prev.place(x=1100,y=400, height=40,width=200)
  HEIGHT_update_prev.configure(background="white")
  HEIGHT_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_update_prev.configure(foreground="#000000")
  
 
  Label(win10, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1140,y=30, height=40,width=110)
  DATE_update_prev = Entry(win10,textvariable =D_update_prev,justify='center',state='readonly')
  DATE_update_prev.place(x=1100,y=80, height=40,width=200)
  DATE_update_prev.configure(background="white")
  DATE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  DATE_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=150, height=40,width=110)
  PHONE_update_prev = Entry(win10,textvariable=p_no_update_prev,justify='center',state='readonly')
  PHONE_update_prev.place(x=1100,y=200, height=40,width=200)
  PHONE_update_prev.configure(background="white")
  PHONE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_update_prev.configure(foreground="#000000")
  
  Label(win10, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=550, height=40,width=100)
  BP_update_prev=Entry(win10,justify='center',textvariable=bload_pressure_update_prev)
  BP_update_prev.place(x=1100,y=600,height=40,width=200)
  BP_update_prev.configure(background="white")
  BP_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  BP_update_prev.configure(foreground="#000000")


  Label(win10, text = "Age",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=715,y=30, height=40,width=100)
  global age_display_entry
  age_update_prev=Entry(win10,textvariable=age_field_update,justify='center',state='readonly')
  age_update_prev.place(x=670,y=80,height=40,width=200)
  age_update_prev.configure(background="white")
  age_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  

  Label(win10, text = "PROBLEM *",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=80,y=150, height=40,width=350)
  ONGOING_DISEASE_update_prev=Text(win10,height=12,width=32)
  ONGOING_DISEASE_update_prev.place(x=80,y=200)
  ONGOING_DISEASE_update_prev.configure(background="white")
  ONGOING_DISEASE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_update_prev.configure(foreground="#000000")
 

  Label(win10, text = "DISEASE (if any)",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=390,y=150, height=40,width=330)
  ADDITIONAL_DISEASE_update_prev=Text(win10,height=12,width=32)
  ADDITIONAL_DISEASE_update_prev.place(x=390,y=200)
  ADDITIONAL_DISEASE_update_prev.configure(background="white")
  ADDITIONAL_DISEASE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_update_prev.configure(foreground="#000000")
 

  Label(win10, text = "PRECAUTIONS",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=695,y=150, height=40,width=330)
  PRECAUTION_update_prev=Text(win10,height=12,width=32)
  PRECAUTION_update_prev.place(x=700,y=200)
  PRECAUTION_update_prev.configure(background="white")
  PRECAUTION_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=450, height=40,width=100)
  BMI_update_prev=Entry(win10,state='readonly',justify='center',textvariable=P_BMI_update_prev)
  BMI_update_prev.place(x=1100,y=500,height=40,width=200)
  BMI_update_prev.configure(background="white")
  BMI_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  BMI_update_prev.configure(foreground="#000000")
  ONGOING_DISEASE_update_prev.insert(END,ONGOING_DISEASE_display.get("1.0","end-1c"))
  ADDITIONAL_DISEASE_update_prev.insert(END,ADDITIONAL_DISEASE_display.get("1.0","end-1c"))
  PRECAUTION_update_prev.insert(END,PRECAUTION_display.get("1.0","end-1c"))
  
  add_problem=HoverButton(win10,text="UPDATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=update_prev_comm).place(x=360,y=570)
  
win10=None
P_update_prev=None
W_update_prev=None
H_update_prev=None
D_update_prev=None
p_no_update_prev=None
bload_pressure_update_prev=None
o_dis_update_prev=None
add_dis_update_prev=None
prec_update_prev=None
P_BMI_update_prev=None
ONGOING_DISEASE_update_prev=None
ADDITIONAL_DISEASE_update_prev=None
PRECAUTION_update_prev=None





def old_patient_show():
  global win4
  global P_display,W_display,H_display,D_display,p_no_display,bload_pressure_display,P_BMI_display,age_display
  P_display=StringVar()
  W_display=StringVar()
  H_display=StringVar()
  D_display=StringVar()
  p_no_display=StringVar()
  bload_pressure_display=StringVar()
  P_BMI_display=StringVar()
  age_display=StringVar()
  
  win4= Toplevel(win3)
  win4.config(bg='#d6e0f0')
  win4.title("PATIENT RECORD")
  x, y = win4.winfo_screenwidth(), win4.winfo_screenheight()
  win4.geometry("%dx%d+0+0" % (x, y))
  Label(win4, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=290,y=30, height=40,width=150)
  patient_display = Entry(win4,textvariable=P_display,justify='center',state='readonly')
  patient_display.place(x=270,y=80, height=40,width=200)
  patient_display.configure(background="white")
  patient_display.configure(font="-family {Palatino Linotype} -size 15")
  patient_display.configure(foreground="#000000")
  

  Label(win4, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=250, height=40,width=100)
  weight_display = Entry(win4,textvariable =W_display,justify='center',state='readonly')
  weight_display.place(x=1100,y=300, height=40,width=200)
  weight_display.configure(background="white")
  weight_display.configure(font="-family {Palatino Linotype} -size 15")
  weight_display.configure(foreground="#000000")


  Label(win4, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=350, height=40,width=100)
  HEIGHT_display = Entry(win4,textvariable =H_display,justify='center',state='readonly')
  HEIGHT_display.place(x=1100,y=400, height=40,width=200)
  HEIGHT_display.configure(background="white")
  HEIGHT_display.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_display.configure(foreground="#000000")
  
 
  Label(win4, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1140,y=30, height=40,width=110)
  DATE_display = Entry(win4,textvariable =D_display,justify='center',state='readonly')
  DATE_display.place(x=1100,y=80, height=40,width=200)
  DATE_display.configure(background="white")
  DATE_display.configure(font="-family {Palatino Linotype} -size 15")
  DATE_display.configure(foreground="#000000")
  

  Label(win4, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=150, height=40,width=110)
  PHONE_display = Entry(win4,textvariable=p_no_display,justify='center',state='readonly')
  PHONE_display.place(x=1100,y=200, height=40,width=200)
  PHONE_display.configure(background="white")
  PHONE_display.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_display.configure(foreground="#000000")
  
  Label(win4, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=550, height=40,width=100)
  BP_display=Entry(win4,justify='center',textvariable=bload_pressure_display,state='readonly')
  BP_display.place(x=1100,y=600,height=40,width=200)
  BP_display.configure(background="white")
  BP_display.configure(font="-family {Palatino Linotype} -size 15")
  BP_display.configure(foreground="#000000")
  
  

  Label(win4, text = "PROBLEM *",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=80,y=150, height=40,width=350)
  global ONGOING_DISEASE_display
  ONGOING_DISEASE_display=Text(win4,height=12,width=32)
  ONGOING_DISEASE_display.place(x=80,y=200)
  ONGOING_DISEASE_display.configure(background="#eeeeee")
  ONGOING_DISEASE_display.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_display.configure(foreground="#000000")
 

  Label(win4, text = "DISEASE (if any)",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=390,y=150, height=40,width=330)
  global ADDITIONAL_DISEASE_display
  ADDITIONAL_DISEASE_display=Text(win4,height=12,width=32)
  ADDITIONAL_DISEASE_display.place(x=390,y=200)
  ADDITIONAL_DISEASE_display.configure(background="#eeeeee")
  ADDITIONAL_DISEASE_display.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_display.configure(foreground="#000000")
 

  Label(win4, text = "PRECAUTIONS",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=695,y=150, height=40,width=330)
  global PRECAUTION_display
  PRECAUTION_display=Text(win4,height=12,width=32)
  PRECAUTION_display.place(x=700,y=200)
  PRECAUTION_display.configure(background="#eeeeee")
  PRECAUTION_display.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_display.configure(foreground="#000000")

  Label(win4, text = "Age",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=690,y=30, height=40,width=100)
  global age_display_entry
  age_display_entry=Entry(win4,textvariable=age_display,justify='center',state='readonly')
  age_display_entry.place(x=650,y=80,height=40,width=200)
  age_display_entry.configure(background="white")
  age_display_entry.configure(font="-family {Palatino Linotype} -size 15")
  

  Label(win4, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=450, height=40,width=100)
  BMI_display=Entry(win4,state='readonly',justify='center',textvariable=P_BMI_display)
  BMI_display.place(x=1100,y=500,height=40,width=200)
  BMI_display.configure(background="white")
  BMI_display.configure(font="-family {Palatino Linotype} -size 15")
  BMI_display.configure(foreground="#000000")
  

  add_problem=HoverButton(win4,text="ADD ANOTHER RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=modify).place(x=200,y=570)
  HoverButton(win4,text="UPDATE THE RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=update_prev).place(x=600,y=570)
  
win4=None
P_display=None
W_display=None
H_display=None
D_display=None
p_no_display=None
bload_pressure_display=None
o_dis_display=None
add_dis_display=None
prec_display=None
P_BMI_display=None
ONGOING_DISEASE_display=None
ADDITIONAL_DISEASE_display=None
PRECAUTION_display=None

def update(rows):
  listBox.delete(*listBox.get_children())
  for i in rows:
    listBox.insert("", "end", values=i)

def clear():
  #====query=====
  z=historyquery.listboxclear()
  #===========================
  update(z)
  q.set("")
  



def search():
  global rows
  q2=q.get()
  #====query=====
  rows=historyquery.listboxsearch(q2)
  #====query=====
  update(rows)
  
rows=None



def view_record():
  selected_item=listBox.selection()
  cur_item=listBox.focus()
  k=listBox.item(cur_item)["values"]
  #====query====
  r=historyquery.save(1)
  #=============
  check=0
  if k=="":
    messagebox.showerror("warning","select the patient",parent=win3)
  else:
    for i in r:
      if i[3]==k[0] and i[0]==k[1]:
        check=1
        old_patient_show()
        P_display.set(i[0])
        W_display.set(i[1])
        H_display.set(i[2])
        p_no_display.set(i[4])
        bload_pressure_display.set(i[5])
        ONGOING_DISEASE_display.insert(END,i[6])
        ADDITIONAL_DISEASE_display.insert(END,i[7])
        PRECAUTION_display.insert(END,i[8])
        P_BMI_display.set(i[9])
        age_display.set(i[10])
        D_display.set(i[3])
        ONGOING_DISEASE_display.configure(state='disabled')
        ADDITIONAL_DISEASE_display.configure(state='disabled')
        PRECAUTION_display.configure(state='disabled')
  
def del_history():
  selected_item=listBox.selection()
  cur_item=listBox.focus()
  k=listBox.item(cur_item)["values"]
  dele=0
  if k=="":
    messagebox.showerror("warning","select the patient",parent=win3)
   
  else:
    if messagebox.askyesno("confirm delete","are you sure patient record will be deleted permenantly",parent=win3):
      #====query=====
      historyquery.delrecord(k[0],k[1],k[2])
      #====query=====
      messagebox.showinfo("Success","Deleted Successfully",parent=win3)
      x=listBox.selection()[0]
      listBox.delete(x)
    




def history():
    global win3
    win3=Toplevel(win1)
    global q,listBox
    q=StringVar()
    x, y =win3.winfo_screenwidth(),win3.winfo_screenheight()
    win3.geometry("%dx%d+0+0" %(x,y))
    win3.config(bg='#e4f9f5')
    cols = ('DATE','NAME' ,'PHONE NO' ,'WEIGHT','HEIGHT','BP','BMI')
    listBox = tt.Treeview(win3, columns=cols, show='headings', selectmode='browse',height=25)
    listBox.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
    for col in cols:
        listBox.heading(col, text=col)
    vsb = tt.Scrollbar(win3, orient="vertical", command=listBox.yview)
    vsb.place(relx=0.937, rely=0.216, relheight=0.580, relwidth=0.012)
    vsb1 = tt.Scrollbar(win3, orient="horizontal", command=listBox.xview)
    vsb1.place(relx=0.046, rely=0.797, relheight=0.025, relwidth=0.896)
    listBox.configure(xscrollcommand=vsb1.set)
    #===query===
    c=historyquery.listboxclear()
    #======
    for i in c:
        listBox.insert("", "end", values=i)
    Label(win3,text="PATIENT RECORD",font=("times new roman",30),bg="#e4f9f5").place(x=500,y=50)
    Label(win3,text="Enter name",font=("times new roman",18),bg="#e4f9f5").place(x=60,y=70)
    Entry(win3,textvariable=q).place(x=200,y=65,height=35,width=230)
    Button1 = HoverButton(win3,text="VIEW RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=view_record)
    Button1.place(relx=0.200, rely=0.867, height=60, width=250)
    Button2 = HoverButton(win3,text="search",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=search)
    Button2.place(x=200,y=110, height=40, width=100)
    Button3 = HoverButton(win3,text="DELETE RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=del_history)
    Button3.place(relx=0.400, rely=0.867, height=60, width=250)
    Button4= HoverButton(win3,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=delete_win3)
    Button4.place(relx=0.600, rely=0.867, height=60, width=250)
    Button5 = HoverButton(win3,text="clear",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=clear)
    Button5.place(x=330,y=110, height=40, width=100)
    
win3=None
listBox=None
q=None


    

def Record(t):
  global win1
  win1=Toplevel(t)
  #menue(win1)
  win1.title("PATIENT RECORD")
  x, y = win1.winfo_screenwidth(), win1.winfo_screenheight()
  win1.geometry("%dx%d+0+0" %(x,y))
  sc=historyquery.Himage(win1)
  win1.bg_image=Label(win1,image=sc).place(x=0,y=0,relwidth=1,relheight=1)
  
  
  title=Label(win1,text="PATIENT RECORD",font=("helvetica",34,"bold"),fg="black",bg="#e6e6e6").place(x=490,y=80)
  new_patient=HoverButton(win1,text="ADD NEW PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",height="4",bd=3,width="40",font=("helvetica",13),command = add_patient).place(x=500,y=200)
  existing_patient=HoverButton(win1,text="EXISTING PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="4",width="40",font=("helvetica",13),command=history).place(x=500,y=310)
  main_close=HoverButton(win1,text="CLOSE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=delete_win1).place(x=545,y=450)
win1=None


#======================================================================================================================================================================================================================

