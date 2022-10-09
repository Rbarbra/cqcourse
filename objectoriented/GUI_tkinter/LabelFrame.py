import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry('300x200')
label_frame = tk.LabelFrame(root, text = "LAB",font=myFont)
label_frame.pack()
var = tk.IntVar()
radio1 = tk.Radiobutton(label_frame, text = "Option1",variable = var, value = 1,font=myFont)
radio1.pack()
radio2 = tk.Radiobutton(label_frame, text = "Option2",variable = var, value = 2,font=myFont)
radio2.pack()
radio3 = tk.Radiobutton(label_frame, text = "Option3",variable = var, value = 3,font=myFont)
radio3.pack()
root.mainloop()