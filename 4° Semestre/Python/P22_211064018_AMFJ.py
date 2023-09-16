from tkinter import *

def Factorial():
    numero  = int(txtNumero.get())
    i       = int(txtI.get())
    multiplicador=0
    for j in range (i+1):
        multiplicador=numero*j
    lblResultado.config(text=multiplicador)

app = Tk()
app.title("Factorial")

#VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

lblA = Label(vp, text="n")
lblA.grid(column=2,row=2,sticky=(W,E))

lblB = Label(vp, text="Factorial (n)")
lblB.grid(column=3,row=2,sticky=(W,E))

btnResolver = Button(vp, text="Resolver", command=Factorial)
btnResolver.grid(column=1,row=1)

lblResultado = Label(vp, text="")
lblResultado.grid(column=4,row=1,sticky=(W,E))

numero = ""
txtNumero= Entry(vp, width=10, textvariable =numero)
txtNumero.grid(column=2,row=1)
i = ""
txtI = Entry(vp, width = 10,textvariable=i )
txtI.grid(column=3,row=1)

app.mainloop()