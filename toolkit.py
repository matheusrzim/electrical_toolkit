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
S_angle = 0
P_value = 1
Q_value = 1
V_value = 1
V_angle = 0
I_value = 1
I_angle = 0

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

#Defining voltage and current to apparent, active and reactive power convertion
def calc_VIS(V_value,V_angle,I_value,I_angle):
    
    return

#Defining window and tabs
root = Tk()
root.title("Electrical Toolkit")
root.option_add('*tearOff', FALSE)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Overcurr. Calc.")
tabControl.add(tab2, text="S -> P,Q")
tabControl.add(tab3, text="V,I -> S,P,Q")

#--------------First tab--------------
intro1 = ttk.Label(tab1, text="\nSingle point calculator - IEC-60255 Overcurrent\n", foreground="black", font="bold")
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
intro2 = ttk.Label(tab2, text="\nApparent, Active and Reactive Power convertor\n", foreground="black",font="bold")
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

#--------------Third tab--------------
intro3 = ttk.Label(tab3, text="\nVoltage and Current to Apparent, Active and Reactive Power convertor\n", foreground="black",font="bold")
line31 = ttk.Label(tab3, text="Please enter the magnitude for V [V]: ")
V_value = ttk.Entry(tab3)
line32 = ttk.Label(tab3, text="Please enter the angle for V [degrees]: ")
V_angle = ttk.Entry(tab3)
line33 = ttk.Label(tab3, text="Please enter the magnitude for I [A]: ")
I_value = ttk.Entry(tab3)
line34 = ttk.Label(tab3, text="Please enter the angle for I [degrees]: ")
I_angle = ttk.Entry(tab3)
line35 = ttk.Label(tab3, text="The Apparent Power (S) is [VA]:")
line36 = ttk.Label(tab3, text=" º")
line37 = ttk.Label(tab3, text="\nThe Active Power (P) is [W]:")
line38 = ttk.Label(tab3, text="\nThe Reactive Power (Q) is [VAr]:")
S1 = ttk.Label(tab3, text=" ")
SA1 = ttk.Label(tab3, text=" ")
P1 = ttk.Label(tab3, text=" ")
Q1 = ttk.Label(tab3, text=" ")
button3 = ttk.Button(tab3, text = "Calculate", command = lambda: calc_VIS(V_value,V_angle,I_value,I_angle))

#Position management
intro3.grid(row=0, column=0, columnspan=3)
line31.grid(row=2, column=0, sticky=W)
V_value.grid(row=2, column=1, padx=0)
line32.grid(row=4, column=0, sticky=W)
V_angle.grid(row=4, column=1, padx=0)
line33.grid(row=6, column=0, sticky=W)
I_value.grid(row=6, column=1, padx=0)
line34.grid(row=8, column=0, sticky=W)
I_angle.grid(row=8, column=1, padx=0)
line35.grid(row=10, column=0)
S1.grid(row=10, column=1)
SA1.grid(row=10, column=2, sticky=W)
line36.grid(row=10, column=3)
line37.grid(row=12, column=0)
P1.grid(row=12, column=1)
line38.grid(row=14, column=0)
Q1.grid(row=14, column=1)
button3.grid(row=9, column=0, columnspan=2)

#signature = ttk.Label(tabControl, text="Developed by: Matheus Ruan Zimmermann - v1.0")
#signature.grid(row=0, column=0, sticky= "sw")
#signature.pack(fill=X, side=BOTTOM)

tabControl.pack(expand=1, fill=BOTH, side=TOP)

root.mainloop()
