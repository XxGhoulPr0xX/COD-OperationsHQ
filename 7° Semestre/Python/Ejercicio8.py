class Ejercicio8:
    def __init__(self):
        self.base = None
        self.altura = None

    def calcular_area_rectangulo(self, base, altura):
        return base * altura

    def calcular_perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

    def tabla_multiplicar(self, numero):
        resultado = ""
        for i in range(1, 11):
            resultado += f"{numero} x {i} = {numero * i}\n"
        return resultado

    def main(self, b, a):
        self.base = b
        self.altura = a
        area = self.calcular_area_rectangulo(b, a)
        perimetro = self.calcular_perimetro_rectangulo(b, a)
        area_table = self.tabla_multiplicar(area)
        perimetro_table = self.tabla_multiplicar(perimetro)
        return  f"El rectángulo tiene una base de {b} y una altura de {a},\n" \
                f"así mismo tiene un área de: {area} y un perímetro de {perimetro}.\n" \
                f"Tabla de multiplicar del área:\n{area_table}\n" \
                f"Tabla de multiplicar del perímetro:\n{perimetro_table}"


if __name__ == "__main__":
    base_rectangulo = float(input("Ingresa la base del rectángulo: "))
    altura_rectangulo = float(input("Ingresa la altura del rectángulo: "))
    alpha = Ejercicio8()
    print(alpha.main(base_rectangulo, altura_rectangulo))
