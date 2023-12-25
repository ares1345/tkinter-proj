import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

button = ttk.Button(window, text="button")
#it is not necessar to write master =, the 1st argument is alr assumed to be the master variable









window.mainloop()