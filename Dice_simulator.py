import random
from tkinter import *

root=Tk()
root.geometry("700x450")
l1=Label(root,font=("times",200))

def die_roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] # unicode characters for 1, 2, 3, 4, 5 & 6
    l1.config(text=f"{random.choice(number)}{random.choice(number)}")
    l1.pack()

b1=Button(root,text="lets roll...",command=die_roll)
b1.place(x=330,y=0)

root.mainloop()