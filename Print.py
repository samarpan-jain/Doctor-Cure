import os
from tkinter import messagebox
import datetime as dt
import webbrowser
from tkinter import filedialog
from tabulate import tabulate
from fpdf import FPDF
from shutil import copy2
import tkinter.ttk as tt
import tkinter as tk
import PrintQuery

x1,x2,x3,x4,fp=None,None,None,None,None

def web2():
    webbrowser.open("www.gmail.com")

def web1():
    webbrowser.open("https://web.whatsapp.com/")

def print_btn(screen9,photo,photo1):
    global x1,x2,x3,x4,fp

    def onclosings():
        screen9.withdraw()
        
    screen9.deiconify()
    x1=tk.StringVar()
    x2=tk.StringVar()
    x3=tk.StringVar()
    x4=tk.StringVar()
    
    Label2 = tk.Label(screen9)
    Label2.grid(row=0,column=0,padx=120,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Print Record Entry")
 
    Label2 = tk.Label(screen9)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="Name of the Patient :")

    Label2_1 = tk.Label(screen9)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="Phone Number :")

    Label2_2 = tk.Label(screen9)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="Date :")

    Entry1 = tk.Entry(screen9,width=28,textvariable=x1)
    Entry1.grid(row=2,column=0,columnspan=1,padx=200,pady=20,sticky="w")
    Entry1.configure(font="-family {Palatino Linotype} -size 12")

    Entry2 = tk.Entry(screen9,width=28,textvariable=x2)
    Entry2.grid(row=3,column=0,pady=20,padx=200,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    Entry3 = tk.Entry(screen9,width=28,textvariable=x3)
    Entry3.grid(row=4,column=0,pady=20,padx=200,sticky="w")
    Entry3.configure(font="-family {Palatino Linotype} -size 12")


    button61=tk.Button(screen9,text="Cancel",padx=60,pady=10,bd=4,font=("arial",10,"bold"),bg="#61c0bf",command=lambda:onclosings())
    button61.grid(row=7,column=0,pady=20 )

    button71=tk.Button(screen9,text="Print",padx=60,pady=10,bd=4,font=("arial",10,"bold"),bg="#61c0bf",command=lambda:print_record(screen9))
    button71.grid(row=7,column=0,padx=10,pady=20,sticky="w")

    Label2_3 = tk.Label(screen9)
    Label2_3.grid(row=9,column=0,pady=20,sticky="w")
    Label2_3.configure(font="-family {Palatino Linotype} -size 12")
    Label2_3.configure(text="Share file on :")

    b6=tt.Button(screen9,command=web1)
    b6.grid(row=9,column=0,padx=110,pady=10,sticky="w")
    b6.configure(image=photo)

    b7=tt.Button(screen9,command=web2)
    b7.grid(row=9,column=0,padx=160,pady=10,sticky="w")
    b7.configure(image=photo1)
    

    w1=PrintQuery.Printquerry(x1,x2,x3,"1")
    
    x1.set(w1[0])
    x2.set(w1[4])
    x3.set(w1[3])
    
    screen9.protocol("WM_DELETE_WINDOW",onclosings)


def print_record(tp):
    
    global x1,x2,x3,x4,fp,filename
    try:
        def onclosings():
            os.remove("LastRecord.pdf")
            tp.destroy()
        
        if str(x1.get())=="" or str(x2.get())=="" or str(x3.get())=="":
            messagebox.showerror("Error","Please fill all the details correctly!",parent=tp)
        else:
            files=[("Pdf Document","*.pdf")]
            fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf",parent=tp)

            if fp is None:
                messagebox.showerror("Invalid file Name","Please enter valid Name",parent=tp)
            else:
                st="\n"
                b1=PrintQuery.Printquerry(x1,x2,x3,"2")
                b2=PrintQuery.Printquerry(x1,x2,x3,"3")
               
                st+="Doctor's Details\n"
                st+="Doctor's Name: "+b1[0]+" "+b1[1]+"\n"
                st+="Doctor's Ph.no: "+b1[2]+"\n\n"
                st+="Patient Details\n"
                st+="Patient Name: "+x1.get()+"\n"
                st+="Patient Age: "+str(b2[0][0])+"\n"
                st+="Patient Ph.no: "+x2.get()+"\n"
                st+="Patient Diagnosis Date: "+x3.get()+"\n\n"

                l1=PrintQuery.Printquerry(x1,x2,x3,"4")
                pdf=FPDF()

                if(len(l1)>=1):
                    fw= open("temp.txt","w")
                    st+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT MEDICINE\n\n"
                    head=["NAME OF\nTHE MEDICINE","DOSAGE TAKEN","TIME TO\nEAT","NO. OF\nDAYS"]
                    st+=tabulate(l1,headers=head,tablefmt="grid")
                    fw.write(st)
                    fw.close()
                    pdf=FPDF()
                    pdf.add_page()
                    pdf.set_font("Courier",style="B",size=9)
                    pdf.set_margins(0,0,0)
                    f=open("temp.txt","r")
                    for x in f:
                        pdf.cell(-1,5,txt = x, ln = 1)
                    f.close()
                    
                l2=PrintQuery.Printquerry(x1,x2,x3,"5")
                if(len(l2)>=1):
                    fw1= open("temp1.txt","w")
                    s1="\n"
                    s1+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT DIET\n\n"
                    head1=["NAME OF\nFOOD ITEMS","FOOD GROUP","QUANTTY","DIMENSIONS","TIME TO\nEAT"]
                    s1+=tabulate(l2,headers=head1,tablefmt="grid")
                    fw1.write(s1)
                    fw1.close()
                    pdf.add_page()
                    pdf.set_font("Courier",style="B",size=9)
                    pdf.set_margins(0,0,0)
                    f1=open("temp1.txt","r")
                    for x in f1:
                        pdf.cell(-1,5,txt = x, ln = 1)
                    f1.close()

                l3=PrintQuery.Printquerry(x1,x2,x3,"6")
                if(len(l3)>=1):
                    s2="\n"
                    s2+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT YOGA\n\n"
                    pdf.add_page()
                    pdf.set_font("Courier",style="B",size=15)
                    s3="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYOGA TIMINGS\t\t\t\t\t\t\t\t\tYOGA DURATION\n\n"
                    pdf.cell(-1,15,txt = s2, ln = 1)
                    pdf.cell(-1,15,txt =s3,ln=2)
                    x=0
                    y=20
                    for image in range(1,len(l3)+1):
                        pdf.image(l3[image-1],x=x,y=y+image,w=60,h=70,type= "PNG")
                        y=y+70
                        if (image%3==0):
                            if(image==len(l3)):
                                break
                            else:
                                pdf.add_page()
                                pdf.cell(-1,15,txt =s3,ln=1)
                                y=20
                
                if(len(l1)>=1):
                    os.remove("temp.txt")
                if(len(l2)>=1):
                    os.remove("temp1.txt")
                if((len(l1)+len(l2)+len(l3))==0):
                    messagebox.showerror("Not Assigned Anything","Please assign Patient Medicine,Diet,Yoga to generate report.",parent=tp)
                else:
                    pdf.output(fp.name)
                    filename=os.path.basename(fp.name)
                    copy2(fp.name,"LastRecord.pdf")
                    os.startfile("LastRecord.pdf")
                    tp.protocol("WM_DELETE_WINDOW",onclosings)
            
    except PermissionError:
        messagebox.showinfo("Permission Error","Please close all the file then try again",parent=tp)
    except:
        pass

