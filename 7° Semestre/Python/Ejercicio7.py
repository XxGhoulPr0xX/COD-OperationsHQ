import math

class Ejercicio7:
    def __init__(self):
        self.radio = None

    def calcular_perimetro_circunferencia(self, radio):
        self.radio = radio
        if self.radio > 0:
            perimetro = 2 * math.pi * radio
            return perimetro
        else:
            return "El radio debe ser mayor que cero."
        
    def main(self, radio):
        return self.calcular_perimetro_circunferencia(radio)

if __name__ == "__main__":
    radio = float(input("Ingresa el radio de la circunferencia: "))
    alpha = Ejercicio7()
    print(alpha.main(radio))
