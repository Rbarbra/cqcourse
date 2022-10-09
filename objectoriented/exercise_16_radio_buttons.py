"""create two GUIs one with a normal radio buttons and another with a button box"""

#one with normal radio buttons
import tkinter as tk
import tkinter.font as font

def ShowChoice():
    print(var.get())

root = tk.Tk()
myFont = font.Font(size=10)
var = tk.StringVar()
var.set("Python")
label1 = tk.Label(root, text="Pick one of the following",font=myFont)
label1.pack()
radio1 = tk.Radiobutton(root,text="Python",variable=var,value="Python", command=ShowChoice,font=myFont)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(root,text="Perl",variable=var,value="Perl",command=ShowChoice,font=myFont)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(root,text="Java",variable=var,value="Java",command=ShowChoice,font=myFont)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(root,text="C++",variable=var,value="C++",command=ShowChoice,font=myFont)
radio4.pack(anchor="w")
radio5 = tk.Radiobutton(root,text="R",variable=var,value="R", command=ShowChoice,font=myFont)
radio5.pack(anchor="w")
radio6 = tk.Radiobutton(root,text="Dart",variable=var,value="Dart", command=ShowChoice,font=myFont)
radio6.pack(anchor="w")

root.mainloop()
