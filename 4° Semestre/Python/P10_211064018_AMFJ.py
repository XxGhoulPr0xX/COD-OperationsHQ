import math
from tkinter import *


def hacer_click():
    _valor = txt_entrada.get()
    _Po = txt_poo.get()
    try:
        _valor = int(txt_entrada.get())
        _Po = int(txt_poo.get())
        if _valor <= 0 and _Po <= 0:
            etiqueta.config(text="Error negativo")
        elif _valor == 0:
            etiqueta2.config(text="1")
        else:
            _valor = _valor ** _Po
            _valor = math.factorial(_valor)
            etiqueta2.config(text=_valor)
            if (_valor % 5) == 0:
                etiqueta3.config(text="si")
            else:
                etiqueta3.config(text="no")
    except ValueError:
        etiqueta.config(text="Introduce solo números")
        etiqueta1.config(text="Introduce solo números")


app = Tk()
app.title("Ejemplo2 GUI")

# VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Numero")
etiqueta.grid(column=2, row=2, sticky=(W, E))
etiqueta1 = Label(vp, text="Potencia")
etiqueta1.grid(column=3, row=2, sticky=(W, E))
etiqueta2 = Label(vp, text="Factorial")
etiqueta2.grid(column=5, row=1, sticky=(W, E))
etiqueta3 = Label(vp, text="Es multiplo de 5")
etiqueta3.grid(column=7, row=1, sticky=(W, E))

boton = Button(vp, text="Resolver", command=hacer_click)
boton.grid(column=1, row=1)

valor = ""
txt_entrada = Entry(vp, width=10, textvariable=valor)
txt_entrada.grid(column=2, row=1)
poo = ""
txt_poo = Entry(vp, width=10, textvariable=poo)
txt_poo.grid(column=3, row=1)

app.mainloop()
