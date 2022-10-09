"""
The program for explaining List Boxes with a Button.
"""

import tkinter as tk
import tkinter.font as font

def items_selected():
    languages = []
    selected_indices = listbox.curselection()
    for i in selected_indices:
        index = listbox.get(i)
        languages.append(index)
    for lang in languages:
        print("You selected:", lang)


root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("400x400")
root.resizable(False, False)
root.title("Listbox")
langs = ["Java","C#","C","C++","Python","Go","JavaScript","PHP","Swift",]
langs_var = tk.StringVar(value=langs)
listbox = tk.Listbox(root,listvariable=langs_var,height=9,selectmode="multiple",selectbackground="blue",selectforeground="snow",font=myFont)
button1 = tk.Button(oot, text="Click Me", command=items_selected,font=myFont)
listbox.pack(fill="both")
button1.pack()
root.mainloop()
