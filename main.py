from tkinter import *
import tkinter.font as font
from captcha.image import ImageCaptcha
from PIL import Image,ImageTk
from tkinter import messagebox
import random as rn
import cx_Oracle
import time

#Main object
root=Tk()
root.title("Banking System")
root.resizable(False,False)

#favicon
photo = PhotoImage(file = "android-icon-36x36.png")
root.iconphoto(False, photo)

#functions
def submit():
    account_no=reg_account_no.get()
    userName=reg_user_name.get()
    passWord=reg_password.get()
    age=reg_age.get()
    gender=reg_gender.get()
    account_type=reg_account_type.get()
    balance=reg_balance.get()

    if account_no == "" or userName == "" or passWord == "" or age == "" or gender == "" or account_type == "" or balance == "":
        messagebox.showerror("Error", "All field should be filled!!")
        return
    try:
        con = cx_Oracle.connect('system/Aks417$@localhost')
        cursor = con.cursor()
        cursor.execute('select * from bank')
        for c in cursor:
            if c[0] == account_no:
                messagebox.showerror("Error", "Account already exist with this Account Number!!")
                break
        else:
            str1="insert into bank values (" +" '"+account_no+"',"+ "'"+ userName +"',"+  "'"+passWord +"',"+ age+",'"+gender+"',"+"'"+account_type+"',"+balance+")"
            # print(str1)
            cursor.execute(str1)
            con.commit()
            messagebox.showinfo("Message", "Account created!!", parent=reg_window)
            reg_window.destroy()

    except:

        messagebox.showerror("Error", "Something went Wrong!!")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def register():
    #vars
    global reg_account_no
    global reg_user_name
    global reg_password
    global reg_gender
    global reg_age
    global reg_account_type
    global reg_balance
    global reg_message
    global reg_window

    reg_account_no=StringVar()
    reg_user_name=StringVar()
    reg_password=StringVar()
    reg_gender=StringVar()
    reg_age=StringVar()
    reg_account_type=StringVar()
    reg_balance=StringVar()
    reg_balance.set("")
    reg_account_type.set("")
    reg_age.set("")
    reg_gender.set("")
    reg_password.set("")
    reg_user_name.set("")
    reg_account_no.set("")

    #reg_window
    reg_window=Toplevel()
    reg_window.resizable(False,False)
    reg_photo=PhotoImage(file="android-icon-36x36.png")
    reg_window.iconphoto(False,reg_photo)
    reg_window.title("Register")
    #reg_frame
    reg_frame=Frame(reg_window,bg="#d3e0ea",relief=SUNKEN,borderwidth=5)
    reg_frame.grid(row=0,column=0,columnspan=4)
    #reg_labels
    reg_title=Label(reg_frame,text="Register",font=("Arial Rounded MT Bold",35 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=10,padx=40,column=0,row=0,columnspan=4)
    reg_lab1 = Label(reg_frame, text="Account No", font=("Imprint MT Shadow", 15, "bold"), fg="#276678",bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=1,columnspan=2)
    reg_lab2 = Label(reg_frame,text="User name",font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=2,columnspan=2)
    reg_lab3 = Label(reg_frame, text="Age", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=3,columnspan=2)
    reg_lab4 = Label(reg_frame, text="Gender", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(pady=5, padx=20,column=0, row=4,columnspan=2)
    reg_lab5 = Label(reg_frame, text="Password", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=5, columnspan=2)
    reg_lab6 = Label(reg_frame, text="Account Type", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=6,columnspan=2)
    reg_lab7 = Label(reg_frame, text="Balance", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=7,columnspan=2)

    #reg_entry
    reg_account_no_entry=Entry(reg_frame,width=20,textvariable=reg_account_no,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2,pady=5,row=1,column=2,padx=10)
    reg_userName_entry=Entry(reg_frame,width=20,textvariable=reg_user_name,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2,pady=5,row=2,column=2,padx=10)
    reg_age_entry = Entry(reg_frame, width=20, textvariable=reg_age,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2, pady=5, row=3,column=3, padx=10)
    reg_gender_entry = Entry(reg_frame, width=20, textvariable=reg_gender,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2, pady=5, row=4, column=2,padx=10)
    reg_password_entry = Entry(reg_frame,width=20,textvariable=reg_password,show="*",font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2, pady=5, row=5, column=2, padx=10)
    reg_account_type_entry = Entry(reg_frame, width=20, textvariable=reg_account_type,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2, pady=5,row=6, column=2, padx=10)
    reg_balance_entry = Entry(reg_frame, width=20, textvariable=reg_balance,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=2, pady=5,row=7, column=2,padx=10)
    #reg_button
    reg_btn1 = Button(reg_frame, text="Register", width=22, fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 11, "bold"),relief=SOLID,borderwidth=2,activebackground="#d3e0ea",
                command=submit).grid(pady=10,padx=20,row=8,column=0,columnspan=4)

    reg_window.mainloop()

def account():
    account_no=logIn_account_no.get()
    username=logIn_username.get()
    password=logIn_password.get()
    captcha=logIn_captcha.get()

    if account_no == "" or username == "" or password == "" or captcha == "":
        messagebox.showerror("Error", "All field should be filled!!")
    elif captcha != original_captcha:
        messagebox.showerror("Error", "Incorrect Captcha!!")
    else:
        try:
            con = cx_Oracle.connect('system/Aks417$@localhost')
            cursor = con.cursor()
            cursor.execute('select * from bank')
            for c in cursor:
                if c[0] == account_no and c[1] == username and c[2] == password :
                    dashBord()
                    break

            else :
                messagebox.showerror("Error", "Invalid Credentials!!!!!")

        except:
            messagebox.showerror("Error", "Something went Wrong!!")

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

def logIn():
    global logIn_account_no
    global logIn_password
    global logIn_username
    global logIn_captcha
    global original_captcha
    global logIn_window
    #vars
    logIn_account_no=StringVar()
    logIn_password=StringVar()
    logIn_username=StringVar()
    logIn_captcha=StringVar()
    l1=['0','1','2','3','4','5','6','7','8','9']
    l2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    logIn_password.set("")
    logIn_captcha.set("")
    logIn_username.set("")
    logIn_account_no.set("")

    logIn_window = Toplevel()
    logIn_photo = PhotoImage(file="android-icon-36x36.png")
    logIn_window.resizable(False,False)
    logIn_window.iconphoto(False, logIn_photo)
    logIn_window.title("Log In")
    #Frame
    logIn_frame = Frame(logIn_window, bg="#d3e0ea", relief=SUNKEN, borderwidth=5)
    logIn_frame.grid(row=0, column=0, columnspan=4)
    #lables
    logIn_title=Label(logIn_frame,text="Log In",font=("Arial Rounded MT Bold",35 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=10,padx=20,column=0,row=0,columnspan=2)
    logIn_lab1 = Label(logIn_frame, text="Account No", font=("Imprint MT Shadow", 15, "bold"), fg="#276678",bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=1,columnspan=1)
    logIn_lab2 = Label(logIn_frame, text="User name", font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=2,columnspan=1)
    logIn_lab3 = Label(logIn_frame, text="Password", font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=5,padx=20,column=0,row=3,columnspan=1)
    logIn_lab4 = Label(logIn_frame, text="Enter Captcha", font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(pady=5, padx=20,column=0, row=4,columnspan=1)

    #entry
    logIn_account_no_entry= Entry(logIn_frame, width=20, textvariable=logIn_account_no,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=1,pady=5, row=1,column=1, padx=10)
    logIn_username_entry = Entry(logIn_frame, width=20, textvariable=logIn_username,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=1,pady=5, row=2,column=1, padx=10)
    logIn_password_entry = Entry(logIn_frame, width=20, textvariable=logIn_password, show="*",font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=1, pady=5,row=3, column=1, padx=10)
    logIn_captcha_entry = Entry(logIn_frame, width=20, textvariable=logIn_captcha,font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=1,pady=5, row=4,column=1, padx=10)

    #captcha
    image_captcha = ImageCaptcha()
    original_captcha=""
    for i in range(5):
        x=rn.randint(0,2)
        if x == 0:
            original_captcha+=rn.choice(l1)
        else:
            original_captcha+=rn.choice(l2)

    captcha_image = image_captcha.generate_image(original_captcha)

    image = captcha_image.resize((230, 30))
    img = ImageTk.PhotoImage(image)
    logIn_lab5= Label(logIn_frame, image=img).grid(column=0,row=5,columnspan=2,pady=10)

    #button
    logIn_btn1=Button(logIn_frame,text="Log In",width=22, fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 11, "bold"),activebackground="#d3e0ea",activeforeground="#276678",command=account).grid(columnspan=2,column=0,row=6,pady=7)
    logIn_window.mainloop()

def dashBord():
    logIn_window.destroy()
    global dashBord_window
    global dashBord_frame
    dashBord_window = Toplevel()

    dashBord_window.resizable(False,False)
    dashBord_photo = PhotoImage(file="android-icon-36x36.png")
    dashBord_window.iconphoto(False, dashBord_photo)
    dashBord_window.title("Dash Bord")


    dashBord_frame=Frame(dashBord_window,bg="#d3e0ea",relief=SUNKEN,borderwidth=4)
    dashBord_frame.grid(row=0,column=0)

    dashBord_lab1= Label(dashBord_frame, text="Dashboard", font=("Arial Rounded MT Bold",35 ,"bold"),fg="#276678",bg="#d3e0ea").pack(pady=25, padx=105)
    mess="Welcome "+logIn_username.get() + " !!"
    dashBord_lab2 = Label(dashBord_frame, text=mess, font=("Comic Sans MS", 13, "bold"), fg="#276678", bg="#d3e0ea").pack(pady=5, padx=25)
    #buttons
    dashBord_btn1=Button(dashBord_frame,text="Personal Info",font=("Comic Sans MS", 13, "bold"),fg="#f6f5f5",bg="#276678",width=25,command=personal_info,activebackground="#d3e0ea",activeforeground="#276678",relief=RAISED).pack(pady=10,padx=25)
    dashBord_btn2 = Button(dashBord_frame, text="Change Password", font=("Comic Sans MS", 13, "bold"), fg="#f6f5f5",bg="#276678", width=25, command=lambda:change_password(), activebackground="#d3e0ea",activeforeground="#276678", relief=RAISED).pack(pady=10, padx=25)
    dashBord_btn3 = Button(dashBord_frame, text="Withdraw", font=("Comic Sans MS", 13, "bold"), fg="#f6f5f5",bg="#276678", width=25,command=withdraw,activebackground="#d3e0ea",activeforeground="#276678",relief=RAISED).pack(pady=10, padx=25)
    dashBord_btn4 = Button(dashBord_frame, text="Deposit", font=("Comic Sans MS", 13, "bold"), fg="#f6f5f5", bg="#276678",width=25,command=deposit,activebackground="#d3e0ea",activeforeground="#276678",relief=RAISED).pack(pady=10, padx=25)
    dashBord_btn5 = Button(dashBord_frame, text="log out", font=("Comic Sans MS", 13, "bold"), fg="#f6f5f5", bg="#276678",width=25,command=logout,activebackground="#d3e0ea",activeforeground="#276678",relief=RAISED).pack(pady=10, padx=25)

    dashBord_message = Label(dashBord_frame, text="Log In Successful !!!",font="poppins 14 bold", fg="#393232", bg="#ffb037",anchor=S).pack(fill=BOTH,pady=15)

    dashBord_window.mainloop()

def logout():
    dashBord_window.destroy()

def personal_info():

    dashBord_frame.grid_remove()
    global dashBord_frame2
    dashBord_frame2 = Frame(dashBord_window, bg="#d3e0ea", relief=SUNKEN, borderwidth=4)
    dashBord_frame2.size()
    dashBord_frame2.grid(row=0, column=0)

    account_no=""
    username=""
    age=""
    gender=""
    password=""
    account_type=""
    balance=""
    conn = cx_Oracle.connect('system/Aks417$@localhost')

    cursor=conn.cursor()
    cursor.execute("""select * from bank""")
    for c in cursor:
        if c[0] == logIn_account_no.get():
            account_no=c[0]
            username=c[1]
            age=c[3]
            password=c[2]
            gender=c[4]
            account_type=c[5]
            balance=c[6]
            break
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    lab0 = Label(dashBord_frame2, text="Personal Information", font=("Arial Rounded MT Bold",35 ,"bold"),fg="#276678",bg="#d3e0ea",width=20).grid(row=0, column=0, pady=10, padx=15,columnspan=2)
    lab1 = Label(dashBord_frame2,text="Account No:",font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=1,column=0,pady=10)
    lab2 = Label(dashBord_frame2,text="Name:",font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=2,column=0,pady=10)
    lab3 = Label(dashBord_frame2, text="Age:",font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=3, column=0,pady=10)
    lab4 = Label(dashBord_frame2, text="Gender:",font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=4, column=0,pady=10)

    lab5 = Label(dashBord_frame2, text=account_no, font=("Imprint MT Shadow", 15, "bold"), fg="#276678",bg="#d3e0ea").grid(row=1, column=1,pady=10)
    lab6 = Label(dashBord_frame2, text=username,font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=2, column=1,pady=10)
    lab7 = Label(dashBord_frame2, text=age,font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=3, column=1,pady=10)
    lab8 = Label(dashBord_frame2, text=gender,font=("Imprint MT Shadow",15 ,"bold"),fg="#276678",bg="#d3e0ea").grid(row=4, column=1,pady=10)

    lab9 = Label(dashBord_frame2, text="Password:", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=5, column=0, pady=10)
    lab10 = Label(dashBord_frame2, text=password, font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=5, column=1, pady=10)
    lab11 = Label(dashBord_frame2, text="Account Type:", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=6,column=0,pady=10)
    lab12 = Label(dashBord_frame2, text="Balance:", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=7,column=0,pady=10)
    lab13= Label(dashBord_frame2, text=account_type, font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=6, column=1,pady=10)
    lab14 = Label(dashBord_frame2, text=balance, font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=7, column=1,pady=10)
    btn1=Button(dashBord_frame2,text="Back",fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 13, "bold"),activebackground="#d3e0ea",activeforeground="#276678",width=25,command=back).grid(row=8,column=0,columnspan=2,pady=10,padx=10)

def change_password():
    dashBord_frame.grid_remove()
    global dashBord_frame2
    dashBord_frame2 = Frame(dashBord_window, bg="#d3e0ea", relief=SUNKEN, borderwidth=4)
    #vars
    current_password=StringVar()
    new_password=StringVar()
    confirm_password=StringVar()

    dashBord_frame2.grid(row=0, column=0)
    lab0 = Label(dashBord_frame2, text="Change Password", font=("Arial Rounded MT Bold", 35, "bold"), fg="#276678", bg="#d3e0ea", width=20).grid( row =0,column=0,columnspan=2,pady=10, padx=15)
    lab1=Label(dashBord_frame2, text="Current Password:", font=("Imprint MT Shadow",15 ,"bold"), fg="#276678", bg="#d3e0ea").grid(row=1, column=0, pady=10,padx=5)
    lab2 = Label(dashBord_frame2, text="New Password:", font=("Imprint MT Shadow", 15, "bold"), fg="#276678", bg="#d3e0ea").grid(row=2, column=0, pady=10, padx=5)
    lab3 = Label(dashBord_frame2, text="Confirm Password:", font=("Imprint MT Shadow", 15, "bold"), fg="#276678", bg="#d3e0ea").grid(row=3, column=0, pady=10, padx=5)

    e1=Entry(dashBord_frame2, width=20, textvariable=current_password, show="*",font=("Imprint MT Shadow",12 )).grid(ipady=2,columnspan=1, pady=10,row=1, column=1, padx=5)
    e2 = Entry(dashBord_frame2, width=20, textvariable=new_password, show="*", font=("Imprint MT Shadow", 12)).grid(ipady=2,columnspan=1,pady=10, row=2,column=1,padx=5)
    e3 = Entry(dashBord_frame2, width=20, textvariable=confirm_password, show="*", font=("Imprint MT Shadow", 12)).grid(ipady=2,columnspan=1,pady=10, row=3,column=1,padx=5)

    btn0 = Button(dashBord_frame2, text="Change Password", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"), activebackground="#d3e0ea", activeforeground="#276678", width=25, command=lambda :set_password(logIn_account_no,current_password,new_password,confirm_password)).grid(row=4, column=0, columnspan=2,pady=10, padx=10)


    btn1 = Button(dashBord_frame2, text="Back", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"), activebackground="#d3e0ea", activeforeground="#276678", width=25, command=back).grid(row=5,column=0,columnspan=2,pady=10, padx=10)

def set_password(logIn_account_no,current_password,new_password,confirm_password):
    conn =cx_Oracle.connect("system/Aks417$@localhost")
    cursor=conn.cursor()
    str1="select * from bank where account_no = '{}'".format(logIn_account_no.get())
    c=list(cursor.execute(str1))
    # print(c)
    if c[0][2] == current_password.get() and new_password.get() == confirm_password.get():
        str1="update bank set password = '{}' where account_no ='{}'".format(new_password.get(),logIn_account_no.get())
        cursor.execute(str1)
        conn.commit()
        messagebox.showinfo("Password","Password changed successfully!!!")
        back()
    else:
        messagebox.showerror("Error","Invalid credentials!!")
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def withdraw():
    dashBord_frame.grid_remove()
    global dashBord_frame2
    dashBord_frame2 = Frame(dashBord_window, bg="#d3e0ea", relief=SUNKEN, borderwidth=4)
    dashBord_frame2.size()
    dashBord_frame2.grid(row=0, column=0)
    balance=""
    withdraw_amt=IntVar()
    withdraw_amt.set(0)
    
    conn = cx_Oracle.connect('system/Aks417$@localhost')

    cursor = conn.cursor()
    cursor.execute("""select * from bank""")
    for c in cursor:
        if c[0] == logIn_account_no.get():
            balance = c[6]
            break
    if cursor:
        cursor.close()
    if conn:
        conn.close()

    lab0 = Label(dashBord_frame2, text="Withdraw", font=("Arial Rounded MT Bold", 35, "bold"), fg="#276678",bg="#d3e0ea", width=20).pack(pady=10, padx=15)
    lab1 = Label(dashBord_frame2, text="Enter the amount you want to withdraw", font=("Imprint MT Shadow", 15, "bold"), fg="#276678",bg="#d3e0ea").pack( pady=10)
    withdraw_amt_entry = Entry(dashBord_frame2, width=20, textvariable=withdraw_amt,font=("Imprint MT Shadow", 12)).pack(ipady=2, pady=5,padx=10)


    btn0 = Button(dashBord_frame2, text="Withdraw amount", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"),activebackground="#d3e0ea", activeforeground="#276678", width=25, command=lambda:withdraw_amount(withdraw_amt,balance)).pack(pady=10, padx=10)

    btn1 = Button(dashBord_frame2, text="Back", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"),activebackground="#d3e0ea", activeforeground="#276678", width=25, command=back).pack( pady=10, padx=10)

def withdraw_amount(withdraw_amt,balance):
    if withdraw_amt.get() > balance :
        messagebox.showerror("Error", "Insufficient balance to withdraw!!")
    else:
        conn = cx_Oracle.connect('system/Aks417$@localhost')

        cursor = conn.cursor()
        # print("update bank set balance = {} where username = '{}'".format((balance-withdraw_amt.get()),logIn_username.get()))
        cursor.execute("update bank set balance = {} where account_no = '{}'".format((balance-withdraw_amt.get()),logIn_account_no.get()))
        conn.commit()

        if cursor:
            cursor.close()
        if conn:
            conn.close()
        messagebox.showinfo("Message", "Amount is withdrawn!!")
        back()

def deposit():
    dashBord_frame.grid_remove()
    global dashBord_frame2
    dashBord_frame2 = Frame(dashBord_window, bg="#d3e0ea", relief=SUNKEN, borderwidth=4)
    dashBord_frame2.size()
    dashBord_frame2.grid(row=0, column=0)
    balance = ""
    deposit_amt = IntVar()
    deposit_amt.set(0)
    conn = cx_Oracle.connect('system/Aks417$@localhost')

    cursor = conn.cursor()
    cursor.execute("""select * from bank""")
    for c in cursor:
        if c[0] == logIn_account_no.get():
            balance = c[6]
            break
    if cursor:
        cursor.close()
    if conn:
        conn.close()

    lab0 = Label(dashBord_frame2, text="Deposit", font=("Arial Rounded MT Bold", 35, "bold"), fg="#276678", bg="#d3e0ea", width=20).pack(pady=10, padx=15)
    lab1 = Label(dashBord_frame2, text="Enter the amount you want to deposit", font=("Imprint MT Shadow", 15, "bold"), fg="#276678", bg="#d3e0ea").pack(pady=10)
    withdraw_amt_entry = Entry(dashBord_frame2, width=20, textvariable=deposit_amt, font=("Imprint MT Shadow", 12)).pack(ipady=2, pady=5, padx=10)

    btn0 = Button(dashBord_frame2, text="Deposit amount", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"), activebackground="#d3e0ea", activeforeground="#276678", width=25, command=lambda: deposit_amount(deposit_amt, balance)).pack(pady=10, padx=10)


    btn1 = Button(dashBord_frame2, text="Back", fg="#f6f5f5", bg="#276678", font=("Comic Sans MS", 13, "bold"), activebackground="#d3e0ea", activeforeground="#276678", width=25, command=back).pack(pady=10, padx=10)


def deposit_amount(deposit_amt,balance):
    if deposit_amt.get() < 0 :
        messagebox.showerror("Error", "Amount to be deposited can't be negative!!")
    else:
        conn = cx_Oracle.connect('system/Aks417$@localhost')
        cursor = conn.cursor()
        cursor.execute("update bank set balance = {} where account_no = '{}'".format((balance+deposit_amt.get()),logIn_account_no.get()))
        conn.commit()

        if cursor:
            cursor.close()
        if conn:
            conn.close()
        messagebox.showinfo("Message", "Amount is Deposited!!")
        back()

def back():
    dashBord_frame2.destroy()
    dashBord_frame.grid()


f1=Frame(root,height=240,width=400,bg="#d3e0ea",relief=SUNKEN,borderwidth=4)
f1.pack()
# pady=30,padx=50
#Lables
l1=Label(f1,text="Banking system",font=("Arial Rounded MT Bold",35 ,"bold"),fg="#276678",bg="#d3e0ea").pack(pady=15,padx=25)
#image
image=Image.open("bank.png")
image=image.resize((200,200))
img = ImageTk.PhotoImage(image)
l2=Label(f1,image=img).pack(pady=15)

#Buttons
b1=Button(f1,text="Register",width=25,fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 13, "bold"),relief=SOLID,borderwidth=2,activebackground="#d3e0ea",command=register,activeforeground="#276678").pack(pady=12)
b2=Button(f1,text="Log In",width=25,fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 13, "bold"),relief=SOLID,borderwidth=2,activebackground="#d3e0ea",command=logIn,activeforeground="#276678").pack(pady=12)
b3=Button(f1,text="Exit",width=25,fg="#f6f5f5",bg="#276678",font=("Comic Sans MS", 13, "bold"),relief=SOLID,borderwidth=2,command=exit,activebackground="#d3e0ea",activeforeground="#276678").pack(pady=12)

root.mainloop()

#f6f5f5
#d3e0ea
#1687a7
#276678
# https://colorhunt.co/palette/252807