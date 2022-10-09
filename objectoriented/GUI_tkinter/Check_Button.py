"""
This is the second example for working with check boxes.
"""

import tkinter as tk
import tkinter.font as font

def Print_Check():
    Checking = checkValue.get()
    if Checking:
        print("You're Check Box is activated")
    else:
        print("You're Check Box is not activated")

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("700x100")
checkValue = tk.BooleanVar()
checkValue.set(True)
check1 = tk.Checkbutton(root, text="my great Checkbox", var=checkValue,font=myFont)
check1.pack(side="left")
button1 = tk.Button(root,text="Check your input",width=40,fg="pink",bg="grey",command=Print_Check,font=myFont)
button1.pack(side="bottom")
root.mainloop()
