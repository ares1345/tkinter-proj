import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

def button_func():
    print(string_var.get())
    string_var.set('button pressed')


string_var = tk.StringVar() #or IntVar, BooleanVar, DoubleVar
#value = "txt" sets the default value of said variable, in the ()



label = ttk.Label(master=window, text="label", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()










window.mainloop()
