from tkinter import *
root=Tk()
root.geometry('600x500')
root.title('HOME AUTOMATION')
f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
def r_frame(frame):
    frame.tkraise()
    for f in (f1,f2,f3):
        f.grid(row=0,column=0,sticky="news")
r_frame(f1)

Label(f1,text=' ').grid(row=0,column=0)
Label(f1,text='START MACHINE',font='Helvetica 20 bold underline').grid(row=0,column=2)
Label(f1,text=' ').grid(row=1,column=1)
Label(f1,text=' ').grid(row=2,column=1)
Button(f1,text='OK',font='Helvetica 15',command=lambda:r_frame(f2)).grid(row=3,column=1)
Label(f1,text=' ').grid(row=4,column=1)
Label(f1,text=' ').grid(row=5,column=1)
Button(f1,text='QUIT',font='Helvetica 15',command=root.destroy).grid(row=6,column=1)

uu=0
aa=[]
bb=[]
var1=StringVar()
var2=StringVar()

Label(f2,text='PLEASE LOGIN',font='Helvetica 30 bold underline').grid(row=0,column=1)
Label(f2,text=' ').grid(row=1,column=1)
Label(f2,text=' ').grid(row=2,column=1)
Label(f2,text='ENTER NAME\t\t:',font='Helvetica',fg='brown').grid(row=3,column=1)
Label(f2,text=' ').grid(row=4,column=1)
Label(f2,text=' ').grid(row=5,column=1)
Label(f2,text=' ').grid(row=6,column=1)
Label(f2,text='ENTER PASSWORD\t:',font='Helvetica',fg='brown').grid(row=7,column=1)
entry1=Entry(f2,textvariable=var1)
entry1.grid(row=3,column=2)
entry2=Entry(f2,textvariable=var2)
entry2.grid(row=7,column=2)
Label(f2,text=' ').grid(row=8,column=1)
Label(f2,text=' ').grid(row=9,column=1)
Label(f2,text=' ').grid(row=10,column=1)
Button(f2,text='Back',font='Helvetica 15',command=lambda:r_frame(f1)).grid(row=16,column=0)
Button(f2,text='Cancel',font='Helvetica 15',command=root.destroy).grid(row=16,column=2)
Label(f2,text=' ').grid(row=12,column=1)
Label(f2,text=' ').grid(row=13,column=1)
Label(f2,text=' ').grid(row=14,column=1)
Label(f2,text=' ').grid(row=15,column=1)
def submit():
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    #print(ids[int(entry3.get())])
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            uu=1
            break
        else:
            uu=0
    if(uu==1):
        return r_frame(f3)
    else:
        Label(f2,text='Invalid Username or Password',font='Helvetica').grid(row=16,column=1)
Button(f2,text='Submit',font='Helvetica 15',command=lambda:submit()).grid(row=16,column=1)
'''import xlrd
wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
s=wb.sheet_by_index(0)
ids=s.col_values(2)
for j in range(1,len(ids)+1):
    if(entry3.get()==str(j)):
        
        break
    print('http://indianiotcloud.com/retrieve.php?id='+ids[j-1])'''
def vote_1(x):
    global c
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            
            room='http://indianiotcloud.com/retrieve.php?id='+cc[i]
            break
    print(room)
    r=requests.get(room)
    dd=r.json()
    c=dd['result'][0]['field1']
    d=dd['result'][0]['field2']
    e=dd['result'][0]['field3']
    f=dd['result'][0]['field4']
    if(x==1):
        c=1
        print(c)
        result(c,d,e,f)
    elif(x==0):
        c=0
        print(c)
        result(c,d,e,f)
def vote_2(x):
    global d
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            room='http://indianiotcloud.com/retrieve.php?id='+cc[i]
            break
    r=requests.get(room)
    dd=r.json()
    c=dd['result'][0]['field1']
    d=dd['result'][0]['field2']
    e=dd['result'][0]['field3']
    f=dd['result'][0]['field4']
    if(x==1):
        d=1
        print(c,d,e,f)
        result(c,d,e,f)
    elif(x==0):
        d=0
        print(d)
        result(c,d,e,f)
def vote_3(x):
    global e
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):   
            room='http://indianiotcloud.com/retrieve.php?id='+cc[i]
            break
    r=requests.get(room)
    dd=r.json()
    c=dd['result'][0]['field1']
    d=dd['result'][0]['field2']
    e=dd['result'][0]['field3']
    f=dd['result'][0]['field4']
    if(x==1):
        e=1
        print(e)
        result(c,d,e,f)
    elif(x==0):
        e=0
        print(e)
        result(c,d,e,f)
def vote_4(x):
    global f
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            room='http://indianiotcloud.com/retrieve.php?id='+cc[i]
            break
    r=requests.get(room)
    dd=r.json()
    c=dd['result'][0]['field1']
    d=dd['result'][0]['field2']
    e=dd['result'][0]['field3']
    f=dd['result'][0]['field4']
    if(x==1):
        f=1
        result(c,d,e,f)
    elif(x==0):
        f=0
        print(f)
        result(c,d,e,f)
