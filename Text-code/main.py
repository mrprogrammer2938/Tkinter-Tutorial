from tkinter import *

root = Tk()
root.title("Window")
root.geometry("500x540+500+80")
root.resizable(0,0)
def get_text():
    text = txt.get("1.0",END)
    print(text)
def clear_txt():
    txt.delete("1.0",END)
def enable():
    txt["state"] = "normal"
def disable():
    txt["state"] = "disable"

txt = Text(master=root,height=20)
txt.pack(padx=5,pady=5)

btn = Button(root,text="Get Text",width=9,height=2,command=get_text)
btn.pack()
clear_btn = Button(root,text="Clear",width=9,height=2,command=clear_txt)
clear_btn.pack()
exit_btn = Button(root,text="Exit",width=9,height=2,command=quit)
exit_btn.pack(padx=10,pady=10)
btn2 = Button(root,text="On",width=8,height=1,command=enable)
btn2.pack()
btn3 = Button(root,text="Off",width=8,height=1,command=disable)
btn3.pack()
root.mainloop()
