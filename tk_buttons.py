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
#it is not necessary to write master =, the 1st argument is alr assumed to be the master variable
#reminder that textvariable overwrites text
button.pack()

#check buttons
check_var = tk.IntVar(value=10)
#value in this case make the checkbox checked or not

che_button = ttk.Checkbutton(window,
                            text="checkbox 1",
                            command=lambda: print(check_var.get()),
                            variable=check_var, #checkbuttons uses variables not textvariables
                            #AND stores the value of the checkbox
                            onvalue=10, #sets the value when its on
                            offvalue=5) #when its off
che_button.pack()










window.mainloop()