class Ejercicio11:
    def enteros_entre_numeros(self, num1, num2):
        if num1 < num2:
            enteros = []  # Lista para almacenar los enteros entre num1 y num2
            for i in range(num1 + 1, num2):
                enteros.append(i)  # Agregar el número actual a la lista
            return enteros  # Devolver la lista de enteros
        else:
            return "El primer número debe ser menor que el segundo. Por favor, inténtalo de nuevo."
        
    def main(self, num1, num2):
        return self.enteros_entre_numeros(num1, num2)


if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            alpha = Ejercicio11()
            print(alpha.main(num1, num2))
            break
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")
