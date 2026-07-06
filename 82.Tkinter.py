from tkinter import *
from PIL import Image, ImageTk  #used pillow library to add img to window

window=Tk()
# gui logic here
window.geometry("900x1200")    #width x height 

# give title to window
window.title("Incredible Hulk")

# set minimum size window
window.minsize(300,300)       #width , height

# set maximum size of window
window.maxsize(900,700)

# Adding label to window
l1=Label(text="Hulk...hulk...hulk...hulk")  
l1.pack()

# Adding Image
img = Image.open(r"D:\DOWNLOADS\hulk.jpg")     
photo=ImageTk.PhotoImage(img)
l2=Label(image=photo)
l2.pack()

window.mainloop()

window=Tk()
# IMPORTANT LABEL ATTRIBUTES:
# text-add the Text
# bd-background
# fg-foregroud
# font-sets the Font 
# padx-x padding 
# pady- y padding
# relief- border styling -SUNKEN, REAISED, GROOVE, RIDGE -adding style
title_label=Label(text='''The Hulk is a superhero appearing in American comic books published by Marvel Comics. Created by writer Stan Lee and 
                  artist Jack Kirby, the character first appeared in the debut issue of The Incredible Hulk (May 1962). In his comic book appearances, 
                  the character, who has dissociative identity disorder (DID), is primarily represented by the alter ego Hulk, an immense, green-skinned,
                   hulking brute, possessing a limitless degree of physical strength, and the alter ego Dr. Robert Bruce Banner, a physically weak, 
                  socially withdrawn, and emotionally reserved physicist, both of whom typically resent each other. Lee stated that the Hulk's creation was
                   inspired by a combination of Frankenstein and Dr. Jekyll and Mr. Hyde.''', bg="red", fg="white", padx=23, pady=44, font="comicsansms 19 bold", borderwidth=100, relief=SUNKEN)

# IMPORTANT PACK ATTRIBUTE
# anchor=nw  (north-west) , ne   (north-east) movng label
# side=top, bottom, left, right -moving label
# fill=X, Y   -creating flexible label
# padx
# pady
title_label.pack(anchor="ne",side=BOTTOM,fill=Y,padx=23,pady=44)
window.mainloop()