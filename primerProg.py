from tkinter import *
from tkinter.ttk import *

window = Tk() # Creacion de ventana

window.title("Chris Torres") # titulo de la ventana
window.geometry('350x200') # tamaño de la ventana


lbl = Label(window, text="Que onda", font=("Arial Bold",10)) # creacion label
lbl.grid(column=0, row=0) #ubicacion del label

txt = Entry(window, width=10)
txt.grid(column=1, row=0)



def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
    
    
btn = Button(window, text="Click me", bg="orange", fg="red", command=clicked)# creacion boton, bg = color de caja, fg = color de fuente
btn.grid(column=2, row=0) #ubicacion del boton

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=1)

window.mainloop() # ciclo infinito para que la ventana se mantega abierta



            
