class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return str(self.valor)

def generar_arbol(niveles, valor_e, valor_f):
    raiz = Nodo("")
    nodos_actuales = [raiz]

    for nivel in range(niveles):
        nuevos_nodos = []
        for nodo in nodos_actuales:
            for valor in [valor_e, valor_f]:
                nuevo_nodo = Nodo(valor)
                nodo.agregar_hijo(nuevo_nodo)
                nuevos_nodos.append(nuevo_nodo)
        nodos_actuales = nuevos_nodos

    return raiz

def imprimir_arbol(arbol):
    nivel_actual = [arbol]
    while nivel_actual:
        nivel_siguiente = []
        for nodo in nivel_actual:
            print(nodo, end=" ")
            for hijo in nodo.hijos:
                nivel_siguiente.append(hijo)
        print()
        nivel_actual = nivel_siguiente

arbol = generar_arbol(5, "E", "F")
imprimir_arbol(arbol)
