import math
from tkinter import *


def hacer_click():
    try:
        _a = int(txt_X1.get())
        _b = int(txt_X2.get())
        _c = int(txt_X3.get())
        x = (math.pow(_b, 2)) - (4 * _a * _c)
        if x <= 0:
            etiqueta3.config(text="Raiz imaginaria")
            etiqueta4.config(text="Raiz imaginaria")
        else:
            x1 = (-(_b) + math.sqrt(x)) / (2 * _a)
            x2 = (-(_b) - math.sqrt(x)) / (2 * _a)
            etiqueta3.config(text=x1)
            etiqueta4.config(text=x2)
    except ValueError:
        etiqueta.config(text="Introduce solo números")


app = Tk()
app.title("Ejemplo2 GUI")

# VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Valor de a")
etiqueta.grid(column=2, row=2, sticky=(W, E))
etiqueta1 = Label(vp, text="Valor de b")
etiqueta1.grid(column=3, row=2, sticky=(W, E))
etiqueta2 = Label(vp, text="Valor de c")
etiqueta2.grid(column=4, row=2, sticky=(W, E))
etiqueta3 = Label(vp, text="X1")
etiqueta3.grid(column=6, row=1, sticky=(W, E))
etiqueta4 = Label(vp, text="X2")
etiqueta4.grid(column=6, row=2, sticky=(W, E))
boton = Button(vp, text="Resolver", command=hacer_click)
boton.grid(column=1, row=1)

a = ""
txt_X1 = Entry(vp, width=10, textvariable=a)
txt_X1.grid(column=2, row=1)
b = ""
txt_X2 = Entry(vp, width=10, textvariable=b)
txt_X2.grid(column=3, row=1)
c = ""
txt_X3 = Entry(vp, width=10, textvariable=c)
txt_X3.grid(column=4, row=1)

app.mainloop()
