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
            self.cinta = [' '] * (tamaño - tamaño_actual) + self.cinta
            self.posicion_cabeza = 0
        elif self.posicion_cabeza >= tamaño_actual:
            # Mover la cabeza más allá del extremo derecho
            self.cinta += [' '] * (tamaño - tamaño_actual)

    def ejecutar(self):
        while self.estado != 'halt':
            símbolo = self.cinta[self.posicion_cabeza]
            if (self.estado, símbolo) not in self.programa:
                print("No hay una transición válida para el estado:", self.estado, "y el símbolo:", símbolo)
                break
            nuevo_estado, nuevo_símbolo, dirección_movimiento = self.programa[(self.estado, símbolo)]
            self.cinta[self.posicion_cabeza] = nuevo_símbolo
            if dirección_movimiento == 'R':
                self.posicion_cabeza += 1
            elif dirección_movimiento == 'L':
                self.posicion_cabeza -= 1
            self.estado = nuevo_estado
            self.asegurar_tamano_cinta(len(self.cinta) * 2)  # Ampliar automáticamente la cinta si es necesario
            print(self.cinta)

# Definición del programa
programa = {
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

# Contenido inicial de la cinta
entrada_cinta = input("Ingrese el contenido inicial de la cinta (0s y 1s, por ejemplo, '1100 1101'): ")
cinta_inicial = list(entrada_cinta)

# Inicializar y ejecutar la máquina de Turing
mt = MaquinaTuring(programa, cinta_inicial)
mt.ejecutar()