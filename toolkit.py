# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:38:28 2024

@author: Matheus
"""


import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
import math


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Arial", 10)
SMALL_FONT= ("Verdana", 8)

k = 1
a = 1
I_value = 1
TMS_value = 1
charac = "null"
S_value = 1
S_angle = 1
P_value = 1
Q_value = 1

#Defining overcurrent calculator
def calc_oc(TMS_input,I_input):
    global k
    global a
    TMS = float(TMS_input.get())
    I = float(I_input.get())
    charac = value_menu1.get()
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
    result1.config(text=t)
    return

def choose_charac(carac):
    global charac
    charac = carac    
    return

#Defining apparent to active and reactive power convertion
def calc_SPQ(S_value,S_angle):
    S_value = float(S_value.get())
    S_angle = float(S_angle.get())
    S_angle = math.acos(S_angle)
    P_value = S_value*math.cos(S_angle)
    Q_value = S_value*math.sin(S_angle)
    P.config(text=P_value)
    Q.config(text=Q_value)
    return

#Defining window and tabs
root = Tk()
root.title("Electrical Toolkit")
root.option_add('*tearOff', FALSE)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Overcurr. Calc.")
tabControl.add(tab2, text="S -> P,Q")

#--------------First tab--------------
intro1 = ttk.Label(tab1, text="Single point calculator - IEC-60255 Overcurrent\n", foreground="black", font="bold")
line11 = ttk.Label(tab1, text="Choose a characteristic curve")
options = ["---","Normally Inverse", "Very Inverse", "Extremely Inverse", "Long Time"]
value_menu1 = tk.StringVar(value='---')
menu1 = ttk.OptionMenu(tab1, value_menu1, *options)
line12 = ttk.Label(tab1, text="\nPlease enter the time multiplier (k): \n")
TMS_input = ttk.Entry(tab1)
line13 = ttk.Label(tab1, text="\nPlease enter the current multiplier (I/In): \n")
I_input = ttk.Entry(tab1)
line14 = ttk.Label(tab1, text="The operation time is [s]:")
result1 = ttk.Label(tab1, text="")
button1 = ttk.Button(tab1, text = "Calculate", command = lambda: calc_oc(TMS_input,I_input))

#Position management
intro1.grid(row=0, column=0, columnspan=2,sticky=N)
line11.grid(row=1, column=0, columnspan=2)
menu1.grid(row=2, column=0, columnspan=2)
line12.grid(row=3, column=0, sticky=W)
TMS_input.grid(row=3, column=1, padx=0)
line13.grid(row=5, column=0, sticky=W)
I_input.grid(row=5, column=1, padx=0)
button1.grid(row=8, column=0, columnspan=2)
line14.grid(row=10, column=0, columnspan=2)
result1.grid(row=11, column=0, columnspan=2)

#--------------Second tab--------------
intro2 = ttk.Label(tab2, text="Apparent, Active and Reactive Power convertor\n", foreground="black",font="bold")
line21 = ttk.Label(tab2, text="Please enter the magnitude for S [VA]: ")
S_value = ttk.Entry(tab2)
line22 = ttk.Label(tab2, text="Please enter the power factor: ")
S_angle = ttk.Entry(tab2)
line23 = ttk.Label(tab2, text="\nThe Active Power (P) is [W]:")
line24 = ttk.Label(tab2, text="\nThe Reactive Power (Q) is [VAr]:")
P = ttk.Label(tab2, text=" ")
Q = ttk.Label(tab2, text=" ")
button2 = ttk.Button(tab2, text = "Calculate", command = lambda: calc_SPQ(S_value,S_angle))

#Position management
intro2.grid(row=0, column=0, columnspan=2)
line21.grid(row=2, column=0, sticky=W)
S_value.grid(row=2, column=1, padx=0)
line22.grid(row=4, column=0, sticky=W)
S_angle.grid(row=4, column=1, padx=0)
button2.grid(row=6, column=0, columnspan=2)
line23.grid(row=8, column=0)
P.grid(row=9, column=0)
line24.grid(row=8, column=1)
Q.grid(row=9, column=1)


#signature = ttk.Label(tabControl, text="Developed by: Matheus Ruan Zimmermann - v1.0")
#signature.grid(row=0, column=0, sticky= "sw")
#signature.pack(fill=X, side=BOTTOM)

tabControl.pack(expand=1, fill=BOTH, side=TOP)

root.mainloop()
