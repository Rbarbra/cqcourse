"""
This si the program for frames
"""

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
####################### Plane 1 #####################
yellow_top = tk.Frame(root)
green = tk.Frame(root)
yellow_bottom = tk.Frame(root)
####################### Plane 2 #####################
label8 = tk.Label(yellow_top, text="Label 8",font=myFont)
red = tk.Frame(green)
brown = tk.Frame(green)
label9 = tk.Label(yellow_bottom, text="Label 9",font=myFont)
####################### Plane 3 #####################
button0 = tk.Button(red, text="Button 0",font=myFont)
button1 = tk.Button(red, text="Button 1",font=myFont)
button2 = tk.Button(red, text="Button 2",font=myFont)
button3 = tk.Button(red, text="Button 3",font=myFont)
button4 = tk.Button(red, text="Button 4",font=myFont)
button5 = tk.Button(brown, text="Button 5",font=myFont)
button6 = tk.Button(brown, text="Button 6",font=myFont)
button7 = tk.Button(brown, text="Button 7",font=myFont)
###################### Packing the Widgets ##########
###################### Plane 1 ######################
yellow_top.pack()
green.pack()
yellow_bottom.pack()
####################### Plane 2 #####################
label8.pack()
red.pack(side="left")
brown.pack(side="left")
label9.pack()
####################### Plane 3 #####################
button0.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
root.mainloop()
