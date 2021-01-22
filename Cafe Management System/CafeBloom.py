from tkinter import*
from tkinter import messagebox
import random
from datetime import date
import time

root=Tk()
root.title("Cafe Management System")
root.geometry("1000x650")
root.resizable(width=False,height=False)
root.configure(bg="#220D0B")

logo = PhotoImage(file="logo.png")
rightcup = PhotoImage(file="rightcup.png")
leftcup = PhotoImage(file="leftcup.png")
#**************************************CheckButton variables*******************************************************

menu1chkVar = IntVar()
menu2chkVar = IntVar()
menu3chkVar = IntVar()
menu4chkVar = IntVar()
menu5chkVar = IntVar()
menu6chkVar = IntVar()
menu7chkVar = IntVar()
menu8chkVar = IntVar()
menu9chkVar = IntVar()
menu10chkVar = IntVar()
menu11chkVar = IntVar()
menu12chkVar = IntVar()

#******************************Entry Variables******************************************************************

menu1Var = IntVar()
menu2Var  = IntVar()
menu3Var  = IntVar()
menu4Var  = IntVar()
menu5Var  = IntVar()
menu6Var  = IntVar()
menu7Var  = IntVar()
menu8Var  = IntVar()
menu9Var  = IntVar()
menu10Var  = IntVar()
menu11Var  = IntVar()
menu12Var  = IntVar()



#************************************FUNCTIONS***********************************************************************
def exit():
    ans=messagebox.askyesno("Cafe Bloom","Are you sure you want to exit?")
    if ans:
        root.destroy()
def CheckBtn_Value():
    if (menu1chkVar.get())==1:
        menu1Entry.configure(state=NORMAL)
    elif menu1chkVar.get()==0:
        menu1Entry.configure(state=DISABLED)
        menu1Var.set("0")

    if (menu2chkVar.get())==1:
        menu2Entry.configure(state=NORMAL)
    elif menu2chkVar.get()==0:
        menu2Entry.configure(state=DISABLED)
        menu2Var.set("0")

    if (menu3chkVar.get())==1:
        menu3Entry.configure(state=NORMAL)
    elif menu3chkVar.get()==0:
        menu3Entry.configure(state=DISABLED)
        menu3Var.set("0")

    if (menu4chkVar.get())==1:
        menu4Entry.configure(state=NORMAL)
    elif menu4chkVar.get()==0:
        menu4Entry.configure(state=DISABLED)
        menu4Var.set("0")

    if (menu5chkVar.get())==1:
        menu5Entry.configure(state=NORMAL)
    elif menu5chkVar.get()==0:
        menu5Entry.configure(state=DISABLED)
        menu5Var.set("0")

    if (menu6chkVar.get())==1:
        menu6Entry.configure(state=NORMAL)
    elif menu6chkVar.get()==0:
        menu6Entry.configure(state=DISABLED)
        menu6Var.set("0")

    if (menu7chkVar.get())==1:
        menu7Entry.configure(state=NORMAL)
    elif menu7chkVar.get()==0:
        menu7Entry.configure(state=DISABLED)
        menu7Var.set("0")

    if (menu8chkVar.get())==1:
        menu8Entry.configure(state=NORMAL)
    elif menu8chkVar.get()==0:
        menu8Entry.configure(state=DISABLED)
        menu8Var.set("0")  

    if (menu9chkVar.get())==1:
        menu9Entry.configure(state=NORMAL)
    elif menu9chkVar.get()==0:
        menu9Entry.configure(state=DISABLED)
        menu9Var.set("0")  

    if (menu10chkVar.get())==1:
        menu10Entry.configure(state=NORMAL)
    elif menu10chkVar.get()==0:
        menu10Entry.configure(state=DISABLED)
        menu10Var.set("0")  

    if (menu11chkVar.get())==1:
        menu11Entry.configure(state=NORMAL)
    elif menu11chkVar.get()==0:
        menu11Entry.configure(state=DISABLED)
        menu11Var.set("0")  

    if (menu12chkVar.get())==1:
        menu12Entry.configure(state=NORMAL)
    elif menu12chkVar.get()==0:
        menu12Entry.configure(state=DISABLED)
        menu12Var.set("0")           
