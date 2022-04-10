from tkinter import *
from tkinter.ttk import Button as TButton,Label as TLabel,Separator,Checkbutton as TCheckbutton,Entry as TEntry

root = Tk()
root.title("Window")
root.geometry("500x400+500+80")
root.resizable(0,0)

btn = Button(root,text="Click")
btn.pack(padx=5,pady=5)
btn2 = TButton(root,text="Click")
btn2.pack(padx=5,pady=5)
sep = Separator(root,orient="horizontal").pack(fill="x")
l = Label(root,text="Hello Python")
l.pack(padx=5,pady=5)

l2 = TLabel(root,text="Hello Python")
l2.pack(padx=5,pady=5)
sep2 = Separator(root,orient="horizontal").pack(fill="x")

inp = Entry(root).pack(padx=5,pady=5)
inp2 = Entry(root).pack(padx=5,pady=5)
sep3 = Separator(root,orient="horizontal").pack(fill="x")
ch = Checkbutton(root,text="I Agree")
ch.pack(padx=5,pady=5)
ch2 = TCheckbutton(root,text="I Agree")
ch2.pack()

root.mainloop()
