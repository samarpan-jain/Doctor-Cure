import yogaQuery
from tkinter import messagebox
import datetime as dt
import tkinter.ttk as tt
import tkinter as tk

def yoga(top,top1,imgl,t1,t2,t3,listBox5):
     top1.deiconify()
     def onclosing():
        top1.withdraw()

     Label1 = tk.Label(top)
     Label1.grid(row=0,column=2,pady=20)
     Label1.configure(font="-family {Palatino Linotype} -size 32 -weight bold")
     Label1.configure(text='''PATIENT YOGA AND EXERCISE''')

     l1=tk.Label(top,text="Name :")
     l1.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l1.grid(row=1,column=1,pady=20,sticky="w")

     t1=tk.StringVar()
     e1=tk.Entry(top,width=26,textvariable=t1)
     e1.configure(font="-family {Palatino Linotype} -size 15")
     e1.grid(row=1,column=1,pady=20,sticky="e")

     l2=tk.Label(top,text="Phone No :")
     l2.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l2.grid(row=1,column=2,padx=20,pady=20,sticky="w")

     t2=tk.StringVar()
     e2=tk.Entry(top,width=24,textvariable=t2)
     e2.configure(font="-family {Palatino Linotype} -size 15")
     e2.grid(row=1,column=2,padx=140,pady=20,sticky="w")

     l3=tk.Label(top,text="Date(dd/mm/yy):")
     l3.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l3.grid(row=1,column=2,columnspan=2,padx=420,pady=20,sticky="w")

     t3=tk.StringVar()
     e3=tk.Entry(top,width=26,textvariable=t3)
     e3.configure(font="-family {Palatino Linotype} -size 15")
     e3.grid(row=1,column=2,columnspan=1,pady=20,sticky="e")

     b1=tk.Button(top,text="Submit",bg="#61c0bf",command=lambda:submit(top,cb,t1,t2,t3,listBox5),padx=80)
     b1.configure(font="-family {Palatino Linotype} -size 15")
     b1.grid(row=1,column=3,pady=20)

     cb=[]
     Cb=[]
     image=[]
     for i in range(1,41):
         cbi=tk.BooleanVar()
         Cbi= tk.Checkbutton(top,var=cbi)
         cb.append(cbi)
         Cb.append(Cbi)

     for j in range(0,40):
         Imgj=tk.Label(top,image=imgl[j])
         image.append(Imgj)
         
     Cb[0].grid(row=2,column=0,sticky="w")
     image[0].grid(row=2,column=1,padx=20,pady=20,sticky="e")
     
     Cb[1].grid(row=2,column=2,columnspan=1,padx=20,sticky="w")
     image[1].grid(row=2,column=2,sticky="w",padx=70)

     Cb[2].grid(row=2,column=2,padx=410,sticky="w")
     image[2].grid(row=2,column=2,padx=80,sticky="e")

     Cb[3].grid(row=2,column=3,sticky="w")
     image[3].grid(row=2,column=3,padx=40,sticky="e")

     Cb[4].grid(row=3,column=0,sticky="w")
     image[4].grid(row=3,column=1,padx=20,pady=20,sticky="e")

     Cb[5].grid(row=3,column=2,columnspan=1,padx=20,sticky="w")
     image[5].grid(row=3,column=2,sticky="w",padx=70)

     Cb[6].grid(row=3,column=2,padx=410,sticky="w")
     image[6].grid(row=3,column=2,padx=80,sticky="e")

     Cb[7].grid(row=3,column=3,sticky="w")
     image[7].grid(row=3,column=3,padx=40,sticky="e")

     Cb[8].grid(row=4,column=0,sticky="w")
     image[8].grid(row=4,column=1,padx=20,pady=20,sticky="e")

     Cb[9].grid(row=4,column=2,columnspan=1,padx=20,sticky="w")
     image[9].grid(row=4,column=2,sticky="w",padx=70)

     Cb[10].grid(row=4,column=2,padx=410,sticky="w")
     image[10].grid(row=4,column=2,padx=80,sticky="e")

     Cb[11].grid(row=4,column=3,sticky="w")
     image[11].grid(row=4,column=3,padx=40,sticky="e")

     Cb[12].grid(row=5,column=0,sticky="w")
     image[12].grid(row=5,column=1,padx=20,pady=20,sticky="e")

     Cb[13].grid(row=5,column=2,columnspan=1,padx=20,sticky="w")
     image[13].grid(row=5,column=2,sticky="w",padx=70)

     Cb[14].grid(row=5,column=2,padx=410,sticky="w")
     image[14].grid(row=5,column=2,padx=80,sticky="e")

     Cb[15].grid(row=5,column=3,sticky="w")
     image[15].grid(row=5,column=3,padx=40,sticky="e")

     Cb[16].grid(row=6,column=0,sticky="w")
     image[16].grid(row=6,column=1,padx=20,pady=20,sticky="e")

     Cb[17].grid(row=6,column=2,columnspan=1,padx=20,sticky="w")
     image[17].grid(row=6,column=2,sticky="w",padx=70)

     Cb[18].grid(row=6,column=2,padx=410,sticky="w")
     image[18].grid(row=6,column=2,padx=80,sticky="e")

     Cb[19].grid(row=6,column=3,sticky="w")
     image[19].grid(row=6,column=3,padx=40,sticky="e")

     Cb[20].grid(row=7,column=0,sticky="w")
     image[20].grid(row=7,column=1,padx=20,pady=20,sticky="e")
     
     Cb[21].grid(row=7,column=2,columnspan=1,padx=20,sticky="w")
     image[21].grid(row=7,column=2,sticky="w",padx=70)

     Cb[22].grid(row=7,column=2,padx=410,sticky="w")
     image[22].grid(row=7,column=2,padx=80,sticky="e")

     Cb[23].grid(row=7,column=3,sticky="w")
     image[23].grid(row=7,column=3,padx=40,sticky="e")

     Cb[24].grid(row=8,column=0,sticky="w")
     image[24].grid(row=8,column=1,padx=20,pady=20,sticky="e")
     
     Cb[25].grid(row=8,column=2,columnspan=1,padx=20,sticky="w")
     image[25].grid(row=8,column=2,sticky="w",padx=70)

     Cb[26].grid(row=8,column=2,padx=410,sticky="w")
     image[26].grid(row=8,column=2,padx=80,sticky="e")

     Cb[27].grid(row=8,column=3,sticky="w")
     image[27].grid(row=8,column=3,padx=40,sticky="e")

     Cb[28].grid(row=9,column=0,sticky="w")
     image[28].grid(row=9,column=1,padx=20,pady=20,sticky="e")
     
     Cb[29].grid(row=9,column=2,columnspan=1,padx=20,sticky="w")
     image[29].grid(row=9,column=2,sticky="w",padx=70)

     Cb[30].grid(row=9,column=2,padx=410,sticky="w")
     image[30].grid(row=9,column=2,padx=80,sticky="e")

     Cb[31].grid(row=9,column=3,sticky="w")
     image[31].grid(row=9,column=3,padx=40,sticky="e")

     Cb[32].grid(row=10,column=0,sticky="w")
     image[32].grid(row=10,column=1,padx=20,pady=20,sticky="e")
     
     Cb[33].grid(row=10,column=2,columnspan=1,padx=20,sticky="w")
     image[33].grid(row=10,column=2,sticky="w",padx=70)

     Cb[34].grid(row=10,column=2,padx=410,sticky="w")
     image[34].grid(row=10,column=2,padx=80,sticky="e")

     Cb[35].grid(row=10,column=3,sticky="w")
     image[35].grid(row=10,column=3,padx=40,sticky="e")

     Cb[36].grid(row=11,column=0,sticky="w")
     image[36].grid(row=11,column=1,padx=20,pady=20,sticky="e")
     
     Cb[37].grid(row=11,column=2,columnspan=1,padx=20,sticky="w")
     image[37].grid(row=11,column=2,sticky="w",padx=70)

     Cb[38].grid(row=11,column=2,padx=410,sticky="w")
     image[38].grid(row=11,column=2,padx=80,sticky="e")

     Cb[39].grid(row=11,column=3,sticky="w")
     image[39].grid(row=11,column=3,padx=40,sticky="e")

     try:   
         w=yogaQuery.SelectQuery("2")
         t1.set(w[0])
         t2.set(w[4])
         t3.set(w[3])
     except:
         pass

