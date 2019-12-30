from tkinter import *
import tkinter.messagebox as mg

top = Tk()

top.title("Login Form")
top.geometry("300x250")

uname = StringVar()
pswd = StringVar()


def login():
    user = uname.get()
    pwd = pswd.get()

    if user == 'rvce' and pwd == '1234':
        mg.showinfo("Log In", "Logged in Successfully")
    else:
        mg.showerror("Error", "Wrong Username or Password")


def cancel():
    uname.set('')
    pswd.set('')


l1 = Label(top, text="Username").grid(row=0,column=0)
username = Entry(textvariable=uname).grid(row=0,column=1)

l2 = Label(top, text="Password").grid(row=1,column=0)
password = Entry(textvariable=pswd, show="*").grid(row=1,column=1)

b1 = Button(top, text="OK", command=login).grid(row=2,column=0)
b2 = Button(top, text="Cancel", command=cancel).grid(row=2,column=1)

top.mainloop()
