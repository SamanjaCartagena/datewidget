# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:26:54 2024

@author: c.samanja09
"""

from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root=tb.Window(themename='darkly')
root.title("TTK Bootstrap")
root.geometry('500x350')


counter = 0
def changer() :
    global counter
    counter += 1
    if counter % 2 ==0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Goodbye World")

# Create a label
my_label = tb.Label(text="Hello World!", font=("Helvetica",28),bootstyle="danger,inverse")

my_label.pack(pady=50)

my_button=tb.Button(text="Click Me!", 
                    bootstyle="success, outline", command=changer)
my_button.pack(pady=20)

root.mainloop()