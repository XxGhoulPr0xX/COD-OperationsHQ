from tkinter import *

def hacer_click():
    pass
    _valor = txt_entrada.get()

    try:
        _valor = int(txt_entrada.get())

        C=(_valor*9/5)+32
        F=(_valor-32)*5/9
        etiqueta2.config(text=C)
        etiqueta3.config(text=F)
    except ValueError:
        etiqueta.config(text="Introduce solo números")

app = Tk()
app.title("C°--->F \nF°--->C°")

#VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
#vp.columnconfigure(0,weight=1)
#vp.rowconfigure(0,weight=1)

etiqueta = Label(vp, text="Ingrese Datos")
etiqueta.grid(column=2,row=2,sticky=(W,E))

etiqueta2 = Label(vp, text="Celsius")
etiqueta2.grid(column=5,row=1,sticky=(W,E))
etiqueta3 = Label(vp, text="Fahrenheit")
etiqueta3.grid(column=6,row=1,sticky=(W,E))
boton = Button(vp, text="Convertir", command=hacer_click)
boton.grid(column=1,row=1)

valor = ""
txt_entrada = Entry(vp, width=10, textvariable = valor)
txt_entrada.grid(column=2,row=1)


app.mainloop()