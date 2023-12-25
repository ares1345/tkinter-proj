import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    entry_txt = entry.get()

    #Update label
    #label.configure(text='some other text') #modify a setting of said variable inside the widget
    #OR
    label['text'] = entry_txt
    entry['state'] = 'disabled' #would disable the widget


def button_func2():
    label["text"] = "some text"
    entry["state"] = 'enabled'


window = ttk.Window(themename = 'darkly') 
window.title("Getting and setting widgets")
window.geometry("800x500") #widthxheight

label = ttk.Label(master=window, text='text')
label.pack()

entry = ttk.Entry(master=window)
output_str = tk.StringVar() #helps to automatically gets the value inside of it
entry.pack()

button = ttk.Button(master=window, text ="button", command=button_func)
button.pack()

button2 = ttk.Button(master=window, text="something something", command=button_func2)
button2.pack()



window.mainloop()