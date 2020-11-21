
#Simple Calculator - Python Tkinter

from tkinter import *
import math
from tkinter import colorchooser

def click(event):
    global scrval
    text = event.widget.cget("text")
    if text == "=":
        value = eval(screen.get())
        scrval.set(value)
    elif text == "C":
        scrval.set("")
    else:
        scrval.set(scrval.get() + text)
        screen.update()


root=Tk()
root.geometry("395x495")
root.title("GUI Simple Calculator")

scrval = StringVar()
scrval.set("")

screen = Entry(root, textvar=scrval, font="Arial 30 bold", bd=12,relief=SUNKEN,bg="powder blue",justify="right")
screen.pack()

frame = Frame(root, bg="grey", pady=10)

list1 = ["7", "8", "9", "C", "4", "5", "6", "/", "1", "2", "3", "*" ,".", "0", "00", "+","%","!","=","-"]
i = 0

for n in list1:
    # here width of button means 1 text width
    btn = Button(frame, text=n, font="lucida 20 bold",height=2,width=1,padx=35,  bd=3,relief=RAISED)
    btn.grid(row=int(i / 4), column=i % 4)
    i = i + 1

    btn.bind("<Button-1>", click)
frame.pack(fill=X)

root.mainloop()
