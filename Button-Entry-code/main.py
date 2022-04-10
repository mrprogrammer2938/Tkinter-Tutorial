from tkinter import *

root = Tk()
root.title("Window")
root.geometry("500x400+500+70")
def start():
    l.configure(text=inp.get())
inp = Entry(root)
inp.pack()

btn = Button(root,text="Click",command=start)
btn.pack()

l = Label(root)
l.pack()

root.mainloop()