def Receipt():
    m1=menu1Var.get()
    m2=menu2Var.get()
    m3=menu3Var.get()
    m4 =menu4Var.get()
    m5 =menu5Var.get()
    m6=menu6Var.get()
    m7=menu7Var.get()
    m8=menu8Var.get()
    m9=menu9Var.get()
    m10=menu10Var.get()
    m11=menu11Var.get()
    m12=menu12Var.get()
    totalQty=m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12

    today=date.today()
    timee = time.strftime("%H:%M")
    todayDate=today.strftime("%d/%m/%Y")
    receiptTxt.delete("1.0", END)
    x = random.randint(10908, 500876)
    billNo = str(x)
    receiptTxt.insert("1.0","\t      Cafe Bloom\n")
    receiptTxt.insert(END,"      Merced 307, Santiago 8320115 Chile\n")
    receiptTxt.insert(END,"\tPhone:020-23088866")
    receiptTxt.insert(END,"\n------------------------------------------------------------\n")
    receiptTxt.insert(END,"\nBill : "+billNo + "\t\t" +todayDate+"\t\t"+timee+"\n")
    
    receiptTxt.insert(END,"\n------------------------------------------------------------")
    receiptTxt.insert(END,"\nItem\t\tQty.\tCost of item\n")
    receiptTxt.insert(END,"------------------------------------------------------------")

    if menu1Var.get()>0:
        receiptTxt.insert(END,"\nAmericano\t\t"+str(m1)+"\t"+str(m1*220))
    if menu2Var.get()>0:
        receiptTxt.insert(END,"\nCappuccino\t\t"+str(m2)+"\t"+str(m2*200))
    if menu3Var.get()>0:
        receiptTxt.insert(END,"\nEspresso\t\t"+str(m3)+"\t"+str(m3*150))
    if menu4Var.get()>0:
        receiptTxt.insert(END,"\nLatte\t\t"+str(m4)+"\t"+str(m4*150))
    if menu5Var.get()>0:
        receiptTxt.insert(END,"\nChoclate\t\t"+str(m5)+"\t"+str(m5*140))
    if menu6Var.get()>0:
        receiptTxt.insert(END,"\nMocha\t\t"+str(m6)+"\t"+str(m6*350))
    if menu7Var.get()>0:
        receiptTxt.insert(END,"\nGlace\t\t"+str(m7)+"\t"+str(m7*245))
    if menu8Var.get()>0:
        receiptTxt.insert(END,"\nHot Choclate\t\t"+str(m8)+"\t"+str(m8*200))
    if menu9Var.get()>0:
        receiptTxt.insert(END,"\nMacchiato\t\t"+str(m9)+"\t"+str(m9*250))
    if menu10Var.get()>0:
        receiptTxt.insert(END,"\nCorto\t\t"+str(m10)+"\t"+str(m10*200))
    if menu11Var.get()>0:
        receiptTxt.insert(END,"\nIced Coffee\t\t"+str(m11)+"\t"+str(m11*175))
    if menu12Var.get()>0:
        receiptTxt.insert(END,"\nIrish Coffee\t\t"+str(m12)+"\t"+str(m12*245))

    totalPrice=0
    totalPrice=(220*m1)+(200*m2)+(150*m3)+(150*m4)+(140*m5)+(350*m6)\
    +(245*m7)+(200*m8)+(250*m9)+(200*m10)+(175*m11)+(245*m12)
    gstAmt=(totalPrice*(18/100))/100
    netPrice=totalPrice+gstAmt

    receiptTxt.insert(END,"\n\n------------------------------------------------------------")
    receiptTxt.insert(END,"\nTotal\t\t"+str(totalQty)+"\t"+str(totalPrice)+"/-")
    receiptTxt.insert(END,"\nGST\t\t\t"+str(gstAmt))
    receiptTxt.insert(END,"\nNet Total\t\t\t"+str(netPrice)+"/-")
    receiptTxt.insert(END,"\n------------------------------------------------------------")
