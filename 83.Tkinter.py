# FRAME
from tkinter import *

window=Tk()
window.geometry("555x200")

f1=Frame(window,bg="blue",borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

l=Label(f1,text="Using Frame")
l.pack(pady=50)

f2=Frame(window,bg="red",borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l2=Label(f2,text="Welcome to Tkinter Frame", font="Helvetica")
l2.pack()

window.mainloop()

# BUTTONS
from tkinter import *

window=Tk()
window.geometry("555x200")

frame=Frame(window,bg="blue",borderwidth=6, relief=SUNKEN)
frame.pack(anchor="nw")

def hello():
    print("Tkinter button")

def new():
    print("New text")

b1=Button(frame,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT)

b1=Button(frame,fg="red",text="Print Now",command=new)
b1.pack(side=LEFT)

b1=Button(frame,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT)

b1=Button(frame,fg="red",text="Print Now",command=new)
b1.pack(side=LEFT)

window.mainloop()

window=Tk()
window.geometry("655x333")

def getvals():
    print(f"welcome {userval.get()} in Tkinter window ")

user= Label(window,text="Username")
user.grid()
password=Label(window,text="Password")
password.grid(row=1)

#VARIABLE CLASSES IN TKINTER: BooleanVar, DoubleVar, IntVar, StringVar
userval=StringVar()
passval=StringVar()

userentry=Entry(window,textvariable=userval)
userentry.grid(row=0,column=1)

passentry=Entry(window,textvariable=passval)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

window.mainloop()