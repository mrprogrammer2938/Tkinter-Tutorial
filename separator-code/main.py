from tkinter import *
from tkinter.ttk import Separator
root = Tk()
root.title("Window")
root.geometry("300x200+500+75")
# root.resizable(0,0)

l = Label(root,text="Hello World !").pack()

sep = Separator(root,orient="horizontal")
sep.pack(fill="x")

l2 = Label(root,text="Second Hello World !").pack()

sep2 = Separator(root,orient="horizontal")
sep2.pack(fill="x")

btn = Button(root,text="Button").pack()
root.mainloop()
