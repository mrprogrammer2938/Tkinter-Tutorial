from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
root.title("Window")
root.geometry("300x200+500+75")
root.resizable(0,0)
def change_color():
    color = askcolor(title="Choose Color")
    l.configure(foreground=color[1])
    
l = Label(root,text="Hello World !",background="black")
l.pack()
btn = Button(root,text="Change Background",width=15,height=3,command=change_color).pack()
root.mainloop()
