from tkinter import *

def Arboles():
        cedros=0
        oyamel=0
        pinos=0
        hectareas = int(txtHectareas.get())
        metros= hectareas*10000
        if(metros>1000000):
            pinos=metros*0.70
            oyamel=metros*0.20
            cedros=metros*0.10
        else:
            pinos=metros*(0.50);
            oyamel=metros*(0.30);
            cedros=metros*(0.20);
        lblCedros.config(text=cedros)
        lblOyamel.config(text=oyamel)
        lblPinos.config(text=pinos)

app = Tk()
app.title("Ejercicio 13")

#VP => Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

lblHectareas = Label(vp, text="Hectareas")
lblHectareas.grid(column=1,row=1,sticky=(W,E))

lblPinos = Label(vp, text="Pinos")
lblPinos.grid(column=1,row=2,sticky=(W,E))

lblOyamel = Label(vp, text="Oyamel")
lblOyamel.grid(column=1,row=3,sticky=(W,E))

lblCedros = Label(vp, text="Cedros")
lblCedros.grid(column=1,row=4,sticky=(W,E))

btnRespuesta = Button(vp, text="Respuesta", command=Arboles)
btnRespuesta.grid(column=1,row=5)

hectareas=""
txtHectareas= Entry(vp, width=10, textvariable = hectareas)
txtHectareas.grid(column=2,row=1)

app.mainloop()