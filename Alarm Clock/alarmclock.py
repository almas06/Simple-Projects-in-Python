from datetime import datetime
import time
import threading
from tkinter import messagebox
from pygame import mixer

root=Tk()
root.title("Alarm Clock")
root.geometry("510x345")
root.resizable(height=False,width=False)
setTimeVar = StringVar()
msgVar = StringVar()

mixer.init()
def th(): 
    t1 = threading.Thread(target=Alarm,args=()) 
    t1.start()

def Alarm():
    tm = settimeEntry.get()
    if tm=="":
        messagebox.showwarning("Error","Enter a valid time")
    else:
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        settime = tm
        messagebox.showinfo("Alarm","Alarm set successfully")
        m=msgEntry.get()
        setTimeVar.set("")
        msgVar.set("")

        while(settime!=currentTime):
            currentTime = time.strftime("%H:%M")
        if settime==currentTime:
            mixer.music.load("tone.mp3")
            mixer.music.play()
            showmsg = messagebox.showinfo("Alarm Clock",m)
            if showmsg=="ok":
                mixer.music.stop()

mainframe = Frame(root,width=510,height=345,bd=4,relief=RIDGE,bg="Powderblue")
mainframe.place(x=0,y=0)

photo = PhotoImage(file="clock.png")

photolbl = Label(mainframe,image=photo)
photolbl.place(x=0,y=0)

heading = Label(mainframe,text="Alarm Clock",font="msserif 22 bold",bg="grey33",fg="white")
heading.place(x=90,y=10)

setTime = Label(mainframe,text="Set Time(Hr:Min) :",font="msserif 15 bold",bg="grey46",fg="white")
setTime.place(x=50,y=80)

settimeEntry = Entry(mainframe,textvar = setTimeVar,width=9,font="msserif 15 bold",bd=2,relief=SUNKEN)
settimeEntry.place(x=70,y=110)

msg = Label(mainframe,text="Message :",font="msserif 15 bold",bg="grey55",fg="white")
msg.place(x=80,y=170)

msgEntry = Entry(mainframe,textvar = msgVar,width=14,font="msserif 15 bold",bd=2,relief=SUNKEN)
msgEntry.place(x=50,y=200)

setAlarmBtn = Button(mainframe,text="Set Alarm",font="msserif 15 bold",bg="black",fg="white"\
,activebackground="black",activeforeground="white",bd=3,relief=RIDGE,command=th)
setAlarmBtn.place(x=65,y=255)

root.mainloop()
