from tkinter import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

def Ejercicio20():
    exec(open("P20_211064018_AMFJ.py").read())
def Ejercicio21():
    exec(open("P21_211064018_AMFJ.py").read())
def Ejercicio22():
    exec(open("P22_211064018_AMFJ.py").read())
app = Tk()
app.title("Interfaz General P20")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

btnEjercicio11 = Button(vp, text="Contador Creciente", command=Ejercicio20)
btnEjercicio11.grid(column=1,row=3)

btnEjercicio12 = Button(vp, text="Contador Decreciente", command=Ejercicio21)
btnEjercicio12.grid(column=1,row=4)

btnEjercicio13 = Button(vp, text="Factorial", command=Ejercicio22)
btnEjercicio13.grid(column=1,row=5)

app.mainloop()
