from tkinter import *

top = Tk()

top.title("Conversion Table")
top.geometry("600x400")

val1 = DoubleVar()
val1.set('')

out = DoubleVar()
out.set('')


def GConversion():
    out.set(val1.get() * 0.03527)


def clear():
    val1.set('')
    out.set('')


l1 = Label(top, text="Gram Value").grid(row=1, column=0, padx=20, pady=10)
gram = Entry(top, textvariable=val1).grid(row=1, column=1, ipadx=20)
ounce = Button(top, text="Ounce", command=GConversion).grid(row=1, column=2, ipadx=20)

l5 = Label(top, text="Output").grid(row=2, column=0, padx=20, pady=10)
l6 = Label(top, textvariable=out).grid(row=2, column=1, padx=20, pady=10)

clear = Button(top, text="Clear", command=clear).grid(row=3, ipadx=20)

top.mainloop()
