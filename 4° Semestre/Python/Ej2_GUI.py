from tkinter import *

def hacer_click():
    #pass
    #_valor = txt_entrada.get()
    #etiqueta.config(text=_valor)
    try:
        _valor = int(txt_entrada.get())
        _valor = _valor * 10
        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Introduce solo números")

app = Tk()
app.title("Ejemplo2 GUI")

#VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta = Label(vp, text="Valor")
etiqueta.grid(column=2,row=2,sticky=(W,E))

boton = Button(vp, text="Click!", command=hacer_click)
boton.grid(column=1,row=1)

valor = ""
txt_entrada = Entry(vp, width=20, textvariable = valor)
txt_entrada.grid(column=2,row=1)

app.mainloop()