from tkinter import messagebox
import datetime as dt
from tkinter import filedialog
import tkinter.ttk as tt
import tkinter as tk
import pandas as pd
import dietQuery

listBox,option3,r3,r2,listBox1,r1,r4,option1,fname4,fg,Quantity1,Dimension1,Timetoeat,option2,listBox2,option4=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
fname2,fg1,Quantity2,Dimension2,Timetoeat1,listBox3,option5,r4,r5,g1,g2,g3,g4=None,None,None,None,None,None,None,None,None,None,None,None,None

df=pd.read_pickle("MyFood1")
dietQuery.initialize(0)

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

def diet1(screen8):        
    root=tk.Toplevel(screen8)   
    x, y = root.winfo_screenwidth(), root.winfo_screenheight()
    root.config(bg="#d6e0f0")
    root.geometry("%dx%d+0+0" % (x, y))
    root.title("DOCTOR CURE : Patient Diet")
    root.iconbitmap(r"images/logo.ico")

    CD=tk.Toplevel(root)
    CD.title("DOCTORCURE: RECOMMENDED DIET")

    cd = tk.Toplevel(root)
    cd.title("DOCTORCURE: CREATE DIET")

    VD=tk.Toplevel(root)
    VD.title("DOCTORCURE: VIEW DIET")

    def clear4():
        r1.set("")
        r2.set("")
        r4.set("")

    def clear3():
        fname4.set("")
        fg.set("")
        Quantity1.set("")
        Dimension1.set("")
        Timetoeat.set("")

    def clear2():
        r6.set("")
        r11.set("")
        r12.set("")

    def clear1():
        fname2.set("")
        fg1.set("")
        Quantity2.set("")
        Dimension2.set("")
        Timetoeat1.set("")

    def menue(t):
        global df
        def onclosing():
            root.destroy()
            df.to_pickle("MyFood1")
        t.deiconify()
        t.iconbitmap(r"images/logo.ico")
        t.config(bg="#d6e0f0")
        x, y = t.winfo_screenwidth(),t.winfo_screenheight()
        t.geometry("%dx%d+0+0" % (x, y))
        t.resizable(1, 1)

        if t!=cd and t!=CD and t!=VD:        
            cd.withdraw()
            CD.withdraw()
            VD.withdraw()
        elif t!=cd and t!=root and t!=CD:
            root.withdraw()
            cd.withdraw()
            CD.withdraw()
        elif t!=cd and t!=root and t!=VD:
            root.withdraw()
            cd.withdraw()
            VD.withdraw()
        else:
            root.withdraw()
            CD.withdraw()
            VD.withdraw()
        
        #Menue Bar
        menubar=tk.Menu(t)
        t.config(menu=menubar)
        #Sub Menue
        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=submenu)
        submenu.add_command(label="Exit",command=onclosing)

        submenu=tk.Menu(menubar,tearoff=0)
        #menubar.add_cascade(label="Edit",menu=submenu)
        #submenu.add_command(label="Dashboard",command=session)
        #submenu.add_command(label="Patient History",command=Record)
        #submenu.add_command(label="Patient Medicine",command=medicine)
        #submenu.add_command(label="Patient Diet",command=lambda:toplevel1(root))
        #submenu.add_command(label="Patient Yoga",command=yogahere)
        def aboutus():
            messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=submenu)
        submenu.add_command(label="About Us",command=aboutus)

        t.protocol("WM_DELETE_WINDOW",onclosing)
        
    ###################################################################################Main Diet Screen####################################################################################################
        
    def toplevel1(top1):
        global listBox,option3,r3,df
        menue(top1)
        top1.config(bg="#d6e0f0")
        r3 = tk.StringVar()
        option3 = tk.StringVar()
        Label1 = tk.Label(top1)
        Label1.place(relx=0.375, rely=0.019, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold")
        Label1.configure(text='''PATIENT DIET''',bg='#d6e0f0',fg='black')

        Label2 = tk.Label(top1)
        Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17")
        Label2.configure(text='''TYPE TO SEARCH -:''',bg='#d6e0f0',fg='black')

        Entry1 = tk.Entry(top1,textvariable=r3)
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

        TCombobox1 = tt.Combobox(top1, textvariable=option3,state='readonly')
        value_list = ['All Records', "Name of food Items","Food Group","Calories","Fat (g)", "Protein (g)","Carbohydrate (g)","Sugars (g)","Fiber (g)","Cholesterol (mg)","Calcium (mg)","Iron, Fe (mg)","Potassium, K (mg)"]
        TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
        option3.set("Choose Category to Search")

        
        cols = ("Name of food Items","Food Group","Calories","Fat (g)", "Protein (g)","Carbohydrate (g)","Sugars (g)","Fiber (g)","Cholesterol (mg)","Saturated Fats (g)","Calcium (mg)","Iron, Fe (mg)","Potassium, K (mg)","Magnesium (mg)","Vitamin A, IU (IU)", "Vitamin A, RAE (mcg)", "Vitamin C (mg)","Vitamin B-12 (mcg)","Vitamin D (mcg)","Vitamin E (Alpha-Tocopherol) (mg)", "Net-Carbs (g)","Water (g)","Omega 3s (mg)","Omega 6s (mg)","PRAL score ()","Trans Fatty Acids (g)","Sucrose (g)","Glucose (Dextrose) (g)","Fructose (g)","Lactose (g)","Maltose (g)","Galactose (g)","Starch (g)","Phosphorus, P (mg)","Sodium (mg)","Zinc, Zn (mg)", "Copper, Cu (mg)","Manganese (mg)","Selenium, Se (mcg)" ,"Fluoride, F (mcg)","Thiamin (B1) (mg)","Riboflavin (B2) (mg)", "Niacin (B3) (mg)", "Pantothenic acid (B5) (mg)","Vitamin B6 (mg)", "Folate (B9) (mcg)","Folic acid (mcg)", "Food Folate (mcg)","Folate DFE (mcg)", "Choline (mg)","Vitamin D3 (cholecalciferol) (mcg)","Vitamin D (IU) (IU)", "Vitamin K (mcg)","Dihydrophylloquinone (mcg)", "Fatty acids, total monounsaturated (mg)","Fatty acids, total polyunsaturated (mg)","Stigmasterol (mg)","Campesterol (mg)", "Beta-sitosterol (mg)", "Fatty acids, total trans-monoenoic (mg)","Fatty acids, total trans-polyenoic (mg)","Tryptophan (mg)","Threonine (mg)", "Isoleucine (mg)","Leucine (mg)","Lysine (mg)", "Methionine (mg)","Cystine (mg)","Phenylalanine (mg)",  "Tyrosine (mg)","Valine (mg)",  "Alanine (mg)", "Aspartic acid (mg)",  "Glutamic acid (mg)","Glycine (mg)",	"Hydroxyproline (mg)","Alcohol (g)","Caffeine (mg)","Theobromine (mg)",	"200 Calorie Weight (g)")
        listBox = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
        listBox.configure(xscrollcommand=vsb.set)

        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox.yview)
        vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
        listBox.configure(yscrollcommand=vsb.set)

        Button1 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_btn())
        Button1.place(relx=0.021, rely=0.867, height=60, width=250)
        Button1.configure(font="-family {Palatino Linotype} -size 16")
        Button1.configure(foreground="#000000")
        Button1.configure(pady="0")
        Button1.configure(text='''SEARCH''')

        Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:toplevel2(cd))
        Button2.place(relx=0.200, rely=0.867, height=60, width=250)
        Button2.configure(font="-family {Palatino Linotype} -size 16")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''CUSTOM DIET''')

        Button3 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_btn(top1))
        Button3.place(relx=0.415, rely=0.867, height=60, width=250)
        Button3.configure(font="-family {Palatino Linotype} -size 16")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''DELETE''')

        Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:viewdiet(VD))
        Button4.place(relx=0.627, rely=0.867, height=60, width=250)
        Button4.configure(font="-family {Palatino Linotype} -size 14")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''VIEW ALL PATIENT DIET''')

        Button5 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:commondiet(CD))
        Button5.place(relx=0.809, rely=0.867, height=60, width=250)
        Button5.configure(font="-family {Palatino Linotype} -size 14")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text='''RECOMMENDED DIET''')

        k=df.values.tolist()

        for i in range(50):
            listBox.insert("", "end", values=k[i])
          
    def delete_btn(tp):
        
        global listBox,df
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
        if MsgBox == "yes":
            selected_items = listBox.selection()
            cur_item=listBox.focus()
            k=listBox.item(cur_item)["values"]
            df=df[df["Name"]!= str(k[0]).upper()]        
            k1=df.values.tolist()
            listBox.delete(*listBox.get_children())
            for i in range(50):
                listBox.insert("", "end", values=k1[i])
        else:
            pass
        
        
    def search_btn():
        global listBox,option3,r3,df,p,k
        _entry = r3.get()
        _option = option3.get()

        if (_option == 'Name of food Items'):
            listBox.delete(*listBox.get_children())
            p=df[df['Name'].str.contains(_entry.upper())]
            m=p.values.tolist()
            for i in m:
                listBox.insert("", "end", values=i)
               
        elif (_option == 'Food Group'):
            listBox.delete(*listBox.get_children())
            p=df[df['FoodGroup'].str.contains(_entry.upper())]
            m=p.values.tolist()
            for i in m:
                listBox.insert("", "end", values=i)
                
        elif (_option == "Calories"):
            listBox.delete(*listBox.get_children())
            z=df[df["Calories"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Fat (g)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Fat"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Protein (g)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Protein"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Carbohydrate (g)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Carbohydrate"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Sugars (g)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Sugars"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Fiber (g)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Fiber"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Cholesterol (mg)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Cholesterol"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Calcium (mg)'):
            listBox.delete(*listBox.get_children())
            z=df[df["Calcium"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Iron, Fe (mg)'):
            listBox.delete(*listBox.get_children())
            z=df[df["IronFe"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == 'Potassium, K (mg)'):
            listBox.delete(*listBox.get_children())
            z=df[df["PotassiumK"]== float(_entry)].values.tolist()
            for i in z:
                listBox.insert("", "end", values=i)
                
        elif (_option == "All Records"):
            listBox.delete(*listBox.get_children())
            for i in range(len(k)):
                listBox.insert("", "end", values=k[i])  
        else:
            option3.set("Choose Category Correctly!")

    ###################################################################################Personal Diet####################################################################################################
    def toplevel2(top2):
        global listBox2,r1,r2,r4
        top2.config(bg="#d6e0f0")
        top2.iconbitmap(r"images/logo.ico")
        x, y = root.winfo_screenwidth(), root.winfo_screenheight()
        top2.geometry("%dx%d+0+0" % (x, y))
        top2.deiconify()

        def onclosings():
            dietQuery.droptable()
            top2.withdraw()
            Add2.withdraw()
            Mdd1.withdraw()
            sug1.withdraw()

        def onclosing():
            clear1()
            Add2.withdraw()

        def onclosings1():
            Mdd1.withdraw()

        def onclosings2():
            sug1.withdraw()

        Add2 = tk.Toplevel(cd)
        Add2.config(bg='#d6e0f0')
        Add2.title("DOCTOR CURE: ADD TO PATIENT DIET")
        Add2.withdraw()
        Add2.protocol("WM_DELETE_WINDOW",onclosing)

        container = tt.Frame(Add2)
        canvas = tk.Canvas(container,height=500,width=450)
        scrollbar = tt.Scrollbar(container, orient="vertical", command=canvas.yview)
        top = tt.Frame(canvas)

        top.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=top, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        Mdd1 = tk.Toplevel(cd)
        Mdd1.title("STOCK UP: MODIFY ENTRY")
        Mdd1.withdraw()
        Mdd1.protocol("WM_DELETE_WINDOW",onclosings1)

        sug1 = tk.Toplevel(cd)
        sug1.title("STOCK UP: FOOD ITEMS SUGGESTIONS")
        sug1.withdraw()
        sug1.protocol("WM_DELETE_WINDOW",onclosings2)
        
        Label1 = tk.Label(top2)
        Label1.place(relx=0.375, rely=0.009, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold",bg='#d6e0f0',fg='black')
        Label1.configure(text='''CREATE DIET''')

        Label2 = tk.Label(top2)
        Label2.place(relx=0.001, rely=0.095, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label2.configure(text='''NAME -:''')
        
        r1 = tk.StringVar()
        Entry1 = tk.Entry(top,width=28, textvariable=fname2)
        Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg1)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
        Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        Entry1 = tk.Entry(top2,textvariable=r1)
        Entry1.place(relx=0.155, rely=0.095, height=30, relwidth=0.211)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="-family {Palatino Linotype} -size 15")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")

        Label4 = tk.Label(top2)
        Label4.place(relx=0.035, rely=0.145, height=40, relwidth=0.241)
        Label4.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label4.configure(text='''DATE(dd/mm/yy) -:''')
        
        r4 = tk.StringVar()
        Entry4 = tk.Entry(top2,textvariable=r4)
        Entry4.place(relx=0.225, rely=0.145, height=30, relwidth=0.141)
        Entry4.configure(background="white")
        Entry4.configure(disabledforeground="#a3a3a3")
        Entry4.configure(font="-family {Palatino Linotype} -size 15")
        Entry4.configure(foreground="#000000")
        Entry4.configure(highlightbackground="#d9d9d9")
        Entry4.configure(highlightcolor="black")
        Entry4.configure(insertbackground="black")
        Entry4.configure(selectbackground="#c4c4c4")
        Entry4.configure(selectforeground="black")

        Label3 = tk.Label(top2)
        Label3.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        Label3.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label3.configure(text='''PH.NO -:''')

        r2 = tk.StringVar()
        Entry2 = tk.Entry(top2,textvariable=r2)
        Entry2.place(relx=0.735, rely=0.125, relheight=0.049, relwidth=0.169)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="-family {Palatino Linotype} -size 15")
        Entry2.configure(foreground="#000000")
        Entry2.configure(highlightbackground="#d9d9d9")
        Entry2.configure(highlightcolor="black")
        Entry2.configure(insertbackground="black")
        Entry2.configure(selectbackground="#c4c4c4")
        Entry2.configure(selectforeground="black")
        
        cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
        listBox2 = tt.Treeview(top2, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox2.heading(col, text=col)
        listBox2.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.627)
        vsb = tt.Scrollbar(top2, orient="horizontal", command=listBox2.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.627)
        listBox2.configure(xscrollcommand=vsb.set)

        vsb1 = tt.Scrollbar(top2, orient="vertical", command=listBox2.yview)
        vsb1.place(relx=0.674, rely=0.216, relheight=0.580, relwidth=0.012)
        listBox2.configure(yscrollcommand=vsb1.set)

        sbframe=tk.Frame(top2)
        sbframe.config(bg='#d6e0f0')
        sbframe.place(relx=0.748, rely=0.224, relheight=0.669, relwidth=0.179)

        Button1 = HoverButton(sbframe,padx=98,pady=5,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:add_btn(top,Add2))
        Button1.pack(side="top",pady=15)
        Button1.configure(font="-family {Palatino Linotype} -size 12 -weight bold")
        Button1.configure(foreground="#000000")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(text='''ADD FOOD ITEM''')

        Button2 = HoverButton(sbframe,padx=110,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:delete_btn2())
        Button2.pack(side="top",pady=15)
        Button2.configure(font="-family {Palatino Linotype} -size 14 ")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''DELETE''')

        Button3 = HoverButton(sbframe,padx=100,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:modi_btn(Mdd1))
        Button3.pack(side="top",pady=25) 
        Button3.configure(font="-family {Palatino Linotype} -size 15 ")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''MODIFY''')

        Button4 = HoverButton(sbframe,padx=99,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:Assign1(top2))
        Button4.pack(side="top",pady=15)
        Button4.configure(font="-family {Palatino Linotype} -size 14 ")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''SAVE AND ASSIGN''')

        Button5 = HoverButton(sbframe,padx=72,pady=20,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:Suggestions(sug1))
        Button5.pack(side="top",pady=15)
        Button5.configure(font="-family {Palatino Linotype} -size 14")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text='''DIET SUGGESTIONS''')
        
        try:
            t=dietQuery.selectQuery(1)
            r1.set(t[0])
            r4.set(t[3])
            r2.set(t[4])
        except:
            pass

        top2.protocol("WM_DELETE_WINDOW",onclosings)

    def add_btn(top,top1):
        dietQuery.initialize(1)
        top1.deiconify()
        top1.geometry("470x500")

        global fname2,fg1,Quantity2,Dimension2,Timetoeat1
        
        def onclosing():
            clear1()
            top1.withdraw()

        fname2=tk.StringVar()
        fg1=tk.StringVar()
        Quantity2=tk.StringVar()
        Dimension2=tk.StringVar()
        Timetoeat1=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Diet Record Entry")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        Entry1 = tk.Entry(top,width=28, textvariable=fname2)
        Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg1)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
        Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat1)
        Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:saveadd2(top1))
        button6.grid(row=8,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=onclosing)
        button7.grid(row=8,column=0,pady=20)

    def saveadd2(tp):
        try:
            global fname2,fg1,Quantity2,Dimension2,Timetoeat1,listBox2
            
            if (fname2.get() == "" or fg1.get() == "" or Quantity2.get() == "" or Dimension2.get() == "" or Timetoeat1.get() == ""):
                clear1()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                if(fname2.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fname2.get())
                if (fg1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fg1.get())
                if (Quantity2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    num=Quantity2.get()
                    if(num.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                    else:
                        list1.append(num)
                if (Dimension2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Dimension2.get())
                if (Timetoeat1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    num2=Timetoeat1.get()
                    list1.append(num2)
                x1=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],1)
                if len(x1)==0:
                    dietQuery.insertQuery(list1[0],list1[1],list1[2],list1[3],list1[4],1)
                    clear1()
                    tp.withdraw()
                else:
                    tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)
                    
            listBox2.delete(*listBox2.get_children())
            mycursor=dietQuery.selectQuery(2)
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        except:
            pass

    def delete_btn2():
        global listBox2
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=cd)
            if MsgBox == "yes":
                selected_items = listBox2.selection()
                cur_item=listBox2.focus()
                k=listBox2.item(cur_item)["values"]
                dietQuery.deleteQuery(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),1)
                for selected_item in selected_items:
                    listBox2.delete(selected_item)
            else:
                pass
        except:
            pass

    def modi_btn(top):
        global listBox2
        selected_items1 = listBox2.selection()
        cur_item1=listBox2.focus()
        k=listBox2.item(cur_item1)["values"]
        if(len(k)==0):
            tk.messagebox.showerror("No Record Selected","Please select a record to Modify",parent=top)
        else:
            def onclosing():
                top.withdraw()
                
            global  fname2,fg1,Quantity2,Dimension2,Timetoeat1
            
            top.deiconify()
            top.geometry("500x550")
            
            fname2 = tk.StringVar()
            fg1 =tk.StringVar()
            Quantity2=tk.StringVar()
            Dimension2=tk.StringVar()
            Timetoeat1=tk.StringVar()

            Label2 = tk.Label(top)
            Label2.grid(row=0,column=1,pady=20,sticky="nw")
            Label2.configure(font="-family {Palatino Linotype} -size 18",bg='#d6e0f0',fg='black')
            Label2.configure(text="Record Entry")

            Label2 = tk.Label(top)
            Label2.grid(row=2,column=0,pady=20,sticky="w")
            Label2.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2.configure(text="SR.NO")

            Label2_1 = tk.Label(top)
            Label2_1.grid(row=3,column=0,pady=20,sticky="w")
            Label2_1.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2_1.configure(text="PRODUCT NAME")

            Label2_2 = tk.Label(top)
            Label2_2.grid(row=4,column=0,pady=20,sticky="w")
            Label2_2.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2_2.configure(text="QUANTITY")
            
            Label3 = tk.Label(top)
            Label3.grid(row=5,column=0,pady=20,sticky="w")
            Label3.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label3.configure(text="MEASUREMENT")

            Label3_5 = tk.Label(top)
            Label3_5.grid(row=6,column=0,pady=20,sticky="w")
            Label3_5.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label3_5.configure(text="PRICE INVESTED")

            Entry1 = tk.Entry(top,width=28, textvariable=fname2)
            Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
            Entry1.configure(font="-family {Palatino Linotype} -size 12")

            Entry2 = tk.Entry(top,width=28, textvariable=fg1)
            Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
            Entry2.configure(font="-family {Palatino Linotype} -size 12")

            Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
            Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
            Entry3.configure(font="-family {Palatino Linotype} -size 12")

            Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
            Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
            Entry4.configure(font="-family {Palatino Linotype} -size 12")

            Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat1)
            Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
            Entry5.configure(font="-family {Palatino Linotype} -size 12")
            

            button6=HoverButton(top,text="SAVE",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:savemodi2(k,top))
            button6.grid(row=7,column=1,pady=20)

            button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:onclosing())
            button7.grid(row=7,column=0,pady=20)

            fname2.set(k[0])
            fg1.set(k[1])
            Quantity2.set(k[2])
            Dimension2.set(k[3])
            Timetoeat1.set(k[4])

    def savemodi2(k3,top2):
        global listBox2,fname2,fg1,Quantity2,Dimension2,Timetoeat1
        
        try:
            if (fname2.get() == "" or fg1.get() == "" or Quantity2.get() == "" or Dimension2.get() == "" or Timetoeat1.get() == ""):
                clear1()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
            else:
                list1=[]
                if(fname2.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(fname2.get())
                if (fg1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(fg1.get())
                if (Quantity2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    num=Quantity2.get()
                    if(num.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                    else:
                        list1.append(num)
                if (Dimension2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(Dimension2.get())
                if (Timetoeat1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    num2=Timetoeat1.get()
                    list1.append(num2)
                
                x1=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],1)
                
                if len(x1)==0:
                    dietQuery.updateQuery(list1[0],list1[1],list1[2],list1[3],list1[4],k3[0],k3[1],k3[2],k3[3],k3[4],1)
                    top2.withdraw()
                else:
                    tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=top2)
                        
                listBox2.delete(*listBox2.get_children())
                mycursor=dietQuery.selectQuery(2)
                for i in mycursor:
                    listBox2.insert("", "end", values=i)
        except:
            pass

    def Assign1(tp):
        try:
            global r1,r2,r4
            u=0
            if r1.get()=="" or r2.get()=="" or r4.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r1.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r1.get())
                if (r2.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r2.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r2.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r4.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:            
                        da=r4.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=dietQuery.selectQuery2(list1[0],list1[1],list1[2],1)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                        
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill all Date correctly!",parent=tp)

                r=dietQuery.selectQuery2(list1[0],list1[1],list1[2],2)
                if len(r)>0:
                    m=dietQuery.selectQuery(3)
                    if len(m)>0:
                        for i in m:
                            dietQuery.insertQuery1(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4],1)
                            
                        o=dietQuery.selectQuery2(list1[0],list1[1],list1[2],3)
                        dietQuery.insertQuery(list1[0],list1[1],list1[2],o[0][0],o[1][0],2)
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        clear4()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
        except:
            pass
       
       
    #########################################################################################common diet################################################################################################        
    def commondiet(top1):
        top1.config(bg="#d6e0f0")
        top1.iconbitmap(r"images/logo.ico")
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        top1.deiconify()

        def onclosings():
            top1.withdraw()
            Add1.withdraw()
            Mdd.withdraw()
            sug.withdraw()
            Ass.withdraw()
            
        def onclosing():
            clear3()
            Add1.withdraw()

        def onclosings1():
            Mdd.withdraw()

        def onclosings2():
            sug.withdraw()

        def onclosing3():
            Ass.withdraw()
            
        global listBox1,r6,r7,r9,r10,r12,r11,option1

        Add1 = tk.Toplevel(CD)
        Add1.config(bg='#d6e0f0')
        Add1.title("DOCTOR CURE: ADD TO PATIENT DIET")
        Add1.withdraw()
        Add1.protocol("WM_DELETE_WINDOW",onclosing)

        Mdd = tk.Toplevel(CD)
        Mdd.title("DOCTOR CURE: MODIFY ENTRY")
        Mdd.withdraw()
        Mdd.protocol("WM_DELETE_WINDOW",onclosings1)

        sug = tk.Toplevel(CD)
        sug.title("DOCTOR CURE: FOOD ITEMS SUGGESTIONS")
        sug.withdraw()
        sug.protocol("WM_DELETE_WINDOW",onclosings2)

        Ass = tk.Toplevel(CD)
        Ass.title("DOCTOR CURE: Question")
        Ass.withdraw()
        Ass.protocol("WM_DELETE_WINDOW",onclosing3)
        
        l4=tk.Label(top1,text="RECOMMENDED DIET",font=("Palatino Linotype",35,"bold"),bg='#d6e0f0',fg='black')
        l4.place(relx=0.365, rely=0.019, height=79, width=525)

        option1 = tk.StringVar()
        TCombobox1 = tt.Combobox(top1, textvariable=option1,state='readonly')
        TCombobox1.bind("<<ComboboxSelected>>",getdiet1)
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.place(relx=0.005, rely=0.114, relheight=0.054, relwidth=0.172)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option1.set("Choose Patient Condition for Diet")
        
        cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
        
        listBox1 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse',height=25)
        listBox1.place(relx=0.005, rely=0.187, relheight=0.462, relwidth=0.750)
        for col in cols:
            listBox1.heading(col, text=col)

        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox1.xview)
        vsb.place(relx=0.005, rely=0.649, relheight=0.025, relwidth=0.750)
        listBox1.configure(xscrollcommand=vsb.set)
            
        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox1.yview)
        vsb.place(relx=0.755, rely=0.187, relheight=0.462, relwidth=0.012)
        listBox1.configure(yscrollcommand = vsb.set)

        l11=tk.Label(top1,text="FILL DETAILS TO ASSIGN DIET TO A PATIENT -:",font=("Palatino Linotype",18,"bold"),bg='#d6e0f0',fg='black')
        l11.place(relx=0.255, rely=0.700, relheight=0.031, relwidth=0.512)
        
        sbframe1=tk.Frame(top1)
        sbframe1.config(bg='#d6e0f0')
        sbframe1.place(relx=0.021, rely=0.777, height=40, width=2000)

        l8=tk.Label(sbframe1,text="NAME   :",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l8.pack(side="left")
        r6=tk.StringVar()
        Entry2=tk.Entry(sbframe1,width=28,textvariable=r6)
        Entry2.pack(side="left",padx=20)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="-family {Palatino Linotype} -size 15")
        Entry2.configure(foreground="#000000")
        Entry2.configure(highlightbackground="#d9d9d9")
        Entry2.configure(highlightcolor="black")
        Entry2.configure(insertbackground="black")
        Entry2.configure(selectbackground="#c4c4c4")
        Entry2.configure(selectforeground="black")

        l9=tk.Label(sbframe1,text="PHONE NO :",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l9.pack(side="left")
        r11=tk.StringVar()
        Entry3=tk.Entry(sbframe1,width=28,textvariable=r11)
        Entry3.pack(side="left",padx=20)
        Entry3.configure(background="white")
        Entry3.configure(disabledforeground="#a3a3a3")
        Entry3.configure(font="-family {Palatino Linotype} -size 15")
        Entry3.configure(foreground="#000000")
        Entry3.configure(highlightbackground="#d9d9d9")
        Entry3.configure(highlightcolor="black")
        Entry3.configure(insertbackground="black")
        Entry3.configure(selectbackground="#c4c4c4")
        Entry3.configure(selectforeground="black")

        l10=tk.Label(sbframe1,text="DATE(dd/mm/yy):",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l10.pack(side="left")
        r12=tk.StringVar()
        Entry4=tk.Entry(sbframe1,width=20,textvariable=r12)
        Entry4.pack(side="left",padx=20)
        Entry4.configure(background="white")
        Entry4.configure(disabledforeground="#a3a3a3")
        Entry4.configure(font="-family {Palatino Linotype} -size 15")
        Entry4.configure(foreground="#000000")
        Entry4.configure(highlightbackground="#d9d9d9")
        Entry4.configure(highlightcolor="black")
        Entry4.configure(insertbackground="black")
        Entry4.configure(selectbackground="#c4c4c4")
        Entry4.configure(selectforeground="black")
       
        sbframe=tk.Frame(top1)
        sbframe.config(bg='#d6e0f0')
        sbframe.place(relx=0.788, rely=0.190, relheight=0.547, relwidth=0.179)

        button1=HoverButton(sbframe,text="ADD FOOD ITEM",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=94,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:add_cmd_button(Add1))
        button1.pack(side="top",pady=10)

        button2=HoverButton(sbframe,text="DELETE",padx=110,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:delete_btn1())
        button2.pack(side="top",pady=10)

        button3=HoverButton(sbframe,text="MODIFY",padx=110,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:modi_cmd_button(Mdd))
        button3.pack(side="top",pady=10)

        button4=HoverButton(sbframe,text="ASSIGN DIET",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=92,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:Assign_cmd(Ass))
        button4.pack(side="top",pady=10)

        button6=HoverButton(sbframe,text="DIET SUGGESTIONS",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=67,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:Suggestions(sug))
        button6.pack(side="top",pady=10)
        
        try:
            t=dietQuery.selectQuery(1)
            r6.set(t[0])
            r12.set(t[3])
            r11.set(t[4])
        except:
            pass

        top1.protocol("WM_DELETE_WINDOW",onclosings)

    def add_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2
        def onclosing():
            clear3()
            top.withdraw()
        
        top.deiconify()
        top.geometry("460x600")

        fname4=tk.StringVar()
        fg=tk.StringVar()
        Quantity1=tk.StringVar()
        Dimension1=tk.StringVar()
        Timetoeat=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Diet Record Entry")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,pady=20,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Diet Type")

        Label2 = tk.Label(top)
        Label2.grid(row=3,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=4,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=5,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=6,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=7,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        option2 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option2.set("Choose Patient Condition for Diet")

        Entry1 = tk.Entry(top,width=28, textvariable=fname4)
        Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg)
        Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
        Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
        Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
        Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=lambda:saveadd1(top))
        button6.grid(row=9,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=onclosing)
        button7.grid(row=9,column=0,pady=20)


    def saveadd1(tp):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1,listbox1
        try:
       
            if (fname4.get() == "" or fg.get() == "" or Quantity1.get() == "" or Dimension1.get() == "" or Timetoeat.get() == ""):
                clear3()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                if(fname4.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fname4.get())
                if (fg.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fg.get())
                if (Quantity1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    f=[]
                    num2=Quantity1.get()
                    if(num2.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                    else:
                        list1.append(num2)
                if (Dimension1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Dimension1.get())
                if (Timetoeat.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Timetoeat.get())
                    
                if(option2.get()=="On Dialysis"):
                    p=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],2)
                    if len(p)==0:
                        dietQuery.insertQuery(list1[0],list1[1],list1[2],list1[3],list1[4],3)
                        clear3()
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)
                elif(option2.get()=="Not on Dialysis"):
                    p1=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],3)
                    if len(p1)==0:
                        dietQuery.insertQuery(list1[0],list1[1],list1[2],list1[3],list1[4],4)
                        clear3()
                    else:
                       tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)

                if(option1.get()=="On Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor=dietQuery.selectQuery(5)
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                        
                elif(option1.get()=="Not on Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor=dietQuery.selectQuery(6)
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                else:
                    pass

                tp.withdraw()
        except:
            pass
                
    def modi_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1
        def onclosing():
            clear3()
            top.withdraw()

        selected_items = listBox1.selection()
        cur_item=listBox1.focus()
        k=listBox1.item(cur_item)["values"]

        if len(k)>0:
            top.deiconify()
            top.geometry("460x600")

            fname4=tk.StringVar()
            fg=tk.StringVar()
            Quantity1=tk.StringVar()
            Dimension1=tk.StringVar()
            Timetoeat=tk.StringVar()

            Label2 = tk.Label(top)
            Label2.grid(row=0,column=1,pady=20,sticky="nw")
            Label2.configure(font="-family {Palatino Linotype} -size 18")
            Label2.configure(text="Diet Record Entery")

            Label1 = tk.Label(top)
            Label1.grid(row=2,column=0,pady=20,sticky="w")
            Label1.configure(font="-family {Palatino Linotype} -size 12")
            Label1.configure(text="Diet Type")

            Label2 = tk.Label(top)
            Label2.grid(row=3,column=0,pady=20,sticky="w")
            Label2.configure(font="-family {Palatino Linotype} -size 12")
            Label2.configure(text="Name of food Items")

            Label2_1 = tk.Label(top)
            Label2_1.grid(row=4,column=0,pady=20,sticky="w")
            Label2_1.configure(font="-family {Palatino Linotype} -size 12")
            Label2_1.configure(text="Food Group")

            Label2_2 = tk.Label(top)
            Label2_2.grid(row=5,column=0,pady=20,sticky="w")
            Label2_2.configure(font="-family {Palatino Linotype} -size 12")
            Label2_2.configure(text="Quantity")
            
            Label3 = tk.Label(top)
            Label3.grid(row=6,column=0,pady=20,sticky="w")
            Label3.configure(font="-family {Palatino Linotype} -size 12")
            Label3.configure(text="Dimensions")

            Label3_5 = tk.Label(top)
            Label3_5.grid(row=7,column=0,pady=20,sticky="w")
            Label3_5.configure(font="-family {Palatino Linotype} -size 12")
            Label3_5.configure(text="Time to eat")

            option2 = tk.StringVar()
            TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
            value_list = ["On Dialysis","Not on Dialysis"]
            TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
            TCombobox1.configure(values=value_list)
            TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
            option2.set("Choose Patient Condition for Diet")

            Entry1 = tk.Entry(top,width=28, textvariable=fname4)
            Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
            Entry1.configure(font="-family {Palatino Linotype} -size 12")
            
            Entry2 = tk.Entry(top,width=28, textvariable=fg)
            Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
            Entry2.configure(font="-family {Palatino Linotype} -size 12")

            Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
            Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
            Entry3.configure(font="-family {Palatino Linotype} -size 12")

            Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
            Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
            Entry4.configure(font="-family {Palatino Linotype} -size 12")
            
            Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
            Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
            Entry5.configure(font="-family {Palatino Linotype} -size 12")

            
            button6=HoverButton(top,text="MODIFY",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=lambda:savemodi1(top,k))
            button6.grid(row=9,column=1,pady=20)

            button7=HoverButton(top,text="CANCEL",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=onclosing)
            button7.grid(row=9,column=0,pady=20)

            if option1.get()=="On Dialysis":
                option2.set("On Dialysis")
                fname4.set(k[0])
                fg.set(k[1])
                Quantity1.set(str(k[2]))
                Dimension1.set(k[3])
                Timetoeat.set(k[4])
            elif option1.get()=="Not on Dialysis":
                option2.set("Not on Dialysis")
                fname4.set(k[0])
                fg.set(k[1])
                Quantity1.set(str(k[2]))
                Dimension1.set(k[3])
                Timetoeat.set(k[4])
            else:
                pass
            
        else:
            tk.messagebox.showerror("Error","Please choose an item to Modify",parent=CD)

    def savemodi1(tp1,k1):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1,listbox1
        
        try:
            if (fname4.get() == "" or fg.get() == "" or Quantity1.get() == "" or Dimension1.get() == "" or Timetoeat.get() == ""):
                messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
            else:
                list1=[]
                if(fname4.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(fname4.get())
                if (fg.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(fg.get())
                if (Quantity1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    f=[]
                    num2=Quantity1.get()
                    if(num2.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                    else:
                        list1.append(num2)
                if (Dimension1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(Dimension1.get())
                if (Timetoeat.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(Timetoeat.get())
                    
                if(option2.get()=="On Dialysis"):
                    p=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],2)
                    if len(p)==0:
                        dietQuery.updateQuery(list1[0],list1[1],list1[2],list1[3],list1[4],k1[0],k1[1],k1[2],k1[3],k1[4],2)
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp1)
                    
                elif(option2.get()=="Not on Dialysis"):
                    p1=dietQuery.selectQuery1(list1[0],list1[1],list1[2],list1[3],list1[4],3)
                    if len(p1)==0:
                        dietQuery.updateQuery(list1[0],list1[1],list1[2],list1[3],list1[4],k1[0],k1[1],k1[2],k1[3],k1[4],3)
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp1)
                else:
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)

                if(option1.get()=="On Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor=dietQuery.selectQuery(5)
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                        
                elif(option1.get()=="Not on Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor=dietQuery.selectQuery(6)
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                else:
                    pass

                tp1.withdraw()
        except:
            pass
        

    def delete_btn1():
        global listBox1,option1
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=CD)
            if MsgBox == "yes":
                selected_items = listBox1.selection()
                cur_item=listBox1.focus()
                k=listBox1.item(cur_item)["values"]
                
                if(option1.get()=="On Dialysis"):
                    a=dietQuery.selectQuery1(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),2)
                    if len(a)>0:
                        dietQuery.deleteQuery(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),3)
                        listBox1.delete(*listBox1.get_children())
                        mycursor=dietQuery.selectQuery(5)
                        for i in mycursor:
                            listBox1.insert("", "end", values=i)
                        conn.commit()
                        
                        
                    else:
                        tk.messagebox.showerror("Error","Choose Correct Patient Condition for Diet",parent=CD)
                        
                elif(option1.get()=="Not on Dialysis"):
                    a=dietQuery.selectQuery1(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),3)
                    if len(a)>0:
                        dietQuery.deleteQuery(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),4)
                        listBox1.delete(*listBox1.get_children())
                        mycursor=dietQuery.selectQuery(6)
                        for i in mycursor:
                            listBox1.insert("", "end", values=i)
                        conn.commit()
                        
                       
                    else:
                        tk.messagebox.showerror("Error","Choose Correct Patient Condition for Diet",parent=CD)
                else:
                    
                    pass
                    
            else:
                
                pass
        except:
            pass


    def add_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2
        def onclosing():
            clear3()
            top.withdraw()
        
        top.deiconify()
        top.geometry("460x600")

        fname4=tk.StringVar()
        fg=tk.StringVar()
        Quantity1=tk.StringVar()
        Dimension1=tk.StringVar()
        Timetoeat=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,pady=20,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Diet Type")

        Label2 = tk.Label(top)
        Label2.grid(row=3,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=4,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=5,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=6,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=7,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        option2 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option2.set("Choose Patient Condition for Diet")

        Entry1 = tk.Entry(top,width=28, textvariable=fname4)
        Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg)
        Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
        Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
        Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
        Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("Palatino Linotype",10,"bold"),command=lambda:saveadd1(top))
        button6.grid(row=9,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("Palatino Linotype",10,"bold"),command=onclosing)
        button7.grid(row=9,column=0,pady=20)

    def getdiet1(event):
        global listbox1,option1
        if(option1.get()=="On Dialysis"):
            listBox1.delete(*listBox1.get_children())
            mycursor=dietQuery.selectQuery(5)
            for i in mycursor:
                listBox1.insert("", "end", values=i)
                        
        elif(option1.get()=="Not on Dialysis"):
            listBox1.delete(*listBox1.get_children())
            mycursor=dietQuery.selectQuery(6)
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        else:
            pass

    def Suggestions(top):
        global option4,foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10
        top.geometry("480x600")
        top.deiconify()
        option4 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=30,textvariable=option4,state='readonly')
        value_list = ["High Protein Food Items","Low Protein Food Items","High Potassium Food Items","Low Potassium Food Items","High Phosphorus Food Items","Low Phosphorus Food Items"]
        TCombobox1.grid(row=1,column=0,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option4.set("Select type of Food Items to search")
        button1=tk.Button(top,text="Search",bd=2,bg="sky blue",fg="black",font=("Palatino Linotype",10,"bold"),padx=20,command=lambda:getsuggestion())
        button1.grid(row=1,column=0,padx=300,sticky="w")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,padx=20,pady=10,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Food Items")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,padx=260,pady=10,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Food Group")

        foodname1=tk.StringVar()
        foodname2= tk.StringVar()
        foodname3= tk.StringVar()
        foodname4= tk.StringVar()
        foodname5= tk.StringVar()
        foodname6= tk.StringVar()
        foodname7= tk.StringVar()
        foodname8= tk.StringVar()
        foodname9= tk.StringVar()
        foodname10= tk.StringVar()
        fgname1= tk.StringVar()
        fgname2= tk.StringVar()
        fgname3= tk.StringVar()
        fgname4= tk.StringVar()
        fgname5= tk.StringVar()
        fgname6= tk.StringVar()
        fgname7= tk.StringVar()
        fgname8= tk.StringVar()
        fgname9= tk.StringVar()
        fgname10= tk.StringVar()
        

        Entry1 = tk.Entry(top,width=28, textvariable=foodname1,state="readonly",readonlybackground="white")
        Entry1.grid(row=3,column=0,padx=20,pady=10,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 10")

        Entry2 = tk.Entry(top,width=28, textvariable=fgname1,state="readonly",readonlybackground="white")
        Entry2.grid(row=3,column=0,padx=260,pady=10,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 10")

        Entry3 = tk.Entry(top,width=28, textvariable=foodname2,state="readonly",readonlybackground="white")
        Entry3.grid(row=4,column=0,padx=20,pady=10,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 10")

        Entry4 = tk.Entry(top,width=28, textvariable=fgname2,state="readonly",readonlybackground="white")
        Entry4.grid(row=4,column=0,padx=260,pady=10,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 10")

        Entry5 = tk.Entry(top,width=28, textvariable=foodname3,state="readonly",readonlybackground="white") 
        Entry5.grid(row=5,column=0,padx=20,pady=10,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 10")

        Entry6 = tk.Entry(top,width=28, textvariable=fgname3,state="readonly",readonlybackground="white")
        Entry6.grid(row=5,column=0,padx=260,pady=10,sticky="w")
        Entry6.configure(font="-family {Palatino Linotype} -size 10")

        Entry7 = tk.Entry(top,width=28, textvariable=foodname4,state="readonly",readonlybackground="white")
        Entry7.grid(row=6,column=0,padx=20,pady=10,sticky="w")
        Entry7.configure(font="-family {Palatino Linotype} -size 10")

        Entry8 = tk.Entry(top,width=28, textvariable=fgname4,state="readonly",readonlybackground="white")
        Entry8.grid(row=6,column=0,padx=260,pady=10,sticky="w")
        Entry8.configure(font="-family {Palatino Linotype} -size 10")

        Entry9 = tk.Entry(top,width=28, textvariable=foodname5,state="readonly",readonlybackground="white")
        Entry9.grid(row=7,column=0,padx=20,pady=10,sticky="w")
        Entry9.configure(font="-family {Palatino Linotype} -size 10")

        Entry10 = tk.Entry(top,width=28, textvariable=fgname5,state="readonly",readonlybackground="white")
        Entry10.grid(row=7,column=0,padx=260,pady=10,sticky="w")
        Entry10.configure(font="-family {Palatino Linotype} -size 10")

        Entry11 = tk.Entry(top,width=28, textvariable=foodname6,state="readonly",readonlybackground="white")
        Entry11.grid(row=8,column=0,padx=20,pady=10,sticky="w")
        Entry11.configure(font="-family {Palatino Linotype} -size 10")

        Entry12 = tk.Entry(top,width=28, textvariable=fgname6,state="readonly",readonlybackground="white")
        Entry12.grid(row=8,column=0,padx=260,pady=10,sticky="w")
        Entry12.configure(font="-family {Palatino Linotype} -size 10")

        Entry13 = tk.Entry(top,width=28, textvariable=foodname7,state="readonly",readonlybackground="white")
        Entry13.grid(row=9,column=0,padx=20,pady=10,sticky="w")
        Entry13.configure(font="-family {Palatino Linotype} -size 10")

        Entry14 = tk.Entry(top,width=28, textvariable=fgname7,state="readonly",readonlybackground="white")
        Entry14.grid(row=9,column=0,padx=260,pady=10,sticky="w")
        Entry14.configure(font="-family {Palatino Linotype} -size 10")

        Entry15 = tk.Entry(top,width=28, textvariable=foodname8,state="readonly",readonlybackground="white")
        Entry15.grid(row=10,column=0,padx=20,pady=10,sticky="w")
        Entry15.configure(font="-family {Palatino Linotype} -size 10")

        Entry16 = tk.Entry(top,width=28, textvariable=fgname8,state="readonly",readonlybackground="white")
        Entry16.grid(row=10,column=0,padx=260,pady=10,sticky="w")
        Entry16.configure(font="-family {Palatino Linotype} -size 10")

        Entry17 = tk.Entry(top,width=28, textvariable=foodname9,state="readonly",readonlybackground="white")
        Entry17.grid(row=11,column=0,padx=20,pady=10,sticky="w")
        Entry17.configure(font="-family {Palatino Linotype} -size 10")

        Entry18 = tk.Entry(top,width=28, textvariable=fgname9,state="readonly",readonlybackground="white")
        Entry18.grid(row=11,column=0,padx=260,pady=10,sticky="w")
        Entry18.configure(font="-family {Palatino Linotype} -size 10")

        Entry19 = tk.Entry(top,width=28, textvariable=foodname10,state="readonly",readonlybackground="white")
        Entry19.grid(row=12,column=0,padx=20,pady=10,sticky="w")
        Entry19.configure(font="-family {Palatino Linotype} -size 10")

        Entry20 = tk.Entry(top,width=28, textvariable=fgname10,state="readonly",readonlybackground="white")
        Entry20.grid(row=12,column=0,padx=260,pady=10,sticky="w")
        Entry20.configure(font="-family {Palatino Linotype} -size 10")

    def Assign_cmd(top):
        top.deiconify()
        top.geometry("270x110")
        Label1 = tk.Label(top)
        Label1.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Which diet you want to Assign ?")
        
        button1=tt.Button(top,text="On Dialysis",command=lambda:ondass(top))
        button1.grid(row=1,column=0,pady=20,padx=40,sticky="w")
        
        button2=tt.Button(top,text="Not on Dialysis",command=lambda:nondass(top))
        button2.grid(row=1,columnspan=1,padx=120,pady=20,sticky="w")

    def ondass(tp):
        try:
            tp.withdraw()
            global r6,r11,r12,listbox1
            u=0

            if r6.get()=="" or r11.get()=="" or r12.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r6.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r6.get())
                if (r11.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r11.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r11.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r12.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:
                        da=r12.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=dietQuery.selectQuery2(list1[0],list1[1],list1[2],1)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                        
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)

                r=dietQuery.selectQuery2(list1[0],list1[1],list1[2],2)
                if len(r)>0:
                    mycursor=dietQuery.selectQuery(5)
                    m=[]
                    for j in mycursor:
                        m.append(j)
                    if len(m)>0:
                        for i in m:
                            dietQuery.insertQuery1(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4],1)
                            
                        o=dietQuery.selectQuery2(list1[0],list1[1],list1[2],3)
                        dietQuery.insertQuery(list1[0],list1[1],list1[2],o[0][0],o[1][0],2)
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        clear2()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
        except:
            pass
            
       
            
    def nondass(tp):
        try:
            tp.withdraw()
            global r6,r11,r12,listbox1
            u=0
            if r6.get()=="" or r11.get()=="" or r12.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r6.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r6.get())
                if (r11.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r11.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r11.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r12.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:
                        da=r12.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=dietQuery.selectQuery2(list1[0],list1[1],list1[2],1)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill all Date correctly!",parent=tp)
                
                r=dietQuery.selectQuery2(list1[0],list1[1],list1[2],2)
                if len(r)>0:
                    mycursor=dietQuery.selectQuery(6)
                    m=[]
                    for j in mycursor:
                        m.append(j)
                    if len(m)>0:
                        for i in m:
                            dietQuery.insertQuery1(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4],1)
                            
                        o=dietQuery.selectQuery2(list1[0],list1[1],list1[2],3)
                        dietQuery.insertQuery(list1[0],list1[1],list1[2],o[0][0],o[1][0],2)
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        clear2()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
                
        except:
            pass
        
    ################################################################Suggesstion###################################################################################
    def getsuggestion():
        global option4,foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10
        op=option4.get()
        if(op=="High Protein Food Items"):
            foodname1.set("Cocoa")
            foodname2.set("Wheat")
            foodname3.set("Peanuts")
            foodname4.set("Soya")
            foodname5.set("Yeast")
            foodname6.set("Flounder")
            foodname7.set("Prawns")
            foodname8.set("Gelatin")
            foodname9.set("Chic. Leg Roasted")
            foodname10.set("Cheddar")
            fgname1.set("Beverages")
            fgname2.set("Grains")
            fgname3.set("Nuts")
            fgname4.set("Cereal Grains")
            fgname5.set("Cakes&Biscuits")
            fgname6.set("Meat&Fish")
            fgname7.set("Meat&Fish")
            fgname8.set("Meat&Fish")
            fgname9.set("Meat&Fish")
            fgname10.set("Milk Products")

        elif(op=="Low Protein Food Items"):
            foodname1.set("Cream")
            foodname2.set("Yogurt")
            foodname3.set("Spring Roll")
            foodname4.set("Irish Stew")
            foodname5.set("Watermelon")
            foodname6.set("Apple")
            foodname7.set("Jelly")
            foodname8.set("Porridge")
            foodname9.set("Beer")
            foodname10.set("Tea")
            fgname1.set("Milk Products")
            fgname2.set("Milk Products")
            fgname3.set("Meat&Fish")
            fgname4.set("Meat&Fish")
            fgname5.set("Fruits")
            fgname6.set("Fruits")
            fgname7.set("Desserts")
            fgname8.set("Desserts")
            fgname9.set("Beverages")
            fgname10.set("Beverages")

        elif(op=="High Potassium Food Items"):
            foodname1.set("Avocado(1/4 whole)")
            foodname2.set("Dates(5 whole)")
            foodname3.set("Artichoke")
            foodname4.set("Brussels Sprouts")
            foodname5.set("Chocolate(1.5-2ounces)")
            foodname6.set("Yogurt")
            foodname7.set("Peanut Butter(2tbs.)")
            foodname8.set("Grapefruit Juice")
            foodname9.set("White Mushrooms(1/2cup)")
            foodname10.set("Pomegranate")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Vegetables")
            fgname4.set("Vegetables")
            fgname5.set("Sweets")
            fgname6.set("Milk Products")
            fgname7.set("Fats&Oils")
            fgname8.set("Fruits")
            fgname9.set("Vegetables")
            fgname10.set("Fruits")

        elif(op=="Low Potassium Food Items"):
            foodname1.set("Blueberries")
            foodname2.set("Mandarin Oranges")
            foodname3.set("Cauliflower")
            foodname4.set("Cucumber")
            foodname5.set("Noodles")
            foodname6.set("Cake")
            foodname7.set("Rice")
            foodname8.set("Apple")
            foodname9.set("Radish")
            foodname10.set("Watermelon")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Vegetables")
            fgname4.set("Vegetables")
            fgname5.set("Grains")
            fgname6.set("Sweets")
            fgname7.set("Grains")
            fgname8.set("Fruits")
            fgname9.set("Vegetables")
            fgname10.set("Fruits")

        elif(op=="High Phosphorus Food Items"):
            foodname1.set("Cheese")
            foodname2.set("Custard")
            foodname3.set("Nuts")
            foodname4.set("Kidey Beans")
            foodname5.set("Chick Peas")
            foodname6.set("Bran cereals")
            foodname7.set("Beer")
            foodname8.set("Cocoa")
            foodname9.set("Chocolte Drinks")
            foodname10.set("Pudding")
            fgname1.set("Milk Products")
            fgname2.set("Milk Products")
            fgname3.set("Nuts&Seeds")
            fgname4.set("Beans")
            fgname5.set("Beans")
            fgname6.set("Whole Grains")
            fgname7.set("Beverages")
            fgname8.set("Beverages")
            fgname9.set("Beverages")
            fgname10.set("Milk Products")

        elif(op=="Low Phosphorus Food Items"):
            foodname1.set("Apricot")
            foodname2.set("Tangerine")
            foodname3.set("Peaches")
            foodname4.set("Carrots")
            foodname5.set("Broccoli")
            foodname6.set("Popcorn")
            foodname7.set("Rice Cereal")
            foodname8.set("Fruit Juices")
            foodname9.set("Sodas")
            foodname10.set("Strawberries")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Fruits")
            fgname4.set("Vegetables")
            fgname5.set("Vegetables")
            fgname6.set("Cereal Grain")
            fgname7.set("Cereal Grain")
            fgname8.set("Beverages")
            fgname9.set("Beverages")
            fgname10.set("Fruits")

        else:
            pass

    ####################################################################View Diet#####################################################################################################
    def viewdiet(top1):
        top1.iconbitmap(r"images/logo.ico")
        top1.config(bg='#d6e0f0')
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        top1.deiconify()

        def onclosing():
            vd1.withdraw()

        vd1 = tk.Toplevel(VD)
        vd1.title("STOCK UP: VIED DIET")
        vd1.withdraw()
        vd1.protocol("WM_DELETE_WINDOW",onclosing)

        def onclosings():
            top1.withdraw()
            vd1.withdraw()
        
        global listBox3,option5,r5
        
        r5 = tk.StringVar()
        option5 = tk.StringVar()
        Label1 = tk.Label(top1)
        Label1.place(relx=0.320, rely=0.019, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold",bg='#d6e0f0',fg='black')
        Label1.configure(text='''VIEW PATIENT DIET''')

        Label2 = tk.Label(top1)
        Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label2.configure(text='''TYPE TO SEARCH -:''')

        Entry1 = tk.Entry(top1,textvariable=r5)
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

        TCombobox1 = tt.Combobox(top1, textvariable=option5,state='readonly')
        value_list = ['All Records',"Name","Phone No.","Date"]
        TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
        option5.set("Choose Category to Search")

        
        cols = ("Name of Patient","Patient Phone No.","Date Diet Given","No of food items","Weight of Patient(Kg)")
        listBox3 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox3.heading(col, text=col)
        listBox3.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox3.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
        listBox3.configure(xscrollcommand=vsb.set)

        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox3.yview)
        vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
        listBox3.configure(yscrollcommand=vsb.set)


        Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_btn_view())
        Button2.place(relx=0.200, rely=0.867, height=60, width=250)
        Button2.configure(font="-family {Palatino Linotype} -size 16")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''SEARCH''')

        Button3 =HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:patient_view_diet(vd1))
        Button3.place(relx=0.415, rely=0.867, height=60, width=250)
        Button3.configure(font="-family {Palatino Linotype} -size 16")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''VIEW DIET''')

        Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_btn3(top1))
        Button4.place(relx=0.627, rely=0.867, height=60, width=250)
        Button4.configure(font="-family {Palatino Linotype} -size 14")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''DELETE''')

        listBox3.delete(*listBox3.get_children())
        mycursor=dietQuery.selectQuery(4)
        for i in mycursor:
            listBox3.insert("", "end", values=i)

        top1.protocol("WM_DELETE_WINDOW",onclosings)

    def search_btn_view():
        global listBox3,option5,r5
        _entry = r5.get()
        _option = option5.get()

        if (_option == 'Name'):
            listBox3.delete(*listBox3.get_children())
            mycursor=dietQuery.selectQuery3(_entry,1)
            for i in mycursor:
                listBox3.insert("", "end", values=i)
                
        elif (_option == 'Phone No.'):
            listBox3.delete(*listBox3.get_children())
            mycursor=dietQuery.selectQuery3(_entry,2)
            for i in mycursor:
                listBox3.insert("", "end", values=i)
                
        elif (_option == "Date"):
            listBox3.delete(*listBox3.get_children())
            mycursor=dietQuery.selectQuery3(_entry,3)
            for i in mycursor:
                listBox3.insert("", "end", values=i)
       
        elif (_option == "All Records"):
            listBox3.delete(*listBox3.get_children())
            mycursor=dietQuery.selectQuery(4)
            for i in mycursor:
                listBox3.insert("", "end", values=i)     
        else:
            option3.set("Choose Category Correctly!")


    def delete_btn3(tp):
        global listBox3
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
            if MsgBox == "yes":
                selected_items = listBox3.selection()
                cur_item=listBox3.focus()
                k=listBox3.item(cur_item)["values"]
                dietQuery.deleteQuery(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),2)
                dietQuery.deleteQuery1(str(k[0]),str(k[1]),str(k[2]),1)
                for selected_item in selected_items:
                    listBox3.delete(selected_item)
            else:
                pass
        except:
            pass

    def patient_view_diet(top1):
        top1.iconbitmap(r"images/logo.ico")
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        global listBox3,listBox4,g1,g2,g3,g4

        def onclosings():
            top1.withdraw()

        selected_items = listBox3.selection()
        cur_item=listBox3.focus()
        k=listBox3.item(cur_item)["values"]

        if(len(k)==0):
            messagebox.showerror("No Record Selected","Please select a record to View",parent=top1)
        else:
            top1.deiconify()
            Label1 = tk.Label(top1)
            Label1.place(relx=0.375, rely=0.009, height=79, width=492)
            Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold")
            Label1.configure(text='''DIET GIVEN''')

            Label2 = tk.Label(top1)
            Label2.place(relx=0.001, rely=0.095, height=40, relwidth=0.241)
            Label2.configure(font="-family {Palatino Linotype} -size 17")
            Label2.configure(text='''NAME -:''')
            
            g1 = tk.StringVar()
            Entry1 = tk.Entry(top1,textvariable=g1,state="readonly")
            Entry1.place(relx=0.155, rely=0.095, height=30, relwidth=0.241)
            Entry1.configure(background="white")
            Entry1.configure(disabledforeground="#a3a3a3")
            Entry1.configure(font="-family {Palatino Linotype} -size 15")
            Entry1.configure(foreground="#000000")
            Entry1.configure(highlightbackground="#d9d9d9")
            Entry1.configure(highlightcolor="black")
            Entry1.configure(insertbackground="black")
            Entry1.configure(selectbackground="#c4c4c4")
            Entry1.configure(selectforeground="black")

            Label4 = tk.Label(top1)
            Label4.place(relx=0.001, rely=0.145, height=40, relwidth=0.241)
            Label4.configure(font="-family {Palatino Linotype} -size 17")
            Label4.configure(text='''DATE -:''')
            
            g2 = tk.StringVar()
            Entry4 = tk.Entry(top1,textvariable=g2,state="readonly")
            Entry4.place(relx=0.155, rely=0.145, height=30, relwidth=0.141)
            Entry4.configure(background="white")
            Entry4.configure(disabledforeground="#a3a3a3")
            Entry4.configure(font="-family {Palatino Linotype} -size 15")
            Entry4.configure(foreground="#000000")
            Entry4.configure(highlightbackground="#d9d9d9")
            Entry4.configure(highlightcolor="black")
            Entry4.configure(insertbackground="black")
            Entry4.configure(selectbackground="#c4c4c4")
            Entry4.configure(selectforeground="black")

            Label3 = tk.Label(top1)
            Label3.place(relx=0.548, rely=0.085, relheight=0.069, relwidth=0.269)
            Label3.configure(font="-family {Palatino Linotype} -size 17")
            Label3.configure(text='''PH.NO -:''')

            g3 = tk.StringVar()
            Entry2 = tk.Entry(top1,textvariable=g3,state="readonly")
            Entry2.place(relx=0.735, rely=0.095, height=30, relwidth=0.169)
            Entry2.configure(background="white")
            Entry2.configure(disabledforeground="#a3a3a3")
            Entry2.configure(font="-family {Palatino Linotype} -size 15")
            Entry2.configure(foreground="#000000")
            Entry2.configure(highlightbackground="#d9d9d9")
            Entry2.configure(highlightcolor="black")
            Entry2.configure(insertbackground="black")
            Entry2.configure(selectbackground="#c4c4c4")
            Entry2.configure(selectforeground="black")

            Label5 = tk.Label(top1)
            Label5.place(relx=0.548, rely=0.134, relheight=0.069, relwidth=0.269)
            Label5.configure(font="-family {Palatino Linotype} -size 17")
            Label5.configure(text='''WEIGHT(kg) -:''')

            g4 = tk.StringVar()
            Entry3 = tk.Entry(top1,textvariable=g4,state="readonly")
            Entry3.place(relx=0.735, rely=0.145, height=30, relwidth=0.169)
            Entry3.configure(background="white")
            Entry3.configure(disabledforeground="#a3a3a3")
            Entry3.configure(font="-family {Palatino Linotype} -size 15")
            Entry3.configure(foreground="#000000")
            Entry3.configure(highlightbackground="#d9d9d9")
            Entry3.configure(highlightcolor="black")
            Entry3.configure(insertbackground="black")
            Entry3.configure(selectbackground="#c4c4c4")
            Entry3.configure(selectforeground="black")
            
            cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
            listBox4 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
            for col in cols:
                listBox4.heading(col, text=col)
            listBox4.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
            
            vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox4.xview)
            vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
            listBox4.configure(xscrollcommand=vsb.set)

            vsb = tt.Scrollbar(top1, orient="vertical", command=listBox4.yview)
            vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
            listBox4.configure(yscrollcommand=vsb.set)

            Label6 = tk.Label(top1)
            Label6.place(relx=0.046, rely=0.825, relheight=0.035, relwidth=0.896)
            Label6.configure(font="-family {Palatino Linotype} -size 17")
            Label6.configure(text='''Note - This Diet is now non-modifiable you have to delete and assign the diet again for any changes.''')

            g1.set(k[0])
            g2.set(k[1])
            g3.set(k[2])
            g4.set(k[3])

            mycursor=dietQuery.selectQuery2(k[0],k[1],k[2],4)

            for i in mycursor:
                listBox4.insert("", "end", values=i)

            top1.protocol("WM_DELETE_WINDOW",onclosings)

    toplevel1(root)
