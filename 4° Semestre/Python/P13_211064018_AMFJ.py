from PaquetesNecesarios import Formulas
from tkinter import *


def hacer_click():
    a = int(txtA.get())
    b = int(txtB.get())
    x = Formulas.Hipotenusa(a, b)
    lblResultado.config(text=x)


app = Tk()
app.title("Ejercicio 11")

"""VP => Ventana principal"""
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

lblA = Label(vp, text="Valor de a")
lblA.grid(column=2, row=2, sticky=(W, E))

lblB = Label(vp, text="Valor de b")
lblB.grid(column=3, row=2, sticky=(W, E))

lblResultado = Label(vp, text="Respuesta")
lblResultado.grid(column=4, row=1, sticky=(W, E))

btnResolver = Button(vp, text="Resolver", command=hacer_click)
btnResolver.grid(column=1, row=1)

a = ""
txtA = Entry(vp, width=10, textvariable=a)
txtA.grid(column=2, row=1)
b = ""
txtB = Entry(vp, width=10, textvariable=b)
txtB.grid(column=3, row=1)

app.mainloop()
