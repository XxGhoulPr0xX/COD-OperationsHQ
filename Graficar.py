import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graficar:
    def __init__(self, frame):
        # Crear figura y eje
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Configurar límites de los ejes
        self.ax.set_xlim(0, 18)
        self.ax.set_ylim(0, 3)  # Ajustar el límite superior para acomodar la nueva línea

        # Inicialmente no hay datos en la gráfica
        self.pierna_der, = self.ax.plot([], [], color='black')
        self.pierna_izq, = self.ax.plot([], [], color='black')
        self.torso, = self.ax.plot([], [], color='black')
        self.cabeza = plt.Circle((0, 2.3), 0.3, color='black', fill=True)  # Agregar la circunferencia
        self.brazo_izq, = self.ax.plot([], [], color='black')
        self.brazo_der, = self.ax.plot([], [], color='black')

        self.counter = 0  # Inicializar el contador en 0

        # Crear el widget de lienzo para la gráfica
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)

        self.ax.axvline(x=6, color='black', linestyle='--')
        self.ax.axvline(x=12, color='black', linestyle='--')
        self.ax.axvline(x=18, color='black', linestyle='--')
        self.ax.add_artist(self.cabeza)  # Agregar la circunferencia a la gráfica
        self.ax.add_artist(self.brazo_izq)  # Agregar el brazo izquierdo a la gráfica
        self.ax.add_artist(self.brazo_der)  # Agregar el brazo derecho a la gráfica

    def dibujar(self, pierna_der_x, pierna_der_y, pierna_izq_x, pierna_izq_y, x3, y3, circle_x, circle_y, arm_izq_x, arm_izq_y, arm_der_x, arm_der_y):
        # Actualizar datos de la gráfica
        self.pierna_der.set_data(pierna_der_x, pierna_der_y)
        self.pierna_izq.set_data(pierna_izq_x, pierna_izq_y)
        self.torso.set_data(x3, y3)
        self.cabeza.center = (circle_x, circle_y)  # Actualizar la posición de la circunferencia
        self.brazo_izq.set_data(arm_izq_x, arm_izq_y)  # Actualizar posición del brazo izquierdo
        self.brazo_der.set_data(arm_der_x, arm_der_y)  # Actualizar posición del brazo derecho

        # Redibujar la gráfica
        self.ax.figure.canvas.draw()

    def actualizar_botones(self):
        # Habilitar o deshabilitar los botones según el valor del contador
        self.btn_avanzar["state"] = tk.NORMAL if self.counter < 9 else tk.DISABLED
        self.btn_atras["state"] = tk.NORMAL if self.counter > 0 else tk.DISABLED

    def avanzar(self):
        if self.counter < 9:  # Verificar el límite de 0
            self.counter += 1
            pierna_der_x = [self.counter * 2 - 2, self.counter * 2]  # Sumar 6 al eje x
            pierna_der_y = [0, 1]
            pierna_izq_x = [self.counter * 2 + 2, self.counter * 2]  # Sumar 6 al eje x
            pierna_izq_y = [0, 1]
            torso_x = [self.counter * 2, self.counter * 2]
            torso_y = [1, 2]
            cabeza_x = self.counter * 2  # Nueva posición x de la circunferencia
            cabeza_y = 2.3  # Nueva posición y de la circunferencia
            arm_izq_x = [torso_x[0], torso_x[0] - 1]  # Nueva posición x del brazo izquierdo
            arm_izq_y = [torso_y[0] + 0.5, torso_y[0]]  # Nueva posición y del brazo izquierdo
            arm_der_x = [torso_x[0], torso_x[0] + 1]  # Nueva posición x del brazo derecho
            arm_der_y = [torso_y[0] + 0.5, torso_y[0]]  # Nueva posición y del brazo derecho
            self.dibujar(pierna_der_x, pierna_der_y, pierna_izq_x, pierna_izq_y, torso_x, torso_y, cabeza_x, cabeza_y, arm_izq_x, arm_izq_y, arm_der_x, arm_der_y)
            self.actualizar_botones()

    def atras(self):
        if self.counter > 0:  # Verificar el límite de 0
            self.counter -= 1
            pierna_der_x = [self.counter * 2 - 2, self.counter * 2]  # Sumar 6 al eje x
            pierna_der_y = [0, 1]
            pierna_izq_x = [self.counter * 2 + 2, self.counter * 2]  # Sumar 6 al eje x
            pierna_izq_y = [0, 1]
            torso_x = [self.counter * 2, self.counter * 2]
            torso_y = [1, 2]
            cabeza_x = self.counter * 2  # Nueva posición x de la circunferencia
            cabeza_y = 2.3  # Nueva posición y de la circunferencia
            arm_izq_x = [torso_x[0], torso_x[0] - 1]  # Nueva posición x del brazo izquierdo
            arm_izq_y = [torso_y[0] + 0.5, torso_y[0]]  # Nueva posición y del brazo izquierdo
            arm_der_x = [torso_x[0], torso_x[0] + 1]  # Nueva posición x del brazo derecho
            arm_der_y = [torso_y[0] + 0.5, torso_y[0]]  # Nueva posición y del brazo derecho
            self.dibujar(pierna_der_x, pierna_der_y, pierna_izq_x,pierna_izq_y, torso_x, torso_y, cabeza_x, cabeza_y, arm_izq_x, arm_izq_y, arm_der_x, arm_der_y)
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

        self.beta = Graficar(self.frame_derecho)  # Crear una instancia de Graficar
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


if __name__ == "__main__":
    app = Principal()
    app.disparador()
