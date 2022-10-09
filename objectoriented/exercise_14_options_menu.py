""" create three Menus,two should contain atleast seven protein names, use functions to change the background color
the text color of a label and the text displayed in the label corresponding to the chosen option  """

# create three Menus

import tkinter as tk
import tkinter.font as font

def display_selected(choice):
    choice = var1.get()
    print(choice)
    label1.config(text=choice)

def change_bg(choice):
    label1.config(bg=var2.get())

def change_fg(choice):
        label1.config(fg=var2.get())


def change_fg(proteins):
        label1.config(fg=var2.get())

def change_fg(proteins):
    label1.config(fg=var3.get())

root = tk.Tk()
myFont = font.Font(size=10)
root.geometry("500x200")

#defining the varvar
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

#setting them
var1.set("Enzymes")
var2.set("blue")
var3.set("pale green")

menu = tk.OptionMenu(root, var1, "antibodies", "structural", "Enzymes", "transport ", "membrane ", "hormonal", "storage",command=display_selected)
menu.pack(side="left")
menu2 = tk.OptionMenu(root, var2, "blue", "silver", "grey", "purple", "cyan", "gold", "yellow", "salmon", command=change_bg)
menu2.pack(side="left")
menu3 = tk.OptionMenu(root, var3, "olivedrabi", "pale green", "plumI", "corali ", "pink ", "orange", "blue", command=change_bg)
menu3.pack(side="left")

label1 = tk.Label(root, text=var1.get(),bg=var2.get(),fg=var3.get(),font=myFont)
label1.pack(side="right")
root.mainloop()
