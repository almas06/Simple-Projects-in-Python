from tkinter import *
import random

root=Tk()
root.title("Rock Paper Scissor")
root.resizable(height=False, width = False)
root.geometry("750x550")
root.configure(bg="powderblue")

#*************************Images***************************************************************************
rockPhoto = PhotoImage(file = "r.png")
paperPhoto = PhotoImage(file="p1.png")
scissorPhoto = PhotoImage(file="s.png")
winPhoto = PhotoImage(file="youwin.png")
loosePhoto = PhotoImage(file="youloose.png")
tiePhoto = PhotoImage(file="tie.png")
rockPhoto1 = PhotoImage(file = "rock.png")
paperPhoto1 = PhotoImage(file="paper.png")
paperPhoto2 = PhotoImage(file="paper1.png")
scissorPhoto1 = PhotoImage(file="scissor.png")
youPhoto = PhotoImage(file="you.png")
compPhoto = PhotoImage(file="comp.png")
resPhoto = PhotoImage(file="res.png")

#***************************Buttons Declaration***************************************************************

yourScrEntry = IntVar()
compScrEntry = IntVar()
click = True
rockPhotoBtn = ''
paperPhotoBtn = ''
scissorPhotoBtn = ''

youchooseBtn = ''
compchooseBtn = ''
winloosetieBtn = ''


#*************************Main Frame and Labels**********************************************************8

mainframe = Frame(root,bd=5,relief = RIDGE,width=750,height=550,bg="powderblue")
mainframe.place(x=0,y=0)

noteLbl = Label(mainframe,text="Select to play",font="MSsansSerif 15 bold",fg="red",bg="powderblue")
noteLbl.place(x=170,y=340)

heading = Label(mainframe,text="Rock Paper Scissor",font="MSsansSerif 27 bold",fg="#000080",bg="powderblue")
heading.place(x=180,y=10)

rocklbl = Label(mainframe,text="Rock",font="arial 15 bold",bg="powderblue")
rocklbl.place(x=80,y=490)

paperlbl = Label(mainframe,text="Paper",font="arial 15 bold",bg="powderblue")
paperlbl.place(x=220,y=490)

scissorlbl = Label(mainframe,text="Scissor",font="arial 15 bold",bg="powderblue")
scissorlbl.place(x=350,y=490)

youchoselbl = Label(mainframe,text="You",font="arial 18 bold",bg="powderblue")
youchoselbl.place(x=90,y=70)

compchoselbl = Label(mainframe,text="Computer",font="arial 18 bold",bg="powderblue")
compchoselbl.place(x=290,y=70)
 
winlooselbl =  Label(mainframe,text="",font="arial 18 bold",bg="powderblue")
winlooselbl.place(x=560,y=70)

compscorelbl = Label(mainframe,text="Computer : ",font="helvetica 15 bold",bg="powderblue")
compscorelbl.place(x=480,y=370)

yourscorelbl = Label(mainframe,text="    You      : ",font="helvetica 15 bold",bg="powderblue")
yourscorelbl.place(x=480,y=410)

#**********************************Entry**********************************************************************
compscoreEntry = Entry(mainframe,textvar=compScrEntry,width=10,font="arial 15 bold",bd=2,relief=SUNKEN)
compscoreEntry.place(x=600,y=370)

yourscoreEntry = Entry(mainframe,textvar=yourScrEntry,width=10,font="arial 15 bold",bd=2,relief=SUNKEN)
yourscoreEntry.place(x=600,y=410)

    
#***********************************Functions***********************************************************************
your_score = 0
comp_score = 0

def newgame():
    global your_score,comp_score
    your_score = 0
    comp_score = 0
    yourScrEntry.set(0)
    compScrEntry.set(0)
    youchooseBtn.configure(image=youPhoto)
    compchooseBtn.configure(image=compPhoto)
    winloosetieBtn.configure(image=resPhoto)


