"""use your GUI from exercise 11 and add three buttons to it.
each button should change the text in one of your three predefined labels"""

import tkinter as tk

def ChangeText1():
    label1.config(text="Gene structure\n molecular structure")

def ChangeText2():
    label2.config(text="Organic chemistry\n types of chemical reactions")

def ChangeText3():
    label3.config(text="Bacteria types\n Virus types\n Parasites types")


root = tk.Tk()

label1 = tk.Label(root, text = "Genomics\n molecules" )
label1.pack()
button1 = tk.Button(root, text="Genomics\n molecules", command=ChangeText1)
button1.pack()

label2 = tk.Label(root, text = "Biochemistry\n Chemical reactions" )
label2.pack()
button2 = tk.Button(root, text="Organic chemistry\n types of chemical reactions", command=ChangeText2)
button2.pack()

label3 = tk.Label(root, text = "Bacteria\n Virus\n Parasites" )
label3.pack()
button3 = tk.Button(root, text ="Bacteria\n Virus\n Parasites", command=ChangeText3 )
button3.pack()

button4 = tk.Button(root, text="close", command=root.destroy)
button4.pack()

root.mainloop()
