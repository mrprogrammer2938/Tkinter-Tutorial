from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Window")
root.geometry("400x300+500+75")

def open_file():
    file_types = [
        ("All Files","*.*"),
        ("Text Files","*.txt"),
        ("Python","*.py")
    ]
    file = askopenfile(mode="r",filetypes=file_types,defaultextension=file_types,title="Open File").read()
    print(file)
def save_file():
    txt = """
Hello Sina
Hello Python
Hello World 
Second Hello World !
    """
    file = asksaveasfile(mode="w",filetypes=[("All Files","*.*")],defaultextension=[("All Files","*.*")])
    file.write(txt)
    file.close()
btn = Button(root,text="Open File",width=9,height=3,command=open_file)
btn.pack(padx=8,pady=8)
btn2 = Button(root,text="Save File",width=9,height=3,command=save_file).pack()

root.mainloop()
