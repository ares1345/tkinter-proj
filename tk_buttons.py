import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("tkinter variables")
window.geometry("800x500") #widthxheight

def button_func():
    print("t")


def ex_func():
    print(radio_var.get())
    check_var.set(value=5)

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

che_button2 = ttk.Checkbutton(window,
                              text="Checkbutton 2",
                              command=lambda: print('test'))
che_button2.pack()



radio_var = tk.StringVar() #converts widgets values to strings if they are ints


#radio buttons
radio1 = ttk.Radiobutton(window,
                        text="Radiobutton 1",
                        value="radio 1",
                        command=lambda: print(radio_var.get()),
                        variable=radio_var)
radio1.pack() #radio buttons must have values and be different or else it breaks, default value is 0

radio2 = ttk.Radiobutton(window,
                        text="Radiobutton 2",
                        value="radio 2")
radio2.pack()


ex_r1 = ttk.Radiobutton(window,
                        value="A",
                        text="Radioo Button 1",
                        variable=radio_var,
                        command=ex_func)
ex_r1.pack()

ex_r2 = ttk.Radiobutton(window,
                        value="B",
                        text="Radioo Button 2",
                        variable=radio_var,
                        command=ex_func)
ex_r2.pack()


#video time: 1:24:00
#do the exercise






window.mainloop()