def clears(t1,t2,t3):
 t1.set("")
 t2.set("")
 t3.set("")

def submit(tp,d1,t1,t2,t3,listBox5):
   q1=[]
   for i in range(1,41):
      if d1[i-1].get()==True:
         q1.append("images/"+str(i)+".png")
      else:
         pass
   u=0
   if(t1.get()=="" or t2.get()=="" or t3.get()==""):
       tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
   else:
       list1=[]
       d=["1","2","3","4","5","6","7","8","9","0"]
       if(t1.get()==""):
           tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
           u+=1
       else:
           list1.append(t1.get())
       if (t2.get() == ""):
           if(u==0):
               u+=1
               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
       else:
           num=t2.get()
           c=0
           if(len(num)==10):
               for i in num:
                   if(i not in d and u==0):
                      tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                      c+=1
                      u+=1
                      break
               if(c==0):
                   list1.append(t2.get())
           else:
               if(u==0):
                   u+=1
                   tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
               
       if(t3.get()==""):
           if(u==0):
               u+=1
               tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
       else:
           try:
               da=t3.get()
               d1=dt.datetime.strptime(da,"%d/%m/%y")
               list1.append(da)
               
               z=yogaQuery.SelectQuerywithp(list1[0],list1[1],list1[2],"1") 
               if len(z)!=0:
                  tk.messagebox.showerror("Error","You have already assign yoga at this date!",parent=tp)
                  list1.pop(2)
               
           except:
               if(u==0):
                   u+=1
                   tk.messagebox.showerror("Error","Please fill the Date correctly!",parent=tp)
    
       r=yogaQuery.SelectQuerywithp(list1[0],list1[1],list1[2],"2")
       if len(r)>0:    
          if len(q1)>0:
             for i in range(len(q1)):
                yogaQuery.InsertQuerywithp(list1[0],list1[1],list1[2],q1[i],"1")
             yogaQuery.InsertQuerywithp(list1[0],list1[1],list1[2],len(q1),"2")
             tk.messagebox.showinfo("YOGA ASSIGNED","Patient Yoga has been assigned successfully!",parent=tp)
             clears(t1,t2,t3)
             listBox5.delete(*listBox5.get_children())
             mycursor=yogaQuery.SelectQuery("3")
             for i in mycursor:
                 listBox5.insert("", "end", values=i)
          else:
             tk.messagebox.showerror("Error","No yoga images Assigned!",parent=tp)
       else:
          tk.messagebox.showerror("Error","Please create Patient History First!",parent=tp)
