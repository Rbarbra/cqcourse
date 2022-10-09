"""create a GUI that allows the user to input a nucleotide
sequence and get the number of:
guanine, adenine, cytosine thymine uracil"""
#importing tkinter
import tkinter as tk
import tkinter.font as font
import re

def changetext1():
    label1.config(text="Gaunine")

def changetext2():
        label2.config(text="Adenine")

def changetext3():
    label3.config(text="Cytosine")

def changetext4():
    label4.config(text="Thyamine")

def changetext5():
    label5.config(text="Uracile")

def Number_up():
    Nr1=input.get()

result1 = [m.start() for m in re.finder("a",Nr1)]
result2 = [m.start() for m in re.finder("c",Nr1)]
result3 = [m.start() for m in re.finder("g",Nr1)]
result4 = [m.start() for m in re.finder("t",Nr1)]
label7.config(text=result1)
label8.config(text=result2)
label9.config(text=result3)
label10.config(text=result4)

#count=0
#for letter in Nr1:
#    if letter=="a" and
#      count=count+1
#      print(count)
#      label2.pack()
#      button2.pack()
#    if letter =="c":
#        count1=count+1


root = tk.Tk()
root.title(nucleotide sequencing)
myfont=font.Font(family="courier", slant="italic",size=20)
myfont=font.Font(family="Times",weight="bold",size=20)

input1=tk.StringVar()
edit=tk.Entry(root,testvariable=input1,with=33,font=myfont)
edit.pack()

# = [m.start() for m in re.finder("a",edit1)]
#13.pick
label1 = tk.Label(root,text="Gaunine",font=myfont)
button1=tk.Button(root,text="result1",command=changetext1)
button1.pack()

label2 = tk.Label(root,text="Adenine",font=myfont)
button2=tk.Button(root,text="result2",command=changetext2)
labe2.pack()
button2.pack()
