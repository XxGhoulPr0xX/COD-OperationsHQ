from cProfile import label
from tkinter import Tk, Label, Button

class VentanaEjemplo:
    def __init__(self,master):
        self.master= master
        master.title("Ejemplo de interaz grafica")

        self.etiqueta= label(master, text="Esta es mi primer ventana")
        self.etiqueta.pack()

        self.botonSaludo= Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()

        self.BotonCerrar=Button(master,text="cerrar", command=master.quit)
        self.BotonCerrar.pack()
