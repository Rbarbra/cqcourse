import tkinter as tk
import tkinter.font as font

#creating a button
def ChangeText1():
    label1.config(text="open button")



def check_button_check():
    Checking_status_1 = checkValue_1.get()
    Checking_status_2 = checkValue_2.get()
    Checking_status_3 = checkValue_3.get()
    #if checkValue_1.get() = True
    #a = "checked"
    #else:
    # a= "unchecked"

    if Checking_status_1
        a = "checked"

    else:
        a = "Unchecked"

    if Checking_status_2
        b = "checked"

    else:
        b = "Unchecked"

    if Checking_status_3
        c = "checked"

    else:
        c = "Unchecked"

    label_status.config(font=myFont, text=
    f" checkbox 1 is {a},\n\
    checkbox 2 is {b},\n\
    checkbox 3 is {c},\n")



creating labels
root = tk.Tk()
label1 = tk.Label(root, text = "click the button" )
label1.pack()
button1 = tk.Button(root, text="", command=ChangeText1)
button1.pack()

#creating check buttons
myFont = font.Font(size=10)
root.geometry("500x100")
checkValue = tk.BooleanVar()
checkValue.set(True)
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue,font=myFont)
check1.pack(side="left")
button1 = tk.Button(root,text="Check your input",width=80,fg="blue",bg="grey",command=Print_Check,font=myFont)
button1.pack(side="right")
root.mainloop()









root.mainloop()
