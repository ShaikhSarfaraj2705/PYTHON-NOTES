# HANDLING ENENTS
from tkinter import *
window=Tk()

def Func(event):
    print("You clicked on the button")

window.title("Events in Tkinter")
window.geometry("655x355")
widget=Button(window,text="Click me please")
widget.pack()
widget.bind("<Button-1>",Func)
widget.bind("<Double-1>",quit)
  
window.mainloop()

# MENUS & SUBMENUS
def Info():
    print("This is info")
window=Tk()
NewMenu=Menu(window)
NewMenu.add_command(label="Desc",command=Info)      # to add command line
window.config(menu=NewMenu)
window.mainloop()

# SUBMENU
window=Tk()
Mainmenu=Menu(window)
Submenu=Menu(Mainmenu,tearoff=0)
