"""
The program for explaining list boxes without a button
"""

import tkinter as tk
import tkinter.font as font
 
def items_selected(event):
    selected_index = listbox.get(listbox.curselection())
    print("You selected:", selected_index)


root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("400x400")
root.resizable(False, False)
root.title("Listbox")
langs = ["Java","C#","C","C++","Python","Go","JavaScript","PHP","Swift",
]
langs_var = tk.StringVar(value=langs)
listbox = tk.Listbox(root, listvariable=langs_var, height=9,font=myFont)
listbox.bind("<<ListboxSelect>>", items_selected)
listbox.pack()
root.mainloop()
