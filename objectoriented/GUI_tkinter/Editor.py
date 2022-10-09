"""
This is the example program for text fields.
"""

import tkinter as tk
import tkinter.font as font

def Text_Output():
    text1.insert(1.0, "This is a Test\n")
    Content = text1.get(1.0, "end")
    label1.config(text="Your pressed the first button")
    print(Content)
    print(repr(Content))

def Text_Clear():
    label1.config(text="Your pressed the second button")
    text1.delete(1.0, "end")

def Text_length():
    label1.config(
        text="You're text has "
        + str(len(text1.get(1.0, "end-1c")))
        + " characters"
    )

root = tk.Tk()
myFont = font.Font(size=20)
text1 = tk.Text(root,font=myFont, background="yellow")

text1.pack()
button1 = tk.Button(
    root, text="get Contents", command=Text_Output,font=myFont
)
button1.pack(side="left")
button2 = tk.Button(
    root, text="clear Text field", command=Text_Clear,font=myFont
)
button2.pack(side="right")
button3 = tk.Button(
    root, text="Display Text length", command=Text_length,font=myFont
)
button3.pack(side="bottom")
label1 = tk.Label(root, text="",font=myFont)
label1.pack(side="bottom")
root.mainloop()
