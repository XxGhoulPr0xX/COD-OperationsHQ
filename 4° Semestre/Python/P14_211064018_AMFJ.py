from PaquetesNecesarios import Formulas
from tkinter import *

def CuadradoArea():
        l = int(txtLado.get())
        x = Formulas.CuadradoArea(l)
        lblArea.config(text=x)
def CuadradoPerimetro():
        l = int(txtLado.get())
        x = Formulas.CuadradoPerimetro(l)
        lblPerimetro.config(text=x)
def RectanguloArea():
        b = int(txtBase.get())
        h = int(txtAltura.get())
        x = Formulas.RectanguloArea(b,h)
        lblArea.config(text=x)
def RectanguloPerimetro():
        b = int(txtBase.get())
        h = int(txtAltura.get())
        x = Formulas.RectanguloPerimetro(b,h)
        lblPerimetro.config(text=x)
def TrainguloArea():
        b = int(txtBase.get())
        h = int(txtAltura.get())
        x = Formulas.TrainguloArea(b,h)
        lblArea.config(text=x)
def TrainguloPerimetro():
        b = int(txtBase.get())
        h = int(txtAltura.get())
        x = Formulas.TrainguloPerimetro(b,h)
        lblPerimetro.config(text=x)
def CirculoArea():
        r = int(txtRadio.get())
        x = Formulas.CirculoArea(r)
        lblArea.config(text=x)
def CirculoPerimetro():
        d = int(txtDiametro.get())
        x = Formulas.CirculoPerimetro(d)
        lblPerimetro.config(text=x)
app = Tk()
app.title("Ejercicio 12")

#VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

lblBase = Label(vp, text="Base")
lblBase.grid(column=1,row=1,sticky=(W,E))

lblAltura = Label(vp, text="Altura")
lblAltura.grid(column=1,row=2,sticky=(W,E))

lblDiametro = Label(vp, text="Diametro")
lblDiametro.grid(column=1,row=3,sticky=(W,E))

lblLado = Label(vp, text="Lado")
lblLado.grid(column=1,row=4,sticky=(W,E))

lblRadio = Label(vp, text="Radio")
lblRadio.grid(column=1,row=5,sticky=(W,E))

lblResultado = Label(vp, text="Resultado= ")
lblResultado.grid(column=3,row=3,sticky=(W,E))

lblArea = Label(vp, text="Area")
lblArea.grid(column=4,row=2,sticky=(W,E))

lblPerimetro = Label(vp, text="Perimetro")
lblPerimetro.grid(column=4,row=4,sticky=(W,E))

btnCuadradoArea = Button(vp, text="Cuadrado Area", command=CuadradoArea)
btnCuadradoArea.grid(column=1,row=6)

btnCuadradoPerimetro = Button(vp, text="Cuadrado Perimetro", command=CuadradoPerimetro)
btnCuadradoPerimetro.grid(column=1,row=7)

btnRectanguloArea = Button(vp, text="Rectangulo Area", command=RectanguloArea)
btnRectanguloArea.grid(column=1,row=8)

btn = Button(vp, text="Rectangulo Perimetro", command=RectanguloPerimetro)
btn.grid(column=1,row=9)

btnTrainguloArea = Button(vp, text="Cuadrado Area", command=TrainguloArea)
btnTrainguloArea.grid(column=2,row=6)

btnTrainguloPerimetro = Button(vp, text="Traingulo Perimetro", command=TrainguloPerimetro)
btnTrainguloPerimetro.grid(column=2,row=7)

btnCirculoArea = Button(vp, text="Circulo Area", command=CirculoArea)
btnCirculoArea .grid(column=2,row=8)

btnCirculoPerimetro = Button(vp, text="Circulo Perimetro", command=CirculoPerimetro)
btnCirculoPerimetro.grid(column=2,row=9)

base = ""
txtBase= Entry(vp, width=10, textvariable =base)
txtBase.grid(column=2,row=1)
altura = ""
txtAltura = Entry(vp, width = 10,textvariable=altura )
txtAltura.grid(column=2,row=2)
diametro = ""
txtDiametro= Entry(vp, width=10, textvariable =diametro)
txtDiametro.grid(column=2,row=3)
lado = ""
txtLado = Entry(vp, width = 10,textvariable=lado )
txtLado.grid(column=2,row=4)
radio = ""
txtRadio = Entry(vp, width = 10,textvariable=radio )
txtRadio.grid(column=2,row=5)

app.mainloop()