import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

def button_func():
    print("t")


button_str = tk.StringVar()


button = ttk.Button(window, text="button", command=button_func, textvariable=button_str)
#it is not necessar to write master =, the 1st argument is alr assumed to be the master variable
#reminder that textvariable overwrites text
button.pack()









window.mainloop()