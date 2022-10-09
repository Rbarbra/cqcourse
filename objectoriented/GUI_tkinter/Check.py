"""
This is the first example for working with check boxes.
"""

import tkinter as tk
import tkinter.font as font

def Print_Check():
    Checking = checkValue.get()
    print("Currently the value of your Checkbutton is", Checking)


root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("250x100")
checkValue = tk.BooleanVar()
checkValue.set(True)
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue, command=Print_Check,font=myFont)
check1.pack(side="left")
root.mainloop()
