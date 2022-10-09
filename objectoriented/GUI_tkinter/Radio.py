"""
This is the example of working with radio buttons
"""
import tkinter as tk
import tkinter.font as font

def ShowChoice():
    print(var.get())


root = tk.Tk()
myFont = font.Font(size=20)
var = tk.StringVar()
var.set("Python")
label1 = tk.Label(root, text="Pick one of the following",font=myFont)
label1.pack()
radio1 = tk.Radiobutton(
    root,
    text="Python",
    variable=var,
    value="Python", 
    command=ShowChoice,
    font=myFont
)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(
    root,
    text="Perl",
    variable=var,
    value="Perl",
    command=ShowChoice,
    font=myFont
)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(
    root,
    text="Java",
    variable=var,
    value="Java",
    command=ShowChoice,
    font=myFont
)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(
    root,
    text="C++",
    variable=var,
    value="C++",
    command=ShowChoice,
    font=myFont    
)
radio4.pack(anchor="w")
root.mainloop()