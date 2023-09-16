from tkinter import *


def hacer_click():
    pass
    _valor = txt_entrada.get()
    _Desc = txt_descuento.get()
    try:
        _valor = int(txt_entrada.get())
        _Desc = int(txt_descuento.get())
        _Desc = (_valor * _Desc) / 100
        res = _valor - _Desc
        etiqueta2.config(text=_Desc)
        etiqueta3.config(text=res)
    except ValueError:
        etiqueta.config(text="Introduce solo números")


app = Tk()
app.title("Ejemplo2 GUI")

"""VP => Ventana principal"""
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Valor del Medicamento")
etiqueta.grid(column=2, row=2, sticky=(W, E))
etiqueta1 = Label(vp, text="Descuento")
etiqueta1.grid(column=3, row=2, sticky=(W, E))
etiqueta2 = Label(vp, text="Descuento")
etiqueta2.grid(column=5, row=1, sticky=(W, E))
etiqueta3 = Label(vp, text="Total a pagar")
etiqueta3.grid(column=6, row=1, sticky=(W, E))
boton = Button(vp, text="Pagara", command=hacer_click)
boton.grid(column=1, row=1)

valor = ""
txt_entrada = Entry(vp, width=10, textvariable=valor)
txt_entrada.grid(column=2, row=1)
Desc = ""
txt_descuento = Entry(vp, width=10, textvariable=Desc)
txt_descuento.grid(column=3, row=1)

app.mainloop()
