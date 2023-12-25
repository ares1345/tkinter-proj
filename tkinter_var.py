import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

label = ttk.Label(master=window, text="test")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()










window.mainloop()
