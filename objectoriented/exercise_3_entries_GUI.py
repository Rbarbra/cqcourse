"""Add two entry fields to your GUI from exercise 12 so that the user
can input what information he wants to display in your changeable labels"""

# adding two  Entry entries to label one
import tkinter as tk
import tkinter.font as font

def ChangeText1():
    label1.config(text=input1.get())

def ChangeText2():
    label2.config(text=input2.get())


root = tk.Tk()
root.tttle("Questions")
myFont = font.Font(size=12)

label1 = tk.Label(root, text = "Genomics\n molecules" )
label1.pack()
input1 = tk.StringVar()
edit1 = tk.Entry(root, textvariable=input1, width=30,font=myFont)
edit1.pack()
button1 = tk.Button(root, text="Click Me", command= ChangeText1, width=30,font=myFont)
button1.pack()
label1 = tk.Label(root, text="", width=33,font=myFont)
label1.pack()
#working on label two
#label2 = tk.Label(root, text ="Biochemistry\n Chemical reactions" )
#label2.pack()
input2 = tk.StringVar()
edit2 = tk.Entry(root, textvariable=input1, width=30,font=myFont)
edit2.pack()
#button2 = tk.Button(root, text="Click Me", command= ChangeText1, width=30,font=myFont)
#button2.pack()
#label2 = tk.Label(root, text="", width=33,font=myFont)
#label2.pack()

root.mainloop()
