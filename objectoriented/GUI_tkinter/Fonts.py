import tkinter as tk
import tkinter.font as font

root = tk.Tk()

myFont = font.Font(family="Courier",slant="italic",size=20, underline=1)
myFont2 = font.Font(family="Times",weight="bold",size=20)

label1 = tk.Label(root,text="Hallo Christoph", font=myFont)
label1.pack()
label2 = tk.Label(root,text="Hallo Christoph", font=myFont2)
label2.pack()
root.mainloop()