def result(c,d,e,f):
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            room='http://indianiotcloud.com/update1.php?id='+cc[i]
            break
    r=room
    ccc='&field2='+str(d)
    dd='&field3='+str(e)
    ee='&field4='+str(f)
    r=r+'&field1='+str(c)+ccc+dd+ee
    requests.get(r)
    blink(c,d,e,f)
def blink(c,d,e,f):
    col=['black','red']
    Label(f3,text='\t').grid(row=50+70,column=5)
    Button(f3,text='',bg=col[int(c)],width=2).grid(row=50+70,column=6)
    Label(f3,text='\t').grid(row=50+70,column=5)
    Button(f3,text='',bg=col[int(d)],width=2).grid(row=50+73,column=6)
    Label(f3,text='\t').grid(row=50+70,column=5)
    Button(f3,text='',bg=col[int(e)],width=2).grid(row=50+76,column=6)
    Label(f3,text='\t').grid(row=50+70,column=5)
    Button(f3,text='',bg=col[int(f)],width=2).grid(row=50+79,column=6)
def refresh():
    import requests
    import xlrd
    wb=xlrd.open_workbook(r'F:\python\shubh-python\idpass1.xls')
    s=wb.sheet_by_index(0)
    aa=s.col_values(0)
    bb=s.col_values(1)
    cc=s.col_values(2)
    global room
    for i in range(0,len(aa)):
        if((aa[i]==entry1.get())&(bb[i]==entry2.get())):
            
            room='http://indianiotcloud.com/retrieve.php?id='+cc[i]
            break

    r=requests.get(room)
    dd=r.json()
    c=dd['result'][0]['field1']
    d=dd['result'][0]['field2']
    e=dd['result'][0]['field3']
    f=dd['result'][0]['field4']
    blink(c,d,e,f)
Label(f3,text='HOME AUTOMATION',font='Helvetica 30 bold underline').grid(row=50+65,column=1)
Label(f3,text=' ').grid(row=50+66,column=1)
Label(f3,text=' ').grid(row=50+67,column=1)
Label(f3,text=' ').grid(row=50+68,column=1)
Label(f3,text=' ').grid(row=50+69,column=1)

l=Label(f3,text='BULB',font='Helvetica 20 bold',fg='brown')#bg=color italic
l.grid(row=50+70,column=1)
Label(f3,text=' ').grid(row=50+70,column=2)
b1=Button(f3,text='ON',font='Helvetica 15',width=10,command=lambda:vote_1(1))
b1.grid(row=50+70,column=3)
b4=Button(f3,text='OFF',font='Helvetica 15',width=10,command=lambda:vote_1(0))
b4.grid(row=50+70,column=4)


Label(f3,text=' ').grid(row=50+71,column=2)
Label(f3,text=' ').grid(row=50+72,column=2)
l=Label(f3,text='AC',font='Helvetica 20 bold',fg='brown' )
l.grid(row=50+73,column=1)
Label(f3,text=' ').grid(row=50+70,column=2)
b2=Button(f3,text='ON',font='Helvetica 15',width=10,command=lambda:vote_2(1))
b2.grid(row=50+73,column=3)
b5=Button(f3,text='OFF',font='Helvetica 15',width=10,command=lambda:vote_2(0))
b5.grid(row=50+73,column=4)

Label(f3,text=' ').grid(row=50+74,column=21)
Label(f3,text=' ').grid(row=50+75,column=21)
l=Label(f3,text='TV',font='Helvetica 20 bold',fg='brown' )
l.grid(row=50+76,column=1)
Label(f3,text=' ').grid(row=50+74,column=2)
b2=Button(f3,text='ON',font='Helvetica 15',width=10,command=lambda:vote_3(1))
b2.grid(row=50+76,column=3)
b6=Button(f3,text='OFF',font='Helvetica 15',width=10,command=lambda:vote_3(0))
b6.grid(row=50+76,column=4)

Label(f3,text=' ').grid(row=50+77,column=21)
Label(f3,text=' ').grid(row=50+78,column=21)
l=Label(f3,text='CURTAINS',font='Helvetica 20 bold',fg='brown')#bg=color italic
l.grid(row=50+79,column=1)
Label(f3,text=' ').grid(row=50+77,column=2)
b7=Button(f3,text='ON',font='Helvetica 15',width=10,command=lambda:vote_4(1))
b7.grid(row=50+79,column=3)
b8=Button(f3,text='OFF',font='Helvetica 15',width=10,command=lambda:vote_4(0))
b8.grid(row=50+79,column=4)


Label(f3,text=' ').grid(row=50+80,column=2)
Label(f3,text=' ').grid(row=50+81,column=2)
Button(f3,text='REFRESH',font='Helvetica 20 bold',width=10,command=refresh).grid(row=50+82,column=2)
Label(f3,text=' ').grid(row=50+83,column=5)
Button(f3,text='Exit',font='Helvetica 15 bold',width=5,command=root.destroy).grid(row=50+83,column=5)

