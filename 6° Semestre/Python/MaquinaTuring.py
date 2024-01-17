'''una máquina de Turing es un modelo
teórico de una máquina que puede realizar
cálculos siguiendo un conjunto de reglas
predefinidas. Se compone de una cinta
infinitamente larga dividida en celdas,
una cabeza de lectura/escritura que se
mueve a lo largo de la cinta y un conjunto
finitos de estados. Cada celda de la cinta
contiene un símbolo, y la cabeza puede leer
y escribir sobre estas celdas.
La máquina de Turing funciona siguiendo
un programa que especifica qué hacer en
función del estado actual y el símbolo que
se encuentra bajo la cabeza. Puede realizar
acciones como escribir un símbolo nuevo,
moverse a la izquierda o derecha, o cambiar de
estado. La máquina repite este proceso hasta que
alcanza un estado de "aceptación" o "rechazo",
lo que determina si un cálculo se completa o no.
La máquina de Turing es un concepto fundamental
en la teoría de la computación y se utiliza para
demostrar qué problemas pueden resolverse
algorítmicamente y cuáles no. Es un modelo
abstracto pero poderoso que forma la base de
Muchas ideas en informática y programación.'''
import tkinter as tk

class MaquinaTuring:
    def __init__(self, programa, cinta):
        self.programa = programa
        self.cinta = cinta
        self.estado = 'q0'
        self.posicion_cabeza = 0

    def asegurar_tamano_cinta(self, tamaño):
        tamaño_actual = len(self.cinta)
        if self.posicion_cabeza < 0:
            # Mover la cabeza más allá del extremo izquierdo
            self.cinta = [' '] * (-self.posicion_cabeza) + self.cinta
            self.posicion_cabeza = 0
        elif self.posicion_cabeza >= tamaño_actual:
            # Mover la cabeza más allá del extremo derecho
            self.cinta += [' '] * (tamaño - tamaño_actual)

    def ejecutar(self):
        resultado = ""
        while self.estado != 'halt':
            símbolo = self.cinta[self.posicion_cabeza]
            transicion = self.programa.get((self.estado, símbolo))
            if transicion is None:
                resultado += f"No hay una transición válida para el estado: {self.estado} y el símbolo: {símbolo}\n"
                break
            nuevo_estado, nuevo_símbolo, dirección_movimiento = transicion
            self.cinta[self.posicion_cabeza] = nuevo_símbolo
            self.posicion_cabeza += 1 if dirección_movimiento == 'R' else -1
            self.estado = nuevo_estado
            self.asegurar_tamano_cinta(len(self.cinta) * 2)  # Ampliar automáticamente la cinta si es necesario
            resultado += f"{self.cinta}\n"
        return resultado

class MaquinaTuringGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Máquina de Turing")

        self.programa = {
            ('q0', '0'): ('q0', '0', 'R'),
            ('q0', '1'): ('q0', '1', 'R'),
            ('q0', ' '): ('q1', ' ', 'L'),
            ('q1', '0'): ('q2', '1', 'L'),
            ('q1', '1'): ('q2', '0', 'L'),
            ('q1', ' '): ('halt', ' ', 'R'),
            ('q2', '0'): ('q2', '0', 'L'),
            ('q2', '1'): ('q2', '1', 'L'),
            ('q2', ' '): ('q1', ' ', 'L'),
        }

        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack()

        self.label_cinta = tk.Label(self.frame, text="Contenido inicial de la cinta:")
        self.label_cinta.grid(row=0, column=0, columnspan=2, pady=10)

        self.entry_cinta = tk.Entry(self.frame)
        self.entry_cinta.grid(row=1, column=0, columnspan=2, pady=10)

        self.btn_iniciar = tk.Button(self.frame, text="Iniciar", command=self.iniciar_maquina_turing)
        self.btn_iniciar.grid(row=2, column=0, pady=10)

        self.btn_salir = tk.Button(self.frame, text="Salir", command=self.master.destroy)
        self.btn_salir.grid(row=2, column=1, pady=10)

        self.resultado_text = tk.Text(self.frame, height=10, width=40)
        self.resultado_text.grid(row=3, column=0, columnspan=2, pady=10)

    def iniciar_maquina_turing(self):
        entrada_cinta = self.entry_cinta.get()
        cinta_inicial = list(entrada_cinta)

        mt = MaquinaTuring(self.programa, cinta_inicial)
        resultado = mt.ejecutar()
        self.resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.resultado_text.insert(tk.END, resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = MaquinaTuringGUI(root)
    root.mainloop()