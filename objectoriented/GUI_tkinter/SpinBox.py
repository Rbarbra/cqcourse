import tkinter as tk
import tkinter.font as font

def DisplayChoice():
    text = "Current Value: " + str(spinbox.get())
    label.configure(text = text)


root = tk.Tk()
myFont = font.Font(size=20)
values = ["Apple", "Banana", "Cabbage", "Beans"]
spinbox = tk.Spinbox(root, from_ = 0, to = 10,increment = 1,font=myFont)
# spinbox = tk.Spinbox(root, from_ = 0, to = 10,increment = 0.5,command = DisplayChoice,font=myFont)
# spinbox = tk.Spinbox(root,values = values,command = DisplayChoice,font=myFont)
spinbox.pack()
text1 = "Current Value: " + str(spinbox.get())
label = tk.Label(root, text = text1,font=myFont)
label.pack()
button1 = tk.Button(root, text="Display Choice", command=DisplayChoice,font=myFont)
button1.pack()
root.mainloop()