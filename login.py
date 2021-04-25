#main import modules
import os
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime as dt
import webbrowser
from tkinter import filedialog
from tabulate import tabulate
from fpdf import FPDF
from shutil import copy2
import tkinter.ttk as tt
from tkinter import ttk
import tkinter as tk
from tkinter import *
import history
import medical
import queries
import Print,PrintQuery
import yoga
import diet
import re

global regex
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

##-----------------------------------------------------------------check validity of phn_no-------------------------------------------------------------------##
 
def validNumber(phone_number):
    return all([x.isdigit() for x in phone_number.split("-")])

##----------------------------------------------------------------Menu bar-------------------------------------------------------------------------------------##

def aboutus(t):
        messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)

##-------------------------------------------------------------Saving data in database(Credentials)-------------------------------------------------------------##

def savedata1():
    global email
    
    r=queries.call()
    a=0

    ##-----------------------------------------all feilds are required--------------------------------------------##
    
    if var_fname.get()=="" or email.get()=="" or option.get()=="Select"or var_answer.get()==""or password.get()==""or var_cpass.get()==""or var_con.get()=="":
        messagebox.showerror("Error","All Fields Are Required",parent=root)

    ##----------------------------------------matching password----------------------------------------------------##
        
    elif password.get()!=var_cpass.get():
        messagebox.showerror("Error","Password and Confirm Password should be same",parent=root)

    ##----------------------------------------length of password----------------------------------------------------##
        
    elif (len(password.get())<8):
        messagebox.showerror("Error","Password must be of 8 characters",parent=root)

    ##-------------------------------------------validity of password----------------------------------------------##

    elif not re.search("[a-z]", password.get()) or not re.search("[A-Z]", password.get()) or not re.search("[0-9]", password.get()) or not re.search("[_@$]",password.get()) or re.search("\s", password.get()):
        messagebox.showerror("Error","Password must have capital letter, number and special character",parent=root)

    ##-----------------------------------tick on terms and conditions-------------------------------------------------##
    
    elif var_chk.get()==0:
        messagebox.showerror("Error","Please agree the terms and conditions",parent=root)

    ##-----------------------------------------validity of email----------------------------------------------------##

    elif not re.search(regex,email.get()):
        messagebox.showerror("Error","Please Enter the valid Emailid ",parent=root)

    ##------------------------------------validity of phn_no-----------------------------------------------------##

    elif not validNumber(var_con.get()):
        messagebox.showerror("Error","Please Enter the valid Contact no ",parent=root)
    
    ##--------------------------------------------checking details from database-------------------------------------##
    else:
        
        for i in r:
          if i[3]==email.get() or i[6]==password.get() or i[2]==contact_no.get():
            a=1
            messagebox.showerror("Warning","User already exist",parent=root)
            root.destroy()

    ## ---------------------------------------------if not there then insert-----------------------------------------------##

        
        if a==0:
          ##c.execute('INSERT INTO credentials(fname,lname,contact_no,email_id,question,answer,password,confirm_password) VALUES(?,?,?,?,?,?,?,?)',(var_fname.get(),var_lname.get(),var_con.get(),email.get(),cmb_question.get(),var_answer.get(),password.get(),var_cpass.get()))
            
          queries.ins(var_fname.get(),var_lname.get(),var_con.get(),email.get(),cmb_question.get(),var_answer.get(),password.get(),var_cpass.get())  
        
          messagebox.showinfo("Success","Registration Successful",parent=root)
          var_fname.set("")
          var_lname.set("") 
          email.set("")
          var_con.set("")
          option.set("")
          var_answer.set("")
          password.set("")
          var_cpass.set("")
      

##--------------------------------------------------------------------------------Login Success---------------------------------------------------------------------##

def login_success():
  global email1,password
 
  r=queries.call()
  check=0
  for i in r:
    if i[3]==email1.get() and i[6]==password.get():
      check=1
      screen2.destroy()
      session()
  if check!=1:
    messagebox.showerror("Error"," User not found",parent=screen2)
    email1.set("")
    password.set("")

##------------------------------------------------------------------------------------------------------------------------------------------------------------------##      



def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def del_mainscreen():
  screen.destroy()

def del_root():
  root.destroy()

def del_screen2():
  screen2.destroy()
  screen.deiconify()

