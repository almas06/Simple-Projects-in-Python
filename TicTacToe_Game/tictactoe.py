
#Tic Tac Toe Game made using Tkinter In Python

from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Tic Tac Toe Game")
root.geometry("480x600")
root.config(bg="#455A64")


def reset():
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""



def NewGame():
    reset()
    playX.set(0)
    playO.set(0)
    
i=True
def checker(buttons):
    global i
    if buttons["text"]=="":
        if (i):
            i = False
            buttons["text"] = "X"
            checkForWin()
        else:
            i = True
            buttons["text"] = "O"
            checkForWin()

def checkForWin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X'
        or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X'
         or
        btn7['text'] =='X' and btn8['text'] == 'X' and btn9['text'] == 'X'
         or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X'
         or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'
         or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X'
         or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' 
        or
        btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        score = float(playX.get())
        playX.set(score+3)

        messagebox.showinfo("Tic Tac Toe","X Wins !")
        reset()

    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
          score = float(playO.get())
          playO.set(score+3) 

          messagebox.showinfo("Tic Tac Toe","O Wins !")
          reset()

    elif(btn1['text'] != '' and btn2['text'] != '' and btn3['text'] != '' and
          btn4['text'] != '' and btn5['text'] != '' and btn6['text'] != '' and
          btn7['text'] != '' and btn8['text'] != '' and btn9['text'] != ''):
          messagebox.showinfo("Tic Tac Toe","Tie Game !")
          reset()


playX = IntVar()
playO = IntVar()

playX.set(0)
playO.set(0)


frame = Frame(root, bg="grey")
frame.place(x=0 ,y=0)
    
btn1 = Button(frame, text="", font="msserif 20 bold",bg="#B0BEC5", height=4,width=7,command=lambda:checker(btn1) )
btn1.grid(row=0, column=0)

btn2 = Button(frame, text="", font="msserif 20 bold", height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn2) )
btn2.grid(row=0, column=1)

btn3 = Button(frame, text="", font="msserif 20 bold",  height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn3) )
btn3.grid(row=0, column=2)

btn4 = Button(frame, text="", font="msserif 20 bold",  height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn4) )
btn4.grid(row=1, column=0)

btn5 = Button(frame, text="", font="msserif 20 bold", height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn5) )
btn5.grid(row=1, column=1)

btn6 = Button(frame, text="", font="msserif 20 bold", height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn6) )
btn6.grid(row=1, column=2)

btn7 = Button(frame, text="", font="msserif 20 bold",  height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn7) )
btn7.grid(row=2, column=0)

btn8 = Button(frame, text="", font="msserif 20 bold",  height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn8) )
btn8.grid(row=2, column=1)

btn9 = Button(frame, text="", font="msserif 20 bold",  height=4,width=7,bg="#B0BEC5",command=lambda:checker(btn9) )
btn9.grid(row=2, column=2)
   

reset_btn = Button(root,text="Reset",bg="#78909C",font="lucida 20 bold",height=1,width=8,bd=3,relief=RIDGE, command=reset)
reset_btn.place(x=50,y=440)

newGame_btn = Button(root,text="New Game",bg="#78909C",font="lucida 20 bold",height=1,width=8,bd=3,relief=RIDGE, command=NewGame)
newGame_btn.place(x=250,y=440)


play1 = Label(root,text="Player-X :",font=("msserif 18 bold"),bg="#455A64")
play1.place(x=40,y=500)

play1entry = Entry(root,textvar=playX ,bd=3,font=("msserif 18 bold"),relief=SUNKEN,width=12)
play1entry.place(x=180,y=500,height=35)

play2 = Label(root,text="Player-O :",font=("msserif 18 bold"),bg="#455A64")
play2.place(x=40,y=540)

play2entry = Entry(root,textvar= playO ,bd=3,font=("msserif 18 bold"),relief=SUNKEN,width=12)
play2entry.place(x=180,y=540,height=35)

root.mainloop()
