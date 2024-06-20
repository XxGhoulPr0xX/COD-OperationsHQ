class Ejercicio9:
    def __init__(self):
        self.contador_vocales = 0

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador

    def solicitar_caracteres(self):
        while self.contador_vocales < 5:
            caracter = input("Ingresa un caracter: ")
            self.contador_vocales += self.contar_vocales(caracter)
            if self.contador_vocales >= 5:
                return "Se han capturado un máximo de 5 vocales."
            else:
                print(f"Vocales capturadas: {self.contador_vocales}/5")

    def main(self):
        return self.solicitar_caracteres()

if __name__ == "__main__":
    alpha = Ejercicio9()
    print(alpha.main())
