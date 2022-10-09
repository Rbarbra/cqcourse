"""create a GUI that contains three different Labels
please use texts with a biological or biochemica background"""
#creating a GUI
import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root, text = "Genomics\n molecules" )
label1.pack()
label2 = tk.Label(root, text = "Biochemistry\n Chemical reactions" )
label2.pack()
label3 = tk.Label(root, text = "Bacteria\n Virus\n Parasites" )
label3.pack()
root.mainloop()
