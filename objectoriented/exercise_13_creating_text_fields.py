""" create a GUI that consists of a text field, five buttons and two labels
The Buttons should be able to:
insert some text into your text field (one at the beginning and one at the end)
clear the whole text field
print out the text into the terminal
display how many characters the current text has in a label
The second label should be used to display which button was pressed
last (just add a label2.config(text=“You pressed Button ...”) to your
functions"""

#create a GUI that consists of a text field ,five buttons and two labels

import tkinter as tk
import tkinter.font as font

#function for printing out the texts in to the terminal and writing the texts in to the field
#for text1
def text_start():
    text.insert(1.0, "Start of Text\n")
    label_button.config(text="Your pressed the first button")


def text_end():
    text.insert("end", "\n End is a Text\n")
    Content2 = text2.get(1.0, "end")
    label_button.config(text="Your pressed the end button")

#function to clear the whole field
# clearing text1
#clearing text
def text_clear():
    text2.delete(1.0, "end")
    label_button.config(text = "You pressed the clear button")
    label_count.config(text = "you pressed the print button")

def text_print():
    label_button.config(text="You pressed the print button")
    content = text.get(1.0, "end")
    print(content)
    print(repr(content))

def text_length():
    label_count.config(text="You're text has "+ str(len(text2.get(1.0, "end-1c")))+ " characters")
    label_button.config(text = "your pressed the count characters button")

root = tk.Tk()
root.title("Text field")

#create own font
font_title = font.Font(size = 18, family = "arial",underline = 1)
font_body = font.Font(size = 15, family = "arial")


#create text field
text = tk.Text(root,font=myFont, background="yellow")
text = tk.Text(root,font=myFont,background="red")
#create labels
label_button = tk.Label(root,text = "", font = font_body)
label_count = tk.Label(root,text = "", font = font_body)

#create buttons

button_start = tk.Button(root, text="Start", command=Text_start,font=font_body)
button_start.pack(side="left")

button_end = tk.Button(root, text="End", command=Text_end,font=font_body)
button_end.pack(side="left")

button_clear = tk.Button(root, text="Clear  ", command=Text_clear,font=font_body)
button_clear.pack(side="right")

button_print= tk.Button(root, text="Print out  ", command=Text_print,font=font_body)
button_print.pack(side="right")

button_count = tk.Button(root, text="Count characters", command=Text_length,font=font_body)
button_count.pack(side="bottom")

#creating button frame
button_frame = tk.Frame(root)

#create label Frame
label_frame = tk.Frame(root)

#load text field, labels and buttons
text.pack()
button_frame.pack(side = "left")
button_start.pack(side="left", expand = True)
button_end.pack(side="left",  expand = True)
button_clear.pack(side="left", expand = True)
button_print.pack(side="left", expand = True)
button_count.pack(side="left", expand = True)
label_frame.pack(side = "right")
label_button.pack(side = "bottom")
label_count.pack(side = "bottom")
# start GUI
root.mainloop()