def play():
    global rockPhotoBtn,paperPhotoBtn,scissorPhotoBtn,youchooseBtn,compchooseBtn,winloosetieBtn
    
    rockPhotoBtn = Button(mainframe,image=rockPhoto,command=lambda : youpick("rock"))
    rockPhotoBtn.place(x=50,y=370)

    paperPhotoBtn = Button(mainframe,image=paperPhoto,command=lambda : youpick("paper"))
    paperPhotoBtn.place(x=200,y=370)

    scissorPhotoBtn = Button(mainframe,image=scissorPhoto,command=lambda : youpick("scissor"))
    scissorPhotoBtn.place(x=320,y=370)

    youchooseBtn= Button(mainframe,image=youPhoto)
    youchooseBtn.place(x=20,y=110)

    compchooseBtn= Button(mainframe,image=compPhoto)
    compchooseBtn.place(x=260,y=110)

    winloosetieBtn= Button(mainframe,image=resPhoto)
    winloosetieBtn.place(x=490,y=110)

def compPick():
    choice = random.choice(["rock","paper","scissor"])
    return choice

def youpick(yourchoice):
    global click,your_score,comp_score
    compChoice = compPick()

    if click == True:
        if yourchoice == "rock":
            youchooseBtn.configure(image=rockPhoto1)
            if compChoice == "rock":
                compchooseBtn.configure(image=rockPhoto1)
                winloosetieBtn.configure(image=tiePhoto)
                winlooselbl.configure(text="Tie!!")
            elif compChoice == "paper":
                compchooseBtn.configure(image=paperPhoto1)
                winloosetieBtn.configure(image=loosePhoto)
                winlooselbl.configure(text="Oops!!")
                comp_score+=1
                compScrEntry.set(comp_score)
            else:
                compchooseBtn.configure(image=scissorPhoto1)
                winloosetieBtn.configure(image=winPhoto)
                winlooselbl.configure(text="Hurray!!")
                your_score+=1
                yourScrEntry.set(your_score)

        elif yourchoice == "paper":
            youchooseBtn.configure(image=paperPhoto1)
            if compChoice == "rock":
                compchooseBtn.configure(image=rockPhoto1)
                winloosetieBtn.configure(image=winPhoto)
                winlooselbl.configure(text="Hurray!!")
                your_score+=1
                yourScrEntry.set(your_score)
            elif compChoice == "paper":
                compchooseBtn.configure(image=paperPhoto1)
                winloosetieBtn.configure(image=tiePhoto)
                winlooselbl.configure(text="Tie!!")
            else:
                youchooseBtn.configure(image=paperPhoto2)
                compchooseBtn.configure(image=scissorPhoto1)
                winloosetieBtn.configure(image=loosePhoto)
                winlooselbl.configure(text="Oops!!")
                comp_score+=1
                compScrEntry.set(comp_score)
                

        elif yourchoice == "scissor":
            youchooseBtn.configure(image=scissorPhoto1)
            if compChoice == "rock":
                compchooseBtn.configure(image=rockPhoto1)
                winloosetieBtn.configure(image=loosePhoto)
                winlooselbl.configure(text="Oops!!")
                comp_score+=1
                compScrEntry.set(comp_score)
            elif compChoice == "paper":
                compchooseBtn.configure(image=paperPhoto2)
                winloosetieBtn.configure(image=winPhoto)
                winlooselbl.configure(text="Hurray!!")
                your_score+=1
                yourScrEntry.set(your_score)
            else:
                compchooseBtn.configure(image=scissorPhoto1)
                winloosetieBtn.configure(image=tiePhoto)
                winlooselbl.configure(text="Tie!!")
    
play()

newgameBtn = Button(mainframe,text="New Game",font="msserif 17 bold",fg="#000080",bg="powderblue",bd=3,relief=RIDGE,command=newgame)
newgameBtn.place(x=500,y=470)
    
root.mainloop()
