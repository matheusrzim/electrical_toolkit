# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:38:28 2024

@author: Matheus
"""


import tkinter as tk
from tkinter import *


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

k = 1
a = 1
I_value = 1
TMS_value = 1
charac = "null"

def calc():
    global k
    global a
    TMS = float(TMS_input.get())
    I = float(I_input.get())
    charac = value_menu.get()
    if charac == "Normalmente Inversa":
        k = 0.14
        a = 0.02
    elif charac == "Muito Inversa":
        k = 13.5
        a = 1
    elif charac == "Extremamente Inversa":
        k = 80
        a = 2
    elif charac == "Tempo Longo":
        k = 120
        a = 1
    t = TMS*(k/((I ** a)-1))
    result.config(text=t)
    
def choose_charac(carac):
    global charac
    charac = carac    
    

window = Tk()
window.title("Overcurrent calculator")
frame1 = tk.Frame()
intro = Label(frame1, text="Single point calculator - IEC-60255 Overcurrent", foreground="black", background="white")
intro.grid(row=0, column=0)
line1 = Label(frame1, text="Choose a characteristic curve")
line1.grid(row=1, column=0)
options = ["Normally Inverse", "Very Inverse", "Extremely Inverse", "Long Time"]
value_menu = StringVar(value='---')
menu = OptionMenu(frame1, value_menu, *options).grid(row=2, column=0)

line2 = tk.Label(frame1, text="Please enter a time multiplier (k): \n").grid(row=3, column=0)
TMS_input = tk.Entry(frame1)
TMS_input.grid(row=4, column=0)

line3 = tk.Label(frame1, text="Please enter a current multiplier (I/In): \n").grid(row=5, column=0)
I_input = tk.Entry(frame1)
I_input.grid(row=6, column=0)


line4 = tk.Label(frame1, text="The operation time is (s):").grid(row=10, column=0)

result = Label(frame1, text="")
result.grid(row=11, column=0)

button = Button(frame1, text = "Calculate", command = lambda: calc()).grid(row=9, column=0)


signature = tk.Label(frame1, text="Developed by: Matheus Ruan Zimmermann - v1.0")
signature.grid(row=15, column=0, sticky= "sw")

frame1.grid()
window.mainloop()


    