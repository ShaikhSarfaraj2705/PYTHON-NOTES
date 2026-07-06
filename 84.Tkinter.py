#CHECKBOX
from tkinter import *

window=Tk()

def getvals():
    print(nameval.get())

window.geometry("655x355")
# heading
Label(window,text="welcome to Tkinter ", font="comicsansms 13 bold", pady=15).grid(row=0,column=3)

# text for form
name=Label(window,text="Name")
phone=Label(window,text="Phone")
gender=Label(window,text="Gender")
emergency=Label(window,text="Emergency Contact")
payments=Label(window,text="Payment Mode")

# pack text form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payments.grid(row=5,column=2)

# variable for storing entries
nameval=StringVar()
phoneval=StringVar()
genderval=StringVar()
emergencyval=StringVar()
paymentmodeval=StringVar()

foodserviceval=IntVar()

# entries for form
nameentry=Entry(window,textvariable=nameval)
phoneentry=Entry(window,textvariable=phoneval)
genderentry=Entry(window,textvariable=genderval)
emergencyentry=Entry(window,textvariable=emergencyval)
paymentmodeentry=Entry(window,textvariable=paymentmodeval)

# pack entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checkbox & pack it
foodservice=Checkbutton(text="want to prebook your meals?", variable=foodserviceval)
foodservice.grid(row=6,column=3)

Button(text="Submit",command=getvals).grid(row=7,column=3)
window.mainloop()