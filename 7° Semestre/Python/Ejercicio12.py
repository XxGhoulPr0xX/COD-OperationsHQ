class Ejercicio12:

    def calcular_costo_banquete(self,num_personas):
        if num_personas <= 200:
            costo_por_persona = 95.00
        elif num_personas <= 300:
            costo_por_persona = 85.00
        else:
            costo_por_persona = 75.00
        costo_total = num_personas * costo_por_persona
        return costo_total

    def main(self,numPersonas):
        while True:
            try:
                if numPersonas > 0:
                    return f"El costo total del banquete para {num_personas} personas es de $ {self.calcular_costo_banquete(num_personas)}"
                    break
                else:
                    return "El número de personas debe ser mayor que cero. Inténtelo de nuevo."
            except ValueError:
                return "Por favor, ingrese un número válido."


if __name__ == "__main__":
    while True:
        try:
            num_personas = int(input("Ingrese el número de personas asistentes al banquete: "))
            alpha = Ejercicio12()
            print(alpha.main(num_personas))
            break
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")
