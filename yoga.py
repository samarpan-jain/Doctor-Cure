from tkinter import messagebox
import datetime as dt
import tkinter.ttk as tt
import tkinter as tk
import yogaQuery
import AssignYoga

t1,t2,t3,listBox5,option6,k1,k,w=None,None,None,None,None,None,None,None
yogaQuery.YogaTableInitialize()

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

def yogahere(screen8):
  def menueyoga(t):
        def onclosing():
            t.destroy()
            
        #Menue Bar
        menubar=tk.Menu(t)
        t.config(menu=menubar)
        #Sub Menue
        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=submenu)
        submenu.add_command(label="Exit",command=onclosing)

        def aboutus():
            messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=submenu)
        submenu.add_command(label="About Us",command=aboutus)

        t.protocol("WM_DELETE_WINDOW",onclosing)
  
  root1=tk.Toplevel(screen8)
  x, y = root1.winfo_screenwidth(), root1.winfo_screenheight()
  root1.geometry("%dx%d+0+0" % (x, y))
  root1.title("DOCTOR CURE : PATIENT YOGA")
  root1.iconbitmap(r"images/logo.ico")

  def toplevel1_yoga(top1):
      global listBox5,option6,k1,k   
      def onclosing():
         pic.withdraw()
         
      def onclosing1():
         ypic.withdraw()

      def onclosings():
         top1.withdraw()
         pic.withdraw()

      pic = tk.Toplevel(root1)
      pic.title("DOCTOR CURE: ASSIGN YOGA")
      pic.withdraw()
      pic.protocol("WM_DELETE_WINDOW",onclosing)

      x, y = pic.winfo_screenwidth(), pic.winfo_screenheight()
      pic.geometry("%dx%d+0+0" % (x, y))

      def _on_mousewheel(event):
          canvas.yview_scroll(int(-1*(event.delta/120)),"units")

      container = tt.Frame(pic,height=y,width=x-25)
      canvas = tk.Canvas(container,height=y,width=x-25)
      scrollbar = tt.Scrollbar(container, orient="vertical", command=canvas.yview)
      scrollbar1 = tt.Scrollbar(container, orient="horizontal", command=canvas.xview)
      canvas.bind_all("<MouseWheel>",_on_mousewheel)
      
      top = tt.Frame(canvas)
      top.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

      canvas.create_window((0, 0), window=top, anchor="nw")
      canvas.configure(yscrollcommand=scrollbar.set)
      canvas.configure(xscrollcommand=scrollbar1.set)

      container.pack()
      canvas.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")
      scrollbar1.place(relx=0.001, rely=0.977, relheight=0.025, relwidth=0.989)

      imgl=[]
      for i in range(1,41):
          img =tk.PhotoImage(file="images/"+str(i)+".png")
          imgl.append(img)  
      
      menueyoga(top1)
      k1 = tk.StringVar()
      option6 = tk.StringVar()
      Label1 = tk.Label(top1)
      Label1.place(relx=0.375, rely=0.019, height=79, width=492)
      Label1.configure(font="-family {Palatino Linotype} -size 26 -weight bold")
      Label1.configure(text='''YOGA ASSIGNED PATIENTS''')

      Label2 = tk.Label(top1)
      Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
      Label2.configure(font="-family {Palatino Linotype} -size 17")
      Label2.configure(text='''TYPE TO SEARCH -:''')

      Entry1 = tk.Entry(top1,textvariable=k1)
      Entry1.place(relx=0.195, rely=0.125, height=40, relwidth=0.241)
      Entry1.configure(background="white")
      Entry1.configure(disabledforeground="#a3a3a3")
      Entry1.configure(font="-family {Palatino Linotype} -size 15")
      Entry1.configure(foreground="#000000")
      Entry1.configure(highlightbackground="#d9d9d9")
      Entry1.configure(highlightcolor="black")
      Entry1.configure(insertbackground="black")
      Entry1.configure(selectbackground="#c4c4c4")
      Entry1.configure(selectforeground="black")

      TCombobox1 = tt.Combobox(top1, textvariable=option6,state='readonly')
      value_list = ['All Records','Name of Patient','Phone Number','Date']
      TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
      TCombobox1.configure(values=value_list)
      TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
      option6.set("Choose Category to Search")

      cols = ('Name of Patient','Phone Number','Date of yoga assigning','No of Yoga Assigned')
      listBox5 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
      for col in cols:
          listBox5.heading(col, text=col)
      listBox5.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
      vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox5.xview)
      vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
      listBox5.configure(xscrollcommand=vsb.set)

      vsb = tt.Scrollbar(top1, orient="vertical", command=listBox5.yview)
      vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
      listBox5.configure(yscrollcommand=vsb.set)

      Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_yoga_btn())
      Button2.place(relx=0.100, rely=0.867, height=60, width=250)
      Button2.configure(font="-family {Palatino Linotype} -size 16")
      Button2.configure(foreground="#000000")
      Button2.configure(highlightbackground="#d9d9d9")
      Button2.configure(highlightcolor="black")
      Button2.configure(pady="0")
      Button2.configure(text='''SEARCH''')

      Button3 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:AssignYoga.yoga(top,pic,imgl,t1,t2,t3,listBox5))
      Button3.place(relx=0.315, rely=0.867, height=60, width=250)
      Button3.configure(font="-family {Palatino Linotype} -size 16")
      Button3.configure(foreground="#000000")
      Button3.configure(highlightcolor="black")
      Button3.configure(highlightbackground="#d9d9d9")
      Button3.configure(pady="0")
      Button3.configure(text='''ASSIGN YOGA''')

      Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_yoga_patient(top1))
      Button4.place(relx=0.527, rely=0.867, height=60, width=250)
      Button4.configure(font="-family {Palatino Linotype} -size 14")
      Button4.configure(foreground="#000000")
      Button4.configure(highlightbackground="#d9d9d9")
      Button4.configure(highlightcolor="black")
      Button4.configure(pady="0")
      Button4.configure(text='''DELETE YOGA PATIENT''')

      selected_items = listBox5.selection()
      cur_item=listBox5.focus()
      k=listBox5.item(cur_item)["values"]

      Button5 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:yoga_view_btn())
      Button5.place(relx=0.745, rely=0.867, height=60, width=250)
      Button5.configure(font="-family {Palatino Linotype} -size 14")
      Button5.configure(foreground="#000000")
      Button5.configure(highlightbackground="#d9d9d9")
      Button5.configure(highlightcolor="black")
      Button5.configure(pady="0")
      Button5.configure(text='''VIEW ASSIGNED YOGA''')

      listBox5.delete(*listBox5.get_children())
      mycursor=yogaQuery.SelectQuery("1")
      for i in mycursor:
          listBox5.insert("", "end", values=i)

      top1.protocol("WM_DELETE_WINDOW",onclosings)
   
    
  def delete_yoga_patient(tp):
      global listBox5
      try:
          MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
          if MsgBox == "yes":
              selected_items = listBox5.selection()
              cur_item=listBox5.focus()
              k=listBox5.item(cur_item)["values"]
              yogaQuery.DeleteQuerywithp(str(k[0]),str(k[1]),str(k[2]),str(k[3]))
              for selected_item in selected_items:
                  listBox5.delete(selected_item)
          else:
              pass
      except:
          pass
      
  def search_yoga_btn():
      global listBox5,option6,k1
      _entry = k1.get()
      _option = option6.get()

      if (_option == 'Name of Patient'):
          listBox5.delete(*listBox5.get_children())
          mycursor=yogaQuery.SelectQuery("4",_entry)
          for i in mycursor:
              listBox5.insert("", "end", values=i)
              
      elif (_option == 'Phone Number'):
          listBox5.delete(*listBox5.get_children())
          mycursor=yogaQuery.SelectQuery("5",_entry)
          for i in mycursor:
              listBox5.insert("", "end", values=i)
              
      elif (_option == 'Date'):
          listBox5.delete(*listBox5.get_children())
          mycursor=yogaQuery.SelectQuery("6",_entry)
          for i in mycursor:
              listBox5.insert("", "end", values=i)
     
      elif (_option == "All Records"):
          listBox5.delete(*listBox5.get_children())
          mycursor=yogaQuery.SelectQuery("1")
          for i in mycursor:
              listBox5.insert("", "end", values=i)     
      else:
          option6.set("Choose Category Correctly!")
          
  def yoga_view_btn():
    global listBox5,k,w
    def onclosing1():
         ypic.withdraw()
         
    ypic = tk.Toplevel(root1)
    ypic.title("DOCTOR CURE: VIEW YOGA")
    ypic.withdraw()
    ypic.protocol("WM_DELETE_WINDOW",onclosing1)
    ypic.geometry("350x500+200+200")
    container1 = tt.Frame(ypic)
    canvas1 = tk.Canvas(container1)
    scrollbar = tt.Scrollbar(container1, orient="vertical", command=canvas1.yview)
    scrollable_frame = tt.Frame(canvas1)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas1.configure(
            scrollregion=canvas1.bbox("all")
        )
    )

    canvas1.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas1.configure(yscrollcommand=scrollbar.set)
    container1.pack()
    canvas1.pack(side="left", fill="both", expand=True)
    canvas1.configure(height=500,width=325)
    scrollbar.pack(side="right", fill="y")
    
    selected_items = listBox5.selection()
    cur_item=listBox5.focus()
    k=listBox5.item(cur_item)["values"]
    
    if len(k)>0:
        x=yogaQuery.SelectQuerywithp(k[0],k[1],k[2],"3")
        w=[]
        for g in x:
          img =tk.PhotoImage(file=g[0])
          w.append(img)
          
        view_yoga(scrollable_frame,ypic)
    else:
      tk.messagebox.showerror("Error","Please choose a record to View",parent=root1)

  def view_yoga(tops,top1):
    global listBox5,k,w

    def onclosings():
      top1.destroy()
      
    top1.deiconify()
    top1.resizable(0,0)
    
    Label1 = tk.Label(tops)
    Label1.grid(row=0,column=0)
    Label1.configure(font="-family {Palatino Linotype} -size 18")
    Label1.configure(text="VIEW ASSIGNED YOGA")
    
    for g in range(len(w)):
      Img=tk.Label(tops,image=w[g])
      Img.grid(row=g+1,column=0,pady=10)
      
    top1.protocol("WM_DELETE_WINDOW",onclosings) 
   
  toplevel1_yoga(root1)
