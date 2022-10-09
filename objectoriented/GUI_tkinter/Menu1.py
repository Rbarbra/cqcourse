import tkinter as tk
import tkinter.font as font
 
def save():
    pass
 
def load():
    pass   
 
root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("200x150")
mainmenu = tk.Menu(root)
mainmenu.add_command(label = "Save", command= save,font=myFont)  
mainmenu.add_command(label = "Load", command= load,font=myFont)
mainmenu.add_command(label = "Exit", command= root.destroy,font=myFont)
root.config(menu = mainmenu)
root.mainloop()