def Total():
    m1=menu1Var.get()
    m2=menu2Var.get()
    m3=menu3Var.get()
    m4 =menu4Var.get()
    m5 =menu5Var.get()
    m6=menu6Var.get()
    m7=menu7Var.get()
    m8=menu8Var.get()
    m9=menu9Var.get()
    m10=menu10Var.get()
    m11=menu11Var.get()
    m12=menu12Var.get()
    totalPrice=0
    totalPrice=(220*m1)+(200*m2)+(150*m3)+(150*m4)+(140*m5)+(350*m6)\
    +(245*m7)+(200*m8)+(250*m9)+(200*m10)+(175*m11)+(245*m12)
    gstAmt=(totalPrice*(18/100))/100
    netPrice=totalPrice+gstAmt

    today=date.today()
    timee = time.strftime("%H:%M")
    todayDate=today.strftime("%d/%m/%Y")
    receiptTxt.delete("1.0", END)
    x = random.randint(10908, 500876)
    billNo = str(x)
    receiptTxt.insert("1.0","\t      Cafe Bloom\n")
    receiptTxt.insert(END,"      Merced 307, Santiago 8320115 Chile\n")
    receiptTxt.insert(END,"\tPhone:020-23088866")
    receiptTxt.insert(END,"\n-----------------------------------------------------------\n")
    receiptTxt.insert(END,"\nBill : "+billNo + "\t\t" +todayDate+"\t\t"+timee)
    
    receiptTxt.insert(END,"\n\nTotal = "+str(totalPrice)+"/-")
    receiptTxt.insert(END,"\nGST = "+str(gstAmt))
    receiptTxt.insert(END,"\nNet Total = "+str(netPrice)+"/-")
def reset():
    menu1Var.set(0)
    menu2Var.set(0)
    menu3Var.set(0)
    menu4Var.set(0)
    menu5Var.set(0)
    menu6Var.set(0)
    menu7Var.set(0)
    menu8Var.set(0)
    menu9Var.set(0)
    menu10Var.set(0)
    menu11Var.set(0)
    menu12Var.set(0)

    receiptTxt.delete("1.0",END)

#************************************MENUCARD FRAME,HEADING AND LABELS******************************************************************

mainFrame = Frame(root,width=1000,height=650,bd=6,relief=SUNKEN,bg="#220D0B").place(x=0,y=0)

logoImage = Label(mainFrame,image=logo,bd=4,relief=SUNKEN).place(x=220,y=10)
rightcupImage = Label(mainFrame,image=rightcup,bd=2,relief=SUNKEN).place(x=745,y=13)
leftcupImage = Label(mainFrame,image=leftcup,bd=2,relief=SUNKEN).place(x=135,y=13)

menucardFrame = Frame(mainFrame,width=600,height=540,bd=6,relief=SUNKEN,bg="#bf8040",highlightthickness=2,highlightbackground="#ffcc00",highlightcolor="#ffcc00")
menucardFrame.place(x=0,y=100)

menuLbl = Label(mainFrame,text="Bloom MenuCard",font="msserif 20 bold",bg="#bf8040").place(x=0,y=110)

#**********************************************Checkbuttons******************************************************************
menu1Chk = Checkbutton(mainFrame,text="Americano",variable=menu1chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=160)
menu2Chk = Checkbutton(mainFrame,text="Cappuccino",variable=menu2chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=200)
menu3Chk = Checkbutton(mainFrame,text="Espresso",variable=menu3chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=240)
menu4Chk = Checkbutton(mainFrame,text="Latte",variable=menu4chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=280)
menu5Chk = Checkbutton(mainFrame,text="Choclate",variable=menu5chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=320)
menu6Chk = Checkbutton(mainFrame,text="Mocha",variable=menu6chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=360)
menu7Chk = Checkbutton(mainFrame,text="Glace",variable=menu7chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=400)
menu8Chk = Checkbutton(mainFrame,text="Hot Choclate",variable=menu8chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=440)
menu9Chk = Checkbutton(mainFrame,text="Macchiato",variable=menu9chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=480)
menu10Chk = Checkbutton(mainFrame,text="Corto",variable=menu10chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=520)
menu11Chk = Checkbutton(mainFrame,text="Iced Coffee",variable=menu11chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=560)
menu12Chk = Checkbutton(mainFrame,text="Irish Coffee",variable=menu12chkVar,font="msserif 17 bold",bg="#bf8040",onvalue=1,offvalue=0,command=CheckBtn_Value).place(x=30,y=600)

#************************************ENTRIES************************************************************************

