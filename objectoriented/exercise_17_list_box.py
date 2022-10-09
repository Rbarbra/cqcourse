""" Create a GUI that consists of a text field, five buttons and two labels
▪ The Buttons should be able to:
 insert some text into your text field (one at the beginning and one at the end)
 clear the whole text field
 print out the text into the terminal
 display how many characters the current text has in a label
▪ The second label should be used to display which button was pressed
last (just add a label2.config(text=“You pressed Button ...”) to your
functions)
Exercise 13 – Text fields  """

import tkinter as tk
import tkinter.font as font

#function
def items_selected():
    Animals = []
    selected_indices = listbox.curselection()
    for i in selected_indices:
        index = listbox.get(i)
        Animals.append(index)
    for anim in Animals:
        print("You selected:", anim)


root = tk.Tk()
myFont = font.Font(size=10)
root.geometry("400x400")
root.resizable(False, False)
root.title("Listbox")
anim = ["cow","sheep","goat","pig","dog","cat","rabbit","lion","bear"]
anim_var = tk.StringVar(value=anim)
listbox = tk.Listbox(root,listvariable=anim_var,height=9,selectmode="multiple",selectbackground="blue",selectforeground="snow",font=myFont)
button1 = tk.Button(root, text="Click Me", command=items_selected,font=myFont)
listbox.pack(fill="both")
button1.pack()

root.mainloop()
