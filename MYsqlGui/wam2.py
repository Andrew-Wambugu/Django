# Code allowing user to change password.

from tkinter import *
from tkinter import messagebox
import mysql
import mysql.connector
import hashlib

###############################################
####              MYSQL CODE              #####
###############################################

conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
cursor = conn.cursor()


# Encrypt Confirmed New Password.
def newPassConfcrypt():
    pent=NewPassConfEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()
    print(pword)
    return password


# Encrypt New password
def newPasscrypt():
    pent=NewPassEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()
    print(pword)
    return password


#############################################################################################################
# This function {passencrypt()} reads password entered by user then compares it to the password in the db   #
# The password entered is encrypted and compared to the encrypted password stored in the db                 #
# The function returns a hashed password                                                                    #
#############################################################################################################
## Using sha512()
def passencrypt():
    pent=PassOldEntry.get()
    pent = pent.encode('utf8')
    pword = hashlib.sha512()
    pword.update(pent)
    password = pword.hexdigest()
    print(pword)
    return password

def changepass():
    uname=StaffEntry.get()
    andy=passencrypt()
    status = False
    newpassword=newPasscrypt()
    newconfirmedpassword=newPassConfcrypt()
    try:
        cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (StaffEntry.get()))
        staffid = cursor.fetchone()
        staffid = str(staffid[0])
        print(staffid)
        if staffid is not None:
            print("cursor null")

            if uname == staffid:
                status = True

    except:
        status = False
        print("here")

    try:
        cursor.execute("SELECT password FROM users WHERE staffid = '%s'" % (StaffEntry.get()))
        password = cursor.fetchone()
        passWord = str(password[0])

        if status == True:
            print("Got password")
            if andy == passWord:
                status = True
                print("Correct Password")
    except:
        status=False
        print("more")

    try:
        if newpassword == newconfirmedpassword:
            print("Matching Passwords")
            status = True

    except:
        status = False
        print("No Changes made")

    try:
        cursor.execute("UPDATE users SET password = '%s' WHERE staffid = '%s'" % (newconfirmedpassword, StaffEntry.get()))
        conn.commit()
        print("Password Changed")

    except:
        status=False
        print("No Change")

    if status == True:
        messagebox.showinfo("PASSWORD", "PASSWORD CHANGED")
    else:
        messagebox.showinfo("PASSWORD", "PASSWORD NOT CHANGED")




###############################################
####              INTERFACE               #####
###############################################

root=Tk()


NameVariable=StringVar()
PasswordVariable=StringVar()
EmailVariable=StringVar()
StaffVariable=StringVar()


FrameOne=Frame(root,height=500,width=500,bg='Green')
FrameOne.grid()

StaffLabel=Label(FrameOne,text="StaffID",bg='Green',fg='white',font=('times',14,'italic'))
StaffLabel.grid(row=0,column=0)

PassOldLabel=Label(FrameOne,text="OldPass",bg='Green',fg='white',font=('times',14,'italic'))
PassOldLabel.grid(row=1,column=0)

NewPassLabel=Label(FrameOne,text="NewPass",bg='Green',fg='white',font=('times',14,'italic'))
NewPassLabel.grid(row=2,column=0)

NewPassConfLabel=Label(FrameOne,text="ConfNew",fg='white',bg='Green',font=('times',14,'italic'))
NewPassConfLabel.grid(row=3,column=0)

StaffEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),textvariable=StaffVariable)
StaffEntry.grid(row=0,column=2)

PassOldEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),show="*",textvariable=NameVariable)
PassOldEntry.grid(row=1,column=2)

NewPassEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),show="*",textvariable=EmailVariable)
NewPassEntry.grid(row=2,column=2)

NewPassConfEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),show="*",textvariable=PasswordVariable)
NewPassConfEntry.grid(row=3,column=2)

SubmitButton=Button(FrameOne,width=10,text="Submit",fg='white',bg='Green',font=('times',14,'italic'),relief='ridge',bd=2
                    ,command=changepass)
SubmitButton.place(x=270,y=108)

ViewButton=Button(FrameOne,width=10,text="View",fg='white',bg='Green',font=('times',14,'italic'),relief='ridge',bd=2)
ViewButton.grid(row=5,column=3)


root.mainloop()