menu1Entry = Entry(mainFrame,textvariable=menu1Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu1Entry.place(x=500,y=160)

menu2Entry = Entry(mainFrame,textvar=menu2Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu2Entry.place(x=500,y=200)

menu3Entry = Entry(mainFrame,textvar=menu3Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu3Entry.place(x=500,y=240)

menu4Entry = Entry(mainFrame,textvar=menu4Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu4Entry.place(x=500,y=280)

menu5Entry = Entry(mainFrame,textvar=menu5Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu5Entry.place(x=500,y=320)

menu6Entry = Entry(mainFrame,textvar=menu6Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu6Entry.place(x=500,y=360)

menu7Entry = Entry(mainFrame,textvar=menu7Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu7Entry.place(x=500,y=400)

menu8Entry = Entry(mainFrame,textvar=menu8Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu8Entry.place(x=500,y=440)

menu9Entry = Entry(mainFrame,textvar=menu9Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu9Entry.place(x=500,y=480)

menu10Entry = Entry(mainFrame,textvar=menu10Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu10Entry.place(x=500,y=520)

menu11Entry = Entry(mainFrame,textvar=menu11Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu11Entry.place(x=500,y=560)

menu12Entry = Entry(mainFrame,textvar=menu12Var,width=4,bg="#bf8040",font="verdana 16 bold",bd=4,relief=RAISED,state=DISABLED)
menu12Entry.place(x=500,y=600)

#*************************************PRICE LABELS******************************************************************
menu1Price = Label(mainFrame,text="---------------------220/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=160)
menu2Price = Label(mainFrame,text="---------------------200/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=200)
menu3Price = Label(mainFrame,text="---------------------150/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=240)
menu4Price = Label(mainFrame,text="---------------------150/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=280)
menu5Price = Label(mainFrame,text="---------------------140/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=320)
menu6Price = Label(mainFrame,text="---------------------350/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=360)
menu7Price = Label(mainFrame,text="---------------------245/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=400)
menu8Price = Label(mainFrame,text="-------------------200/-",font="msserif 16 bold italic",bg="#bf8040").place(x=250,y=440)
menu9Price = Label(mainFrame,text="---------------------250/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=480)
menu10Price = Label(mainFrame,text="---------------------200/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=520)
menu11Price = Label(mainFrame,text="---------------------175/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=560)
menu12Price = Label(mainFrame,text="---------------------245/-",font="msserif 16 bold italic",bg="#bf8040").place(x=230,y=600)
#************************************RECEIPT FRAME,LABEL and TEXT*******************************************************************

receiptFrame = Frame(mainFrame,width=385,height=540,bd=6,relief=SUNKEN,bg="#bf8040",highlightthickness=2,highlightbackground="#ffcc00",highlightcolor="#ffcc00")
receiptFrame.place(x=603,y=100)

receiptLbl = Label(receiptFrame,text="Receipt",font="msserif 20 bold ",bg="#bf8040")
receiptLbl.place(x=-5,y=2)

receiptTxt = Text(receiptFrame,width=40,height=22,bd=3,relief=RAISED,font="verdana 10 bold")
receiptTxt.place(x=0,y=40)

#**********************************BUTTONS****************************************************************************

totalBtn = Button(receiptFrame,text="Total",width=10,font="verdana 16 bold",bg="#bf8040",bd=4,relief=RAISED,\
highlightthickness=3,highlightbackground="#ffcc00",highlightcolor="#ffcc00",command=Total)
totalBtn.place(x=0,y=430)

receiptBtn = Button(receiptFrame,text="Receipt",width=10,font="verdana 16 bold",bg="#bf8040",bd=4,relief=RAISED,\
highlightthickness=3,highlightbackground="#ffcc00",highlightcolor="#ffcc00",command=Receipt)
receiptBtn.place(x=185,y=430)

resetBtn = Button(receiptFrame,text="Reset",width=10,font="verdana 16 bold",bg="#bf8040",bd=4,relief=RAISED,\
highlightthickness=3,highlightbackground="#ffcc00",highlightcolor="#ffcc00",command=reset)
resetBtn.place(x=0,y=475)

exitBtn = Button(receiptFrame,text="Exit",width=10,font="verdana 16 bold",bg="#bf8040",bd=4,relief=RAISED,\
highlightthickness=3,highlightbackground="#ffcc00",highlightcolor="#ffcc00",command=exit)
exitBtn.place(x=185,y=475)

#*********************************************************************************************************************

root.mainloop()
