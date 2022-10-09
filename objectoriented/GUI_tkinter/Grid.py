"""
This is the example for working with grid
"""

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("420x170")
root.title("Login")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(100, weight=3)
username_label = tk.Label(root, text="Username:",font=myFont)
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
username_entry = tk.Entry(root,font=myFont)
username_entry.grid(column=100, row=0, sticky=tk.E, padx=5, pady=5)
password_label = tk.Label(root, text="Password:",font=myFont)
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = tk.Entry(root, show="*",font=myFont)
password_entry.grid(column=100, row=1, sticky=tk.E, padx=5, pady=5)
login_button = tk.Button(root, text="Login",font=myFont)
login_button.grid(column=100, row=3, sticky=tk.E, padx=5, pady=5)
root.mainloop()