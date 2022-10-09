""" Create a GUI with Grid
▪ Include at least 10 different elements
 One Button is a must
 The Button should have a function assigned to him """

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("420x170")
root.title("list of Animals")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(100, weight=3)
#################
label_frame = tk.Label(root,text = "Please enter the animal name below")
label_frame.grid(column=0, sticky=tk.E, padx=5, pady=5)
############
Animal1 = tk.Label(root, text="Animal:",font=myFont)
Animal1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
Animal1 = tk.Entry(root,font=myFont)
Animal.grid(column=100, row=0, columspan=50, sticky=tk.E, padx=5, pady=5)
#################################
Animal2 = tk.Label(root, text="Animal2",font=myFont)
Animal2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
Animal2 = tk.Entry(root, show="*",font=myFont)
Animal2.grid(column=100, row=1, sticky=tk.E, padx=5, pady=5)
##############
button = tk.Button(root, text="Enter your list",font=myFont)
button.grid(column=100, row=3, sticky=tk.E, padx=5, pady=5)
root.mainloop()
