import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graficar:
    def __init__(self, frame):
        # Crear figura y eje
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Configurar límites de los ejes
        self.ax.set_xlim(0, 20)
        self.ax.set_ylim(0, 1)  # Ajustar el límite superior para acomodar la nueva línea

        # Inicialmente no hay datos en la gráfica
        self.line, = self.ax.plot([], [])
        self.counter = 0  # Inicializar el contador en 0

        # Crear el widget de lienzo para la gráfica
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)

        self.ax.axvline(x=6, color='black', linestyle='--')
        self.ax.axvline(x=12, color='black', linestyle='--')
        self.ax.axvline(x=18, color='black', linestyle='--')

    def dibujar(self, x, y):
        # Actualizar datos de la gráfica
        self.line.set_data(x, y)

        # Redibujar la gráfica
        self.ax.figure.canvas.draw()

    def actualizar_botones(self):
        # Habilitar o deshabilitar los botones según el valor del contador
        self.btn_avanzar["state"] = tk.NORMAL if self.counter < 3 else tk.DISABLED
        self.btn_atras["state"] = tk.NORMAL if self.counter> 0 else tk.DISABLED

    def avanzar(self):
        if self.counter < 3:  # Verificar el límite de 0
            self.counter += 1
            x = [0, self.counter * 6]  # Sumar 6 al eje x
            y = [0, 1]
            self.dibujar(x, y)
            self.actualizar_botones()

    def atras(self):
        if self.counter >= 0:  # Verificar el límite de 0
            self.counter -= 1
            x = [0, self.counter * 6]  # Restar 6 al eje x
            y = [0, 1]
            self.dibujar(x, y)
            self.actualizar_botones()

class Interfaz:
    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Practica 1")
        self.ventana.geometry("640x480")  # Establecer tamaño fijo de la ventana

        # Crear marco para el lado derecho
        self.frame_derecho = tk.Frame(self.ventana)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Crear marco para el lado izquierdo
        frame_izquierdo = tk.Frame(self.ventana)
        frame_izquierdo.pack(side=tk.LEFT)

        # Crear botones en el marco izquierdo
        self.beta = Graficar(self.frame_derecho)  # Crear una instancia de Graficar
        # Crear botones en el marco izquierdo
        self.beta.btn_avanzar = tk.Button(frame_izquierdo, text="Avanzar", command=self.beta.avanzar)
        self.beta.btn_avanzar.pack(pady=0, padx=50)  # Añadir espacio en la parte inferior

        self.beta.btn_atras = tk.Button(frame_izquierdo, text="Atras", command=self.beta.atras)
        self.beta.btn_atras.pack(pady=0, padx=50)  # Añadir espacio en la parte inferior

        self.beta.actualizar_botones()

    def run(self):
        self.ventana.mainloop()

class Principal:
    def disparador(self):
        alpha = Interfaz()
        alpha.run()

Charlie = Principal()
Charlie.disparador()

