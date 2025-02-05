from tkinter import*
import os
from PIL import ImageTk,Image
import mysql.connector
import random

#=====================================#SQL Database Connection================
mydb=mysql.connector.connect(host='localhost',user='root',password='12345',port=3321,database='bank')

cursor=mydb.cursor()

#=====================================Main Screen=====================
master=Tk()
master.title('Banking App')

#==============================Image======================
img=Image.open(r'C:\Users\91976\Desktop\bank app\secure.png')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)
#Function
def finish_reg():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global lbl
    global temp_balance

    name=temp_name.get()
    age=temp_age.get()
    gender=temp_gender.get()
    bal= temp_balance.get()
    password=temp_password.get()
    acc=random.randint(111111111,999999999)
    vrif_user=f'select Acc_no from user_info where Acc_no={acc}'
    cursor.execute(vrif_user)
    result=cursor.fetchall()


    if len(result)==0:
        reg_user='insert into user_info value(%s,%s,%s,%s,%s,%s)'
        val=[(name,age,gender,acc,bal,password)]
        cursor.executemany(reg_user,val)
        mydb.commit()
    else:
        ibl.config(text='   Account all ready Exist')
def register():
    #variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_balance
    global lbl
    
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()
    temp_balance=StringVar()
    
    #Register Screen
    reg_sc=Toplevel(master)
    reg_sc.title("Register")
    reg_sc.config(bg='#FA8072')

    #label
    Label(reg_sc,text="Please Enter Your details below to Register",font=('Calibri',12),bg='#FA8072').grid(row=0,sticky=N,pady=10)
    Label(reg_sc,text="Name",font=('Calibri',12),bg='#FA8072').grid(row=1,sticky=W)
    Label(reg_sc,text="Age",font=('Calibri',12),bg='#FA8072').grid(row=2,sticky=W)
    Label(reg_sc,text="Gender",font=('Calibri',12),bg='#FA8072').grid(row=3,sticky=W)
    Label(reg_sc,text="Balance",font=('Calibri',12),bg='#FA8072').grid(row=4,sticky=W)
    Label(reg_sc,text="Password",font=('Calibri',12),bg='#FA8072').grid(row=5,sticky=W)
    Ibl=Label(reg_sc,font=('calibri',12),bg='#FA8072')
    Ibl.grid(row=6,sticky=N)
    #Register Button
    Button(reg_sc,text='Register',font=('calibri',12),command=finish_reg).grid(row=6,sticky=N,pady=10)

    #Entry
    Entry(reg_sc,textvariable=temp_name).grid(row=1,column=0)
    Entry(reg_sc,textvariable=temp_age).grid(row=2,column=0)
    Entry(reg_sc,textvariable=temp_gender).grid(row=3,column=0)
    Entry(reg_sc,textvariable=temp_balance).grid(row=4,column=0)
    Entry(reg_sc,textvariable=temp_password).grid(row=5,column=0)
    
def Login():
    global temp_acc
    global temp_password

    temp_acc=StringVar()
    temp_password=StringVar()
    #Login Screen
    lg_sc=Toplevel(master)
    lg_sc.title('Login')
    lg_sc.config(bg='#FA8072')

    #Label
    #Label(lg_sc,text='Enter the Username And Password',font=('Calibri',12,'bold'),bg='#FA8072').grid(row=0,sticky=N,pady=10)
    Label(lg_sc,text='Enter the Account Number',font=('calibri',12),bg='#FA8072').grid(row=0,sticky=W)
    Label(lg_sc,text='Password',font=('calibri',12),bg='#FA8072').grid(row=1,sticky=W)

    #Entry
    Entry(lg_sc,textvariable=temp_acc).grid(row=0,column=1)
    Entry(lg_sc,textvariable=temp_password).grid(row=1,column=1)

    #Buttons
    Button(lg_sc,text='Submit',font=('calibri',12),command=id_login).grid(row=5,sticky=N,pady=10)

def id_login():
    
    global temp_acc
    global temp_password

    acc = temp_acc.get()  
    pass1 = temp_password.get()
    verify_user = f'select name from bank.user_info where Acc_no = %s and password = %s'

    try:
        cursor.execute(verify_user, (acc, pass1))
        result = cursor.fetchall()
        print(result)
        if result:
            print('Login Successful')
        else:
            print("User not found or incorrect credentials")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    

#Labels
Label(master,text='Custom Banking Beta',font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master,text="The Most Secure Bank you've Probably used",font=('calibri',12)).grid(row=1,sticky=N)
Label(master,image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master,text='Register',font=('Calibri',12,'bold'),width=30,command=register).grid(row=3,sticky=N)
Button(master,text='Login',font=('Calibri',12,'bold'),width=30,command=Login).grid(row=4,sticky=N)
master.mainloop()






