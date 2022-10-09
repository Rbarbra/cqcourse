"""  Create a GUI with three message boxes
 Should have different formats
 Should contain texts of different lengths
Exercise 19 – Message Boxes"""

import tkinter as tk


root = tk.Tk()
create own font
font_title
#creating Message boxes
whatever = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text=whatever)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.pack()
root.mainloop()
