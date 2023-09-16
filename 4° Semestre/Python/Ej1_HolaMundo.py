from tkinter import *

root = Tk()
root.config(width=300, height=200)
#creación de caja de texto
entry = Entry(root)
#posición de la caja de texto en relación a (X,Y)
entry.place(x=30, y=50)
entry.insert(0, "Hola mundo!")
#entry.insert("mundo!")
#entry.config(text="Hola mundo")
#Para justificar el texto usamos .RIGHT, .CENTER, .LEFT(por defecto)
entry = Entry(justify=CENTER)
root.mainloop()