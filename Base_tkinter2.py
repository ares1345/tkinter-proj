#temps video: 33:07

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly') 
window.title("Editeur de texte")
window.geometry("800x500") #widthxheight

#ttk widgets
label = ttk.Label(master = window, text = "bruh")
label.pack()



# tkwidgets
textbox = tk.Text(master = window) #we put it inside window
textbox.pack(pady = 15)



window.mainloop() 
#updates the gui and checks for movements, make sure it is at the end of the file 
