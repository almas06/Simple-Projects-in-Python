#Color Game -Python Tkinter

from tkinter import *
import random
from tkinter import messagebox 

colors = ["Red","Blue","Black","Grey","Yellow","Green","Maroon","Brown","Orange","Violet","Cyan","Silver"]
score = 0
timeleft = 60


def startGame(event):
    if timeleft == 60:
        countdown()
    nextcolor()
    
def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Left","Time Over , Score is "+str(score))
    if timeleft > 0 :
        timeleft -= 1
        timelbl.config(text="Time Left : "+str(timeleft))
        timelbl.after(1000,countdown)


def nextcolor():
    global timeleft
    global score
    if timeleft > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
        entry.delete(0,END)

        random.shuffle(colors)
        
        colorlbl.config(fg = str(colors[1]) , text=str(colors[0]))
        scorelbl.config(text="Score : "+str(score))

def reset():
    global timeleft
    global score
    timeleft = 60
    score = 0 
    colorlbl.config(text="")
    scorelbl.config(text = "Score : " + str(score))
    timelbl.config(text="Time Left : "+str(timeleft))
    entry.delete(0, END)
    
    

def exit():
    root.destroy()


root=Tk()
root.title("Color Game")
root.geometry("500x500")


BGimg = PhotoImage(file = "bg2.png")
background_label = Label(root, image=BGimg)
background_label.place(x=0,y=0)

heading = Label(root,text="Color Game",font="helvetica 25 bold",bg="light blue")
heading.place(x=160,y=10)

instruction = Label(root,text=" Note : Type in the color of words,",font="system 13 bold",bg="light blue",fg="red")
instruction.place(x=80,y=70)

instruction1 = Label(root,text=" and not the word text !!",font="system 13 bold",bg="light blue",fg="red")
instruction1.place(x=140,y=100)

startlbl = Label(root,text="Press Enter to Start",font="helvetica 15 bold",bg="light blue",fg="maroon")
startlbl.place(x=150,y=140)

scorelbl = Label(root,text="Score : "+str(score),font="msserif 15 bold",bg="light blue")
scorelbl.place(x=100,y=180)

timelbl = Label(root,text="Time Left : "+ str(timeleft),font="msserif 14 bold",bg="light blue")
timelbl.place(x=270,y=180)

colorlbl = Label(root,font="helvetica 35 bold")
colorlbl.place(x=180,y=230)


entry = Entry(root,font="msserif 13 bold",bd=2,relief=RIDGE,width=15)
root.bind("<Return>",startGame)
entry.place(x=150,y=320)
entry.focus_set()

resetBtn = Button(root,text="RESET",font="msserif 12 bold",height="1",width=8,bd=2,relief=RIDGE,bg="pink",command=reset)
resetBtn.place(x=180,y=370)

exitBtn = Button(root,text="EXIT",font="msserif 12 bold",height="1",width=8,bd=2,relief=RIDGE,bg="pink",command=exit)
exitBtn.place(x=180,y=410)

root.mainloop()


