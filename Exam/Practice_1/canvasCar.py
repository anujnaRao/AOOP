from tkinter import *


def movement():
    canvas.move("car", 5, 0)
    canvas.after(100, movement)


top = Tk()
canvas = Canvas(top)

rect = canvas.create_rectangle(150, 150, 320, 200, tags="car")

canvas.pack()
movement()
top.mainloop()
