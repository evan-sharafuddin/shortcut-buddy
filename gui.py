# https://www.pythonguis.com/tutorials/create-gui-tkinter/

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Shortcut Buddy")
root.minsize(200, 200)  # width, height
width, height = 400, 300
root.geometry(f"{width}x{height}+{(root.winfo_screenwidth() - width) // 2}+{(root.winfo_screenheight() - height) // 2}")

# title
title = Label(root, text="Welcome to Shortcut Buddy!", font=("Yu Gothic Light", 24))
title.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

# subheading

root.mainloop()
