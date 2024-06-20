import random

class Ejercicio13:
    def __init__(self):
        self.numeros_aleatorios=[]

    def generar_numeros_aleatorios(self):
        for _ in range(50):
            numero = random.randint(50, 500)
            self.numeros_aleatorios.append(numero)
        return self.numeros_aleatorios

    # Función para contar números pares e impares
    def contar_pares_impares(self,numeros):
        pares = 0
        impares = 0
        for numero in numeros:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        return pares, impares
    
    def main(self):
        numeros_aleatorios = self.generar_numeros_aleatorios()
        pares, impares = self.contar_pares_impares(numeros_aleatorios)
        return f"Números generados: {numeros_aleatorios}\nCantidad de números pares: {pares} \nCantidad de números impares: {impares}"

if __name__ == "__main__":
    alpha = Ejercicio13()
    print(alpha.main())