def del_screen8():
  screen8.destroy()
def pass1():
    pass

##----------------------------------------------------------------------------------------------------------------------------------------------------------------##

def session():
  screen.destroy()
  global screen8,screen9
  #screen8 = Toplevel(screen)
  screen8=Tk()
  x1, y1 = screen8.winfo_screenwidth(), screen8.winfo_screenheight()
  screen8.geometry("%dx%d+0+0" % (x1, y1))
  
  screen8.bg=ImageTk.PhotoImage(file="images/201.jpg")
  
  screen8.bg_image=Label(screen8,image=screen8.bg).place(x=0,y=0,relwidth=1,relheight=1)
 
  screen8.title("Dashboard")
  screen8.iconbitmap(r"images/logo.ico")

  menue(screen8)
  screen9=Toplevel(screen8)
  screen9.geometry("450x450")
  screen9.resizable(0,0)
  screen9.withdraw() #6b88fe
  screen9.transient(screen8)
  photo=tk.PhotoImage(file="images/Whatsapp-icon.png")
  photo1=tk.PhotoImage(file="images/Gmail-icon.png")
  title=Label(screen8,text=" Welcome to the Dashboard!",font=("times new roman",40),fg="#2d6187",bg="#bedcfa").place(x=100,y=50)
  HoverButton(screen8,text="Patient History",font=("times new roman",18,),activebackground='#a8e6cf',bg="#a3d8f4",bd=3,fg="black",command=lambda:history.Record(screen8),width=18,height=2).place(x=280,y=150)
  HoverButton(screen8,text="Patient Diet",font=("times new roman",18,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=18,height=2,command=lambda:diet.diet1(screen8)).place(x=280,y=350)
  HoverButton(screen8,text="Patient Medicine",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=lambda:medical.medicine(screen8)).place(x=450,y=250)
  HoverButton(screen8,text="Patient Yoga",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=lambda:yoga.yogahere(screen8)).place(x=450,y=450)
  HoverButton(screen8,text="Print",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=lambda:Print.print_btn(screen9,photo,photo1)).place(x=280,y=550)
  
screen8=None
screen2=None
screen9=None


##---------------------------------------------------------------------Updating Details------------------------------------------------------------------------------#

def pass_match():

    if cmb_question.get()=='Select' or var_answer.get()=="" or pass1.get()=="":
        messagebox.showerror("Error","All feilds are required",parent=root2)
    else:   
        queries.call()
        check2=0
        for j in r1:
            if j[4]==cmb_question.get() and j[5]==var_answer.get():
                check2=1
        if check2!=1:
            messagebox.showerror("Error","Enter the correct details",parent=root2)
        else:
           
            queries.upd()
            queries.comm()
            messagebox.showinfo("Success","Password updated successfully. Login Again",parent=root2)
            root2.destroy()
            email1.set("")


##-----------------------------------------------------------------------------update password window---------------------------------------------------------------##

def forgot_password():
    global email1,cmb_question,var_answer,pass1,root2
    if email1.get()=="":
        messagebox.showerror("Error","Please enter  email to reset your password",parent=screen2)

    else:
      queries.call() 
      check1=0
      for i in r:
        if i[3]==email1.get() : 
          check1=1
      if check1!=1:
         messagebox.showerror("Error","Enter the valid email to reset your password",parent=screen2)
      else:
        if check1==1:
          
          root2=Toplevel(screen)
          root2.title("Forgot Password")
          root2.iconbitmap(r"images/logo.ico")
          root2.geometry("350x400+470+150")
          root2.config(bg="white")
          root2.focus_force()
          root2.grab_set()
          Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
          #option=StringVar()
          question=Label(root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
          cmb_question=ttk.Combobox(root2,font=("times new roman",13),state='readonly',justify=CENTER)
          cmb_question['values']=("Select","Your Pet name","Your previous school name","Your previous college","Your Birth Place","Your Bestfriend Name","Your Favourite place","Your favourite holiday destination ")
          cmb_question.place(x=50,y=130,width=250)
          cmb_question.current(0)
          var_answer=StringVar()
          answer=Label(root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=180)
          txt_answer=Entry(root2,font=("times new roman",15),bg="light gray",textvariable=var_answer).place(x=50,y=210,width=250)
          global pass1
          pass1=StringVar()
          Label(root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=260)
          new_pass=Entry(root2,font=("times new roman",15),bg="light gray",textvariable=pass1,show=".").place(x=50,y=290,width=250)
          HoverButton(root2,text="Reset Password",activebackground='#a8e6cf',bg="#a3d8f4",fg="white",font=("times new roman",15,"bold"),command=pass_match).place(x=100,y=340)

email1=None
cmb_question=None
var_answer=None
pass1=None
root2=None         
##---------------------------------------------------------------------------------Registration---------------------------------------------------------------------##



def register():
  queries.create()  
  c=queries.call2()
  for i in c:
    if i[0]==0:
  
      global var_fname,var_lname,var_con,email,password,var_cpass,var_answer,cmb_question,var_chk,root,option
      root=Toplevel(screen)
      root.title("Registration form")
      root.iconbitmap(r"images/logo.ico")
      
      x, y = root.winfo_screenwidth(), root.winfo_screenheight()
      root.geometry("%dx%d+0+0" % (x, y))
      root.bg=ImageTk.PhotoImage(file="images/l1.jpg")
      root.bg_image=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
      frame0=Frame(root,width=400,height=500)
      frame0.place(x=150,y=100,width=400,height=500)

      frame0.bg=ImageTk.PhotoImage(file="images/l4.jpg")
      frame0.bg_image=Label(frame0,image=frame0.bg).place(x=0,y=0,width=350,height=500)

        

      frame1=Frame(root,bg="#eff8ff")
      frame1.place(x=480,y=100,width=700,height=500)
      title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=50)
      var_fname=StringVar()
      f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=100)
      txt_fname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_fname).place(x=50,y=130,width=250)

      var_lname=StringVar()
      l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=100)
      txt_lname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_lname).place(x=370,y=130,width=250)
        

      var_con=StringVar()
      c_name=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=170)
      txt_cname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_con).place(x=50,y=200,width=250) 

      email=StringVar()
      e_name=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=170)
      email_entry=Entry(frame1,font=("times new roman",15),bg="white",textvariable=email).place(x=370,y=200,width=250) 

      option=StringVar()
      question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=240)
      cmb_question=ttk.Combobox(frame1,font=("times new roman",13),textvariable=option,state='readonly',justify=CENTER)
      cmb_question['values']=("Select","Your Pet name","Your previous school name","Your previous college","Your Birth Place","Your Bestfriend Name","Your Favourite place","Your favourite holiday destination ")
      cmb_question.place(x=50,y=270,width=250)
      cmb_question.current(0)

      var_answer=StringVar()
      answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=240)
      txt_answer=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_answer).place(x=370,y=270,width=250)


       
      password=StringVar()
      password2=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=310)
      password_entry=Entry(frame1,font=("times new roman",15),bg="white",textvariable=password,show=".").place(x=50,y=340,width=250)

      var_cpass=StringVar()
      cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=310)
      txt_cpassword=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_cpass,show=".").place(x=370,y=340,width=250)

      var_chk=IntVar()
      chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",variable=var_chk,onvalue=1,offvalue=0,bg="#eff8ff",font=("times new roman",12)).place(x=50,y=380)
        
      btn_register=HoverButton(frame1,text = "Register Now",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",cursor="hand2",command=savedata1,height="1",width="30",font=("times new roman",13)).place(x=50,y=420)
      HoverButton(root,text = "Sign In",activebackground='#a8e6cf',bd=3,bg="#a3d8f4",fg="black",cursor="hand2",height="1",width="30",font=("times new roman",20),command=login).place(x=230,y=530,width=180)
      HoverButton(frame1,text="Back",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,height="1",width="15",font=("times new roman",13),command=del_root).place(x=370,y=420)

    else:
      messagebox.showerror("Error","You are already registered go to login and try Forgot Password",parent=screen)
  
var_fname=None
var_lname=None
var_con=None
email=None
password=None
var_cpass=None
var_chk=None
root=None
option=None

##---------------------------------------------------------------------------------Login -----------------------------------------------------------------------##


def login():
  global screen2,email_entry1,password_entry1,email1,password,password_verify,email_entry1,password_entry1,email1,password
  queries.create()
  def onclosings():
      screen2.destroy()
      screen.destroy()
      
  screen.withdraw()
  screen2 = Toplevel(screen)

  x, y = screen2.winfo_screenwidth(), screen2.winfo_screenheight()
  screen2.geometry("%dx%d+0+0" % (x, y))
  
  screen2.title("Login")
  screen2.iconbitmap(r"images/logo.ico")

  screen2.bg=ImageTk.PhotoImage(file="images/l3.png")
  screen2.bg_image=Label(screen2,image=screen2.bg).place(x=0,y=0,relwidth=1,relheight=1)  
  title=Label(screen2,text="LOGIN HERE",font=("helvetica",34,"bold"),bg="#d0e8f2",fg="#07689f").place(x=740,y=100)

  mycursor=queries.call1()
  v1=[]
  for i in mycursor:
      v1.append(i)
  email1=StringVar()
  email=Label(screen2,text="Email Address",font=("times new roman",20,"bold"),bg="#d0e8f2",fg="#07689f").place(x=740,y=200)
  email_entry1=tt.Combobox(screen2,values=v1,textvariable=email1,font=('Fixed', 12,'bold')).place(x=740,y=250,height=28, width=405)
  
   
  password=StringVar()
  password1=Label(screen2,text="Password",font=("times new roman",20,"bold"),bg="#d0e8f2",fg="#07689f").place(x=740,y=300)
  password_entry1=Entry(screen2,font=("times new roman",15),bg="white",width=40,textvariable=password,show=".").place(x=740,y=350)

  HoverButton(screen2,text="Forgot Password?",font=("times new roman",14),bd=3,activebackground='#a8e6cf',bg="#a3d8f4",command=forgot_password).place(x=740,y=380)
  HoverButton(screen2,text="Login",font=("times new roman",16,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=15,height=2,command=login_success).place(x=740,y=470)
  HoverButton(screen2,text="Back",fg="black",bd=3,height=2,width=15,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",16),command=del_screen2).place(x=990,y=470)

  screen2.protocol("WM_DELETE_WINDOW",onclosings)

  
email_entry1=None
password_entry1=None
email1=None
password=None
password_verify=None
email_entry1=None
password_entry1=None
screen2=None




##------------------------------------------------------------------Hover Button-----------------------------------------------------------##


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


##-----------------------------------------------------------------Main Screen-------------------------------------------------------------------------------------##

    
def main_screen():
  global screen
  screen = Tk()
  x, y = screen.winfo_screenwidth(), screen.winfo_screenheight()
  screen.geometry("%dx%d+0+0" % (x, y))
  screen.bg=ImageTk.PhotoImage(file="images/l1.jpg")
  screen.bg_image=Label(screen,image=screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen.title("DOCTOR CURE")
  screen.iconbitmap(r"images/logo.ico")
  title=Label(screen,text="DOCTOR CURE",font=("impact",60,"bold"),fg="#2d6187",bg="#bedcfa").place(x=270,y=50)
  HoverButton(screen,text="Login",font=("times new roman",14,),activebackground='#a8e6cf',bg="#a3d8f4",bd=3,fg="black",command=login,width=40,height=4).place(x=280,y=250)
  HoverButton(screen,text="Register",font=("times new roman",14,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=40,height=4,command=register).place(x=280,y=390)
  HoverButton(screen,text="Close",fg="black",bd=3,height=2,width=15,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",16),command=del_mainscreen).place(x=390,y=530)



  screen.mainloop()
  screen=None

def menue(t):
    def onclosing():
        t.destroy()
        
    t.deiconify()
    t.iconbitmap(r"images/logo.ico")
    x, y = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (x, y))
    t.resizable(1, 1)

    
    
    #Menue Bar
    menubar=Menu(t)
    t.config(menu=menubar)
    #Sub Menue
    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=submenu)
    submenu.add_command(label="Exit",command=onclosing)

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=submenu)
    submenu.add_command(label="Dashboard",command=session)
    submenu.add_command(label="Patient History",command=pass1)
    submenu.add_command(label="Patient Medicine",command=pass1)
    submenu.add_command(label="Patient Diet",command=pass1)
    submenu.add_command(label="Patient Yoga",command=pass1)

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=submenu)
    submenu.add_command(label="About Us",command=lambda:aboutus(t))

    t.protocol("WM_DELETE_WINDOW",onclosing)

    
main_screen()

