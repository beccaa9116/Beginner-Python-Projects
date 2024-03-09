import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("My Digital Clock")

def time():
 string = strftime("%H:%M:%S")
 label.config(text=string)
 label.after(1000, time)

label = Label(root, background="black", foreground="pink")
label.pack(anchor="center")
label.size
time()

mainloop()
