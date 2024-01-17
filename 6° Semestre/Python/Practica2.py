import tkinter as tk
from tkinter import messagebox
import math

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Programa Multifunción")

        self.seleccion = tk.StringVar()
        self.seleccion.set("Texto")

        opciones = ["Texto", "Numérico", "Juego"]
        menu = tk.OptionMenu(ventana, self.seleccion, *opciones)
        menu.pack(pady=10)

        boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=self.ejecutar_seccion)
        boton_ejecutar.pack()

    def ejecutar_seccion(self):
        seleccion = self.seleccion.get()

        if seleccion == "Texto":
            self.seccion_texto()
        elif seleccion == "Numérico":
            self.seccion_numerico()
        elif seleccion == "Juego":
            self.seccion_juego()

    def seccion_texto(self):
        pass

    def seccion_numerico(self):
        # Aquí implementar la lógica para la sección numérica
        pass

    def seccion_juego(self):
        # Aquí implementar la lógica para la sección de juego
        pass

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
