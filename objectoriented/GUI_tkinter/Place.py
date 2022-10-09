import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("500x500")
label1 = tk.Label(root,text="Label1",background="white",foreground="red",font=myFont)
label2 = tk.Label(root,text="Label2",background="white",foreground="blue",font=myFont)
label3 = tk.Label(root,text="Label3",background="white",foreground="green",font=myFont)
label1.place(width=75,height=20,x=100,y=200)
label2.place(width=125,height=50,x=300,y=400)
label3.place(relwidth=0.2,relheight=0.1,relx=0.5,rely=0.5)

root.mainloop()