"""Create a GUI that contains at least 6 different Widgets
▪ Arrange them on your GUI using the place() method
▪ Try to create some Widgets that are placed dynamically
Exercise 22 – Using place"""

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("700x700")
#creating widgets
#create labels
label1 = tk.Label(root,text="Label1",background="white",foreground="red",font=myFont)
label2 = tk.Label(root,text="Label2",background="white",foreground="blue",font=myFont)
label3 = tk.Label(root,text="Label3",background="white",foreground="green",font=myFont)
label4 = tk.Label(root,text="Label4",background="white",foreground="red",font=myFont)
label5 = tk.Label(root,text="Label5",background="white",foreground="blue",font=myFont)
label6 = tk.Label(root,text="Label6",background="white",foreground="green",font=myFont)
#using place method to arrange them on the GUI
label1.place(width=100,height=25,x=100,y=200)
label2.place(width=125,height=50,x=300,y=400)
label3.place(relwidth=0.2,relheight=0.1,relx=0.5,rely=0.5)
label4.place(width=90,height=20,x=90,y=100)
label5.place(width=125,height=50,x=200,y=300)
label6.place(relwidth=0.2,relheight=0.2,relx=0.7,rely=0.7)
#########
root.mainloop()
