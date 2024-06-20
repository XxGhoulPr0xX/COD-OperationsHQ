import random

class OptimizacionLocal:
    def _init_(self):
        pass

    def generarSolucion(self):
        return random.uniform(0, 10)

    def hillClimbing(self, funcion_objetivo, max_iter):
        mejor_s = self.generarSolucion()
        mejor_v = eval(funcion_objetivo.replace('x', str(mejor_s)))

        for _ in range(max_iter):
            nueva_solucion = mejor_s + random.uniform(-0.1, 0.1)
            nuevo_valor = eval(funcion_objetivo.replace('x', str(nueva_solucion)))

            if nuevo_valor > mejor_v:
                mejor_s = nueva_solucion
                mejor_v = nuevo_valor

        return mejor_s, mejor_v

    def toString(self, funcion_objetivo, max_iter):
        x, y = self.hillClimbing(funcion_objetivo, max_iter)
        return f"Con este programa se busca buscar de forma optimizada los números para resolver una función cuadrática usando un algoritmo llamado hillClimbing. Utilizando {max_iter} iteraciones, se encontró que la solución óptima es: x = {x}, y = {y}, y la función objetivo es: {funcion_objetivo}"

if __name__ == "__main__":
    alpha = OptimizacionLocal()
    funcion_objetivo = input("Ingrese la función objetivo (utilice 'x' como la variable independiente): ")
    max_iter = int(input("Ingrese el número máximo de iteraciones: "))
    print(alpha.toString(funcion_objetivo, max_iter))
