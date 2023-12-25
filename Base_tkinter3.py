import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    print("t")

    #Update label
    label.config(text='some other text') #modify a setting of said variable inside the widget

window = ttk.Window(themename = 'darkly') 
window.title("Getting and setting widgetsgi")
window.geometry("800x500") #widthxheight

label = ttk.Label(master=window, text='text')
label.pack()

entry = ttk.Button(master=window)
output_str = tk.StringVar()
entry.pack()

button = ttk.Button(master=window, text ="buttton", command=button_func)
button.pack()



window.mainloop()