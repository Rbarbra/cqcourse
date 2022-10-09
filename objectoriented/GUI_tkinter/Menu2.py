import tkinter as tk
import tkinter.font as font

def emptyfunc():
    pass
 
root = tk.Tk()
myFont = font.Font(size=20) 
mainmenu = tk.Menu(root)
# Menu 1
filemenu = tk.Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Open", command = emptyfunc,font=myFont)
filemenu.add_command(label = "Save", command = emptyfunc,font=myFont)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy,font=myFont)
mainmenu.add_cascade(label="File", menu=filemenu)
# Menu 2
toolmenu = tk.Menu(mainmenu, tearoff = 0)
toolmenu.add_command(label = "Find", command = emptyfunc,font=myFont)
toolmenu.add_command(label = "Debugger", command = emptyfunc,font=myFont)
toolmenu.add_command(label = "Replace", command = emptyfunc,font=myFont)
mainmenu.add_cascade(label="Tools", menu=toolmenu)
# Menu 3
helpmenu = tk.Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = "Documentation", command = emptyfunc,font=myFont)
mainmenu.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = mainmenu)
root.mainloop()