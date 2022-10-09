"""Qn2: objectoriented
Temperature conversion
Write a program for the six conversion of different temperature units into each
other. Generate a GUI for a program that handles these conversions.
The GUI should include at least the OptionMenu, an entry field for putting in a value,
 a label in which the result is printed and a button that starts the conversion.
 Use the definitions below for your implementation:
Celsius = 5/9 * (Fahrenheit - 32).
Celsius = Kelvin - 273.15.
The lowest possible temperature is 0K."""

import tkinter as tk
import tkinter.font as font

# Declaration of variable which are global
temp_Val = "Celsius"


#first setting my drop down value
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

# Function for converting temperature
def convert_temp():
    temp = inputnumber.get()

    if temp_Val == "Fahrenheit-Celsius":

       # Conversion of fahrenheit temperature to celsius
       c = float((float(temp)-32) * 5/9)
       result_label.config(text =f"wow you converted Celsius to Fahrenheit: {c}")

       #converting celsius to fahrenheit
    elif temp_Val == "Celsius-Fahrenheit":
        # Conversion of Celsius temperature to Fahrenheit
        f = float((float(temp) * 9/5) + 32)
        result_label.config(text =f"wow you converted fahrenheit to Celsius: {f} ")
        #converting kelvin to celsius
    elif temp_Val == "Kelvin-Celsius":
        # Conversion of kelvin temperature to celsius
        c = float((float(temp) - 273.15))
        result_label.config(text =f"wow you converted kelvin to celsius: {c}")

        #converting celsius to kelvin
    elif temp_Val == "Celsius-Kelvin":
        # Conversion of celsius temperature to kelvin
        k = float((float(temp) + 273.15))
        result_label.config(text =f"wow you converted celsius to kelvin: {k} ")

        #converting kelvin to fahrenheit
    elif temp_Val == "Kelvin-Fahrenheit":

        # Conversion of kelvin temperature to fahrenheit
        f = float((float(temp)-273.15)*1.8 + 32)
        result_label.config(text =f"wow you converted Kelvin to Fahrenheit: {f}")

      #converting fahrenheit to kelvin
    elif temp_Val == "Fahrenheit-Kelvin":

        # Conversion of fahrenheit temperature to Kelvin
        k = float((float(temp) - 32) * 5/9 + 273.15)
        result_label.config(text =f"wow you converted fahrenheit to Kelvin: {k} ")
####################
root = tk.Tk()
myFont = font.Font(size=20)
root.title("Temperature converter")
root.geometry("700x300")
 #Lay out widgets
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(1, weight = 1)
###################
inputnumber = tk.DoubleVar()
var = tk.DoubleVar()
##################
#creating label and field entry
label_input = tk.Label(root,text="Enter Temperature",font=myFont)
result_label = tk.Label(root)
result_label.grid(row = 3, columnspan = 4)
input_entry = tk.Entry(root, textvariable = inputnumber,font=myFont)
input_entry.grid(row = 1, column = 1)
##################
dropDownList = ["Fahrenheit-Celsius", "Celsius-Fahrenheit","Kelvin-Celsius","Celsius-Kelvin","Kelvin-Fahrenheit","Fahrenheit-Kelvin"]
drop_down = tk.OptionMenu(root, var, *dropDownList, command = store_temp)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)
##################
button_return = tk.Button(root,text="convert",command=convert_temp,font=myFont)
button_return.grid(row = 2, columnspan = 2)
###################
root.mainloop()
