from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Window")
root.geometry("300x200+500+75")
root.resizable(0,0)

def get_name():
    txt = inp.get()
    q = askyesnocancel(title="Question",message="Do You Want To Show Your Name? ")
    if q:
        showinfo(title="Information",message=txt)
        print(txt)
    elif q == None:
        pass
    else:
        print(False)

l = Label(root,text="Enter Your Name: ").pack()
inp = Entry(root)
inp.pack(padx=8,pady=8)

btn = Button(root,text="Submit",width=9,height=3,foreground="yellow",background="black",command=get_name)
btn.pack()

root.mainloop()
