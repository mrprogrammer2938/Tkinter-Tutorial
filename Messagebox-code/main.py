from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Messagebox In Tkinter")
root.geometry("400x300+500+80")
root.resizable(0,0)

def show_info():
    showinfo(title="Information",message="Hello World !")
    
def show_error():
    showerror(title="Error",message="Hello World !")

def show_warning():
    showwarning(title="Warning",message="Hello World !")

btn = Button(root,text="Show Info",command=show_info,width=10,height=3)
btn.pack(padx=10,pady=10)
btn2 = Button(root,text="Show Error",command=show_error,width=10,height=3)
btn2.pack(padx=5,pady=5)
btn3 = Button(root,text="Show Warning",command=show_warning,width=10,height=3)
btn3.pack()

root.mainloop()
