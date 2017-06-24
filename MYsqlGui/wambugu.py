# Code for adding a new user to the db

from tkinter import *
from tkinter import messagebox
import mysql
import mysql.connector
import hashlib

##############################################
####           MYSQL CODE                #####
##############################################

conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
cursor = conn.cursor()


def reset():
    NameVariable.set("")

    PasswordVariable.set("")
    EmailVariable.set("")
    StaffVariable.set("")


## Using sha512()
def passencrypt():
    pent=PassEntry.get()
    pent = pent.encode('utf8')
    pword = hashlib.sha512()
    pword.update(pent)
    password = pword.hexdigest()
    print(pword)
    return password


def insertdata():
    cursor.execute("""INSERT INTO users(staffid, 
    name, password, email) 
    VALUES('%s','%s','%s','%s')""" %(StaffEntry.get(), NameEntry.get(), passencrypt(), EmailEntry.get()))
    conn.commit()
    conn.close()
    print("Done")
    reset()


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

NameLabel=Label(FrameOne,text="Name",bg='Green',fg='white',font=('times',14,'italic'))
NameLabel.grid(row=1,column=0)

EmailLabel=Label(FrameOne,text="Email",bg='Green',fg='white',font=('times',14,'italic'))
EmailLabel.grid(row=2,column=0)

PasswordLabel=Label(FrameOne,text="Password",fg='white',bg='Green',font=('times',14,'italic'))
PasswordLabel.grid(row=3,column=0)

StaffEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),textvariable=StaffVariable)
StaffEntry.grid(row=0,column=2)

NameEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),textvariable=NameVariable)
NameEntry.grid(row=1,column=2)

EmailEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),textvariable=EmailVariable)
EmailEntry.grid(row=2,column=2)

PassEntry=Entry(FrameOne,width=30,font=('times',14,'italic'),show="*",textvariable=PasswordVariable)
PassEntry.grid(row=3,column=2)


SubmitButton=Button(FrameOne,width=10,text="Submit",fg='white',bg='Green',font=('times',14,'italic'),relief='ridge',bd=2
                    ,command=insertdata)
SubmitButton.place(x=270,y=108)

ViewButton=Button(FrameOne,width=10,text="View",fg='white',bg='Green',font=('times',14,'italic'),relief='ridge',bd=2)
ViewButton.grid(row=5,column=3)


root.mainloop()