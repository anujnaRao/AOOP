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
        mg.showinfo("Logged in Successfully")
    else:
        mg.showerror("Wrong Username or Password")


def cancel():
    uname.set('')
    pswd.set('')


l1 = Label(top, text="Username").grid()
username = Entry(textvariable=uname)

l2 = Label(top, text="Password")
password = Entry(textvariable=pswd, show="*")

b1 = Button(top, text="OK", command=login)
b2 = Button(top, text="Cancel", command=cancel)

pack()

top.mainloop()
