from tkinter import *

def Ejercicio13():
    exec(open("../Ejercicios/P13_211064018_AMFJ.py").read())
def Ejercicio14():
    exec(open("../Ejercicios/P14_211064018_AMFJ.py").read())
def Ejercicio15():
    exec(open("../Ejercicios/P15_211064018_AMFJ.py").read())
app = Tk()
app.title("Interfaz General 13,14,15")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

btnEjercicio11 = Button(vp, text="Ejercicio 11", command=Ejercicio13)
btnEjercicio11.grid(column=1,row=3)

btnEjercicio12 = Button(vp, text="Ejercicio 12", command=Ejercicio14)
btnEjercicio12.grid(column=1,row=4)

btnEjercicio13 = Button(vp, text="Ejercicio 13", command=Ejercicio15)
btnEjercicio13.grid(column=1,row=5)

app.mainloop()