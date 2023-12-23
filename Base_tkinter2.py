#temps video: 44:45

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("Editeur de texte")
window.geometry("800x500") #widthxheight

def button_func():
    print('test')



#ttk widgets
label = ttk.Label(master = window, text = "bruh")
label.pack()

# tkwidgets
textbox = tk.Text(master = window) #we put it inside window
textbox.pack(pady = 15)

#tk-entry
entry = ttk.Entry(master = window)
entry.pack()

label2 = ttk.Label(master=window, text="My label")
label2.pack()
button2 = ttk.Button(master=window, command=lambda: print("hello")) #lambda functions are undeclared functions
button2.pack()



#tk-button
button = ttk.Button(master=window, text= 'A button', command=button_func)
button.pack(pady = 10) 


window.mainloop() 
#updates the gui and checks for movements, make sure it is at the end of the file 
