import tkinter as tk


def ChangeText1():
    w.config(text="I have new Text")

root = tk.Tk()
w = tk.Label(root, text="Hello World!")
w.pack()
button1 = tk.Button(root, text="Hello World!", command=ChangeText1)
button1.pack()
button2 = tk.Button(root, text="Hello 2", command=root.destroy)
button2.pack()
root.mainloop()
