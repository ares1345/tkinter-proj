# Créé par izemr, le 21/12/2023 en Python 3.7
import tkinter as tk
# from tkinter import ttk peut aussi etre utilise si ttkbootstrap pas installer
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get() #gets the value inside of entryInt, that was taken from entry widget, put it inside
    km_output = mile_input * 1.61
    output_str.set(km_output) #set/update the text inside of output_str






#window
window = ttk.Window(themename = 'darkly') 
window.title("Convertisseur miles à kilomètres")
window.geometry("480x150") #widthxheight

#title, this is called a widget
title_label = ttk.Label(master = window, #master is the container where we put it, in this case window
    text = "Miles to kilometers",
    font = "Calibri 24 bold")
title_label.pack() #serve to place this label inside of window variable, aka the value of master         No commas, can also add bold or italic after it



#input field
input_frame = ttk.Frame(master = window)
#type d'objet que l'on veut créer, dans ce cas Frame car on veut mettre d'autre elements dedans
entry_int = tk.IntVar() #create a variable to store and update values
entry = ttk.Entry(master = input_frame,
                textvariable = entry_int) #link the the widget with the variable



button = ttk.Button(master = input_frame,
                    text = "Convert",
                    command = convert)




entry.pack(side = 'left', padx = 10)
#we want to put this inside input_frame, note that tkinter puts it in order of entry
# You use padding with padx or pady, so in this case the horizontal line
button.pack(side = 'left') #same thing
#side = left helps to position the widgets, center is the default
input_frame.pack(pady = 10) #and we put this on the window




#output
output_str = tk.StringVar() #variable to store a string
output_label = ttk.Label(master = window,
    text = "Output",
    font = "Calibri 20",
    textvariable = output_str) #note that it overrides the str inside of text
output_label.pack(pady = 5)



#remember this that all widgets are stacked in function of the position of the pack methods
#DO NOT CALL FUNCTIONS IN command ARGUMENTS AKA DONT PUT THE () AT THE END OF THE FUNCTION

#run
window.mainloop()



