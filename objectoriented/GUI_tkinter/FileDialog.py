import tkinter as tk
import tkinter.font as font
from tkinter import filedialog as fd

def select_file():
    filetypes = (('Fasta files','*.fasta'),('Python files', '*.py'),('sh files', '*.sh'),('text files', '*.txt'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',filetypes=filetypes)
    label1.config(text=filename)
    
root = tk.Tk()
root.geometry("800x300")
root.title("File Dialogue")
myFont = font.Font(size=20)
button1 = tk.Button(root,text="Open File",font=myFont,command=select_file)
button1.place(x=400,y=150,anchor=tk.CENTER)
label1 =tk.Label(root,background="snow",font=myFont)
label1.place(width=750,height=50,x=25,y=250)
root.mainloop()