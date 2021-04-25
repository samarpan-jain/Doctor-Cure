from sqlite3 import *
import mainquery

c1 = mainquery.cursor()
mycursor=c1[0]
conn=c1[1]

def initialize(p1):
    global mycursor,conn
    if p1==1:
        mycursor.execute("create table if not exists spd(nameoffooditem2 text, foodgroup2 text,Quantity2 int,Dimensions2 text,Timetoeat2 text)")
    else:
        mycursor.execute("create table IF NOT EXISTS patientdiet(pname text,pphno int,pdate date,nameoffooditem3 text, foodgroup3 text,Quantity3 int,Dimensions3 text,Timetoeat3 text)")
        mycursor.execute("create table IF NOT EXISTS viewdiet(pname1 text,pphno1 int, pdate1 date,nooffooditem int,weight real)")
        try:
            mycursor.execute('select * from cm1')
        except(OperationalError):
            mycursor.execute("create table cm1(nameoffooditem text, foodgroup text,Quantity int,Dimensions text,Timetoeat text)")
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Scrambled Egg Whites","Eggs,Meat & Fish","3/4","cup","Breakfast"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Multi-grain Toast","Grains","1","slice","Breakfast"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Apple","Fruits","1","unit","Breakfast"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Banana","Fruits","1","unit","Breakfast"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Protein Shake","Supplements","400","ml","Breakfast"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Turkey Breast","Eggs,Meat & Fish","2","oz","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Mayonnaise","Fats & Oils","1","Tbsp","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Multi-grain Bread","Grains","2","slices","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Baby Carrots","Vegtables","8","unit","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Cottage Cheese","Milk Products","1/2","cup","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Protein Bar","Supplements","1(20gm)","unit","Lunch"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Roasted Chicken Breast","Eggs,Meat & Fish","1","unit","Dinner"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Lentil Soup","Soups","1","cup","Dinner"))
            mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",("Celery sticks with cream cheese","Milk Products","2 (sticks), 2 (cheese)","unit , tbsp","Dinner"))
            conn.commit()
        try:
            mycursor.execute('select * from cm2')
        except(OperationalError):
            mycursor.execute("create table cm2(nameoffooditem1 text, foodgroup1 text,Quantity1 int,Dimensions1 text,Timetoeat1 text)")
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Bread","Grains","1","slice","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Dry cereal","Grains",1,"oz","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Cooked Rice or Pasta","Grains","1/2","cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Leafy Vegetable","Vegetables",1,"cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Cooked Vegetable","Vegetables","1/2","cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Vegetable Juice","Vegetables","1/2","cup","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Apple","Fruits",1,"unit","Afternoon Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Dried Fruit","Fruits","1/4","cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Frozen or canned fruits","Fruits","1/2","cup","Evening Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Mango, Sweet Lemon Juice","Fruits","1/2","cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Milk or Yogurt","Milk Products",1,"oz","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Cheese","Milk Products",2,"oz","Afternoon Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Cooked Meat or Fish","Eggs,Meat & Fish",1,"oz","Dinner"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Nuts","Nuts & Seeds","1/3","cup","Evening Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Peanut Butter","Nuts & Seeds",2,"Tbsp","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Seeds","Nuts & Seeds",2,"Tbsp","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Cooked Legumes","Nuts & Seeds","1/2","cup","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Soft Margarine","Fats & Oils",1,"tsp","Afternoon Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Vegetable Oil","Fats & Oils",1,"tsp","Dinner"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Mayonnaise","Fats & Oils",1,"Tbsp","Evening Snack"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Salad dressing","Fats & Oils",2,"Tbsp","Lunch"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Sugar","Sweets&Added Sugar",1,"Tbsp","Entire day"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Jam","Sweets&Added Sugar",1,"Tbsp","Breakfast"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Sorbet,Gelatin","Sweets&Added Sugar","1/2","cup","Dinner"))
            mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",("Lemonade","Refreshments",1,"cup","Evening Snack"))
            conn.commit()

def droptable():
    global mycursor
    mycursor.execute("Drop table if exists spd")

def selectQuery(p):
    global mycursor
    if p==1:
        t=mycursor.execute("select * from record").fetchall()[-1]
        return(t)
    elif p==2:
        mycursor=mycursor.execute("select * from spd order by Timetoeat2 asc")
        return(mycursor)
    elif p==3:
        mycursor.execute("select * from spd")
        m=[]
        for j in mycursor:
            m.append(j)
        return(m)
    elif p==4:
        mycursor.execute("select * from viewdiet order by pdate1 desc")
        return(mycursor)
    elif p==5:
        mycursor.execute("select * from cm1 order by Timetoeat asc")
        return(mycursor)
    elif p==6:
        mycursor.execute("select * from cm2 order by Timetoeat1 asc")
        return(mycursor)

def selectQuery3(p1,p):
    global mycursor
    if p==1:
        mycursor.execute('select * from viewdiet where pname1 like "%{0}%" order by pdate1 desc'.format(p1))
        return(mycursor)
    elif p==2:
        mycursor.execute('select * from viewdiet where pphno1 like "%{0}%" order by pdate1 desc'.format(p1))
        return(mycursor)
    elif p==3:
        mycursor.execute("select * from viewdiet where pdate1 like '%{0}%' order by pdate1 desc".format(p1))
        return(mycursor)
    
def selectQuery1(p1,p2,p3,p4,p5,p):
    global mycursor
    if p==1:
        mycursor.execute("select * from spd where nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(p1,p2,p3,p4,p5))
        x1=[]
        for y in mycursor:
            x1.append(y)
        return(x1)
    elif p==2:
        l1=[]
        mycursor.execute("select * from cm1 where nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(p1,p2,p3,p4,p5))
        for i in mycursor:
            l1.append(i)
        return(l1)
    elif p==3:
        d1=[]
        mycursor.execute("select * from cm2 where nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(p1,p2,p3,p4,p5))
        for i in mycursor:
            d1.append(i)
        return(d1)
            
def selectQuery2(p1,p2,p3,p):
    global mycursor
    if p==1:
        z=[]
        mycursor.execute("select * from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(p1,p2,p3))
        for b in mycursor:
            z.append(b)
        return(z)
    elif p==2:
        r=[]
        mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(p1,p2,p3))
        for w in mycursor:
            r.append(w)
        return(r)
    elif p==3:
        mycursor.execute("select count(*) from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(p1,p2,p3))
        o=[]
        for q in mycursor:
            o.append(q)
        mycursor.execute("select weight from record WHERE name=? AND phn_no=? AND date=?",(p1,p2,p3))
        for t in mycursor:
            o.append(t)
        return(o)
    elif p==4:
        mycursor.execute("select nameoffooditem3,foodgroup3,Quantity3,Dimensions3,Timetoeat3 from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(p1,p2,p3))
        return(mycursor)

    
def insertQuery(p1,p2,p3,p4,p5,p):
    global mycursor,conn
    if p==1:
        mycursor.execute("INSERT INTO spd VALUES(?,?,?,?,?)",(p1,p2,p3,p4,p5))
        conn.commit()
    if p==2:
        mycursor.execute("INSERT INTO viewdiet VALUES(?,?,?,?,?)",(p1,p2,p3,p4,p5))
        conn.commit()
    if p==3:
        mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",(p1,p2,p3,p4,p5))
        conn.commit()
    if p==4:
        mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",(p1,p2,p3,p4,p5))
        conn.commit()

def insertQuery1(p1,p2,p3,p4,p5,p6,p7,p8,p):
    global mycursor,conn
    if p==1:
        mycursor.execute("INSERT INTO patientdiet VALUES(?,?,?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,p7,p8))
        conn.commit()
                         

def deleteQuery(p1,p2,p3,p4,p5,p):
    global mycursor,conn
    if p==1:
        mycursor.execute("DELETE FROM spd WHERE nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(p1,p2,p3,p4,p5))
        conn.commit()
    elif p==2:
        mycursor.execute("DELETE FROM viewdiet WHERE pname1=? AND pphno1=? AND pdate1=? AND nooffooditem=? AND weight=?",(str(p1),str(p2),str(p3),str(p4),str(p5)))
        conn.commit()
    elif p==3:
        mycursor.execute("DELETE FROM cm1 WHERE nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(str(p1),str(p2),str(p3),str(p4),str(p5)))
        conn.commit()
    elif p==4:
        mycursor.execute("DELETE FROM cm2 WHERE nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(str(p1),str(p2),str(p3),str(p4),str(p5)))
        conn.commit()

def updateQuery(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p):
    global mycursor,conn
    if p==1:
        mycursor.execute("UPDATE spd SET nameoffooditem2=?,foodgroup2=?,Quantity2=?,Dimensions2=?,Timetoeat2=? WHERE nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10))
        conn.commit()
    if p==2:
        mycursor.execute("UPDATE cm1 SET nameoffooditem=?,foodgroup=?,Quantity=?,Dimensions=?,Timetoeat=? WHERE nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10))
        conn.commit()
    if p==3:
        mycursor.execute("UPDATE cm2 SET nameoffooditem1=?,foodgroup1=?,Quantity1=?,Dimensions1=?,Timetoeat1=? WHERE nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10))
        conn.commit()

def deleteQuery1(p1,p2,p3,p):
    global mycursor,conn
    if p==1:
        mycursor.execute("DELETE FROM patientdiet WHERE pname=? AND pphno=? AND pdate=?",(str(p1),str(p2),str(p3)))
        conn.commit()
