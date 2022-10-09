import tkinter as tk
import tkinter.font as font

def ChangeText1(Text):
    w.config(text=Text)
    print(Text)

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry('300x200')
w = tk.Label(root, text="Hello World!",font=myFont)
w.pack()
button1 = tk.Button(root, text="Hello World!", command=lambda:ChangeText1("Hello Christoph"),font=myFont)
button1.pack()
root.mainloop()

multiplication = lambda x,y: x*y
print(multiplication(5,4))