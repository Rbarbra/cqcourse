import tkinter as tk
import tkinter.font as font

def convert_temp(conversion):
    conversion = conversion_option.get()
    value = int(entered_value.get())

    #label1.config(text=var2.get())
    if conversion == "fahrenheit2celsius":
        celsius = 5/9 * (value - 32)
        label.config(text=celsius)
    else:
        label.config(text="Not implemented")


root = tk.Tk()
myFont = font.Font(size=20)
root.title("Temperature converter")
root.geometry("500x200")
button_start = tk.Button(root,text="Start the conversion",command=convert_temp,font=myFont)
label1 = tk.Label(root,text="Empty",font=myFont)

conversion_option = tk.StringVar()
menu = tk.OptionMenu(root,conversion_option,"fahrenheit2,"celsius2celvin","tempC4","tempC5","tempC6","",command=convert_temp)


entered_value = tk.StringVar()
label1.config(text="empty")

entry1 = tk.Entry(root,textvariable=entered_value,font=myFont)
#packing
button_start.pack(side="bottom")
menu.pack(side="left")
label1.pack(side="right")
entry1.pack(side="right")
root.mainloop()
