import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

string_var = tk.StringVar(value="test") #or IntVar, BooleanVar, DoubleVar
#value sets the default value of said variable



label = ttk.Label(master=window, text="label", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()










window.mainloop()
