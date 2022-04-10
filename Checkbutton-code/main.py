from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
root.title("Checkbutton In Tkinter")
root.geometry("300x200+500+75")
root.resizable(0,0)

def get_mess():
    showinfo(title="Information",message=ch_out.get())

ch_out = StringVar()

l = Label(root,text="Access To Memory").pack()

ch = Checkbutton(root,text="I Agree",variable=ch_out,onvalue="I Agree",offvalue="No",command=get_mess)
ch.pack()

root.mainloop()
