import tkinter as tk
import tkinter.font as font

def add_up():
    Nr1 = input1.get()
    Nr2 = input2.get()
    ergebnis = float(Nr1) + float(Nr2)
    w.config(text=str(ergebnis))


root = tk.Tk()
myFont = font.Font(size=20)
input1 = tk.StringVar()
input2 = tk.StringVar()
edit1 = tk.Entry(root, textvariable=input1, width=33,font=myFont)
edit2 = tk.Entry(root, textvariable=input2, width=33,font=myFont)
edit1.pack()
edit2.pack()
button1 = tk.Button(root, text="Click Me", command=add_up, width=30,font=myFont)
button1.pack()
w = tk.Label(root, text="", width=33,font=myFont)
w.pack()
root.mainloop()