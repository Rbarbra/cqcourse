"""
The program for explaining vertical scales
"""

import tkinter as tk
import tkinter.font as font

def show1():
    sel = "Vertical Scale Value = " + str(v1.get())
    label2.config(text=sel,)


root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("400x300")
v1 = tk.DoubleVar()
scale1 = tk.Scale(
    root, variable=v1, from_=1, to=100, orient="vertical",font=myFont
)
label1 = tk.Label(root, text="Vertical Scaler",font=myFont)
button1 = tk.Button(
    root, text="Display Vertical", command=show1, bg="yellow",font=myFont
)
label2 = tk.Label(root,font=myFont)
scale1.pack(anchor="center")
label1.pack()
button1.pack(anchor="center")
label2.pack()
root.mainloop()