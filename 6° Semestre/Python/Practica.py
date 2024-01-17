from matplotlib import pyplot as plt


puntos=[]
while True:
    a = int(input("Opcion"))
    if a == 1:
        while True:
            menu1 = int(input("Elige"))
            if menu1 == 1:
                i = int(input("dame A"))
                b = int(input("Dame b"))
                while i <= b:
                    if (i % 2) == 0:
                        print("El numero", i, " es par")
                    else:
                        print("El numero", i, " es impar")
                    i = i + 1  # o i += 1
                break
            elif menu1 == 2:
                print("Saliendo al menu principal")
                break
            else:
                print("Intentalo de nuevo")
                break
    elif a==2:
        while True:
            menu2=int(input())
            if menu2==1:
                print("Resolver la ecuacion de dos variables 3x+2y=?")
                x=int(input("Dame x"))
                y=int(input("Dame y"))
                resultado=(3*x)+(2*y)
                print(resultado)
                break
            if menu2==2:
                print("Salir")
                break
            else:
                print("Intentalo de nuevo")
    elif a==3:
        while True:
            menu3=int(input("Eligue"))
            if menu3==1:
                j=int(input("Dame a"))
                c = int(input("Las veces que se va repetir"))
                while j<=c:
                    es_primo = True
                    if j < 2:
                        es_primo = False
                    else:
                        for i in range(2, int(j**0.5) + 1):
                            if j % i == 0:
                                es_primo = False
                    if es_primo:
                        print("Es primo", j)
                    else:
                        print("No es primo", j)
                    j += 1
            elif menu3==2:
                print("Salir")
                break
            else:
                print("Intentalo de nuevo")
    elif a==4:
        while True:
            menu4=int(input("Eligue"))
            if menu4==1:
                h=int(input("Dame a"))
                k=int(input("Dame b"))
                while h<=k:
                    resultado=(3*h)+(2*h)
                    puntos.append((h, resultado))
                    h+=1
                if puntos:
                    xs, ys = zip(*puntos)  # Desempaqueta los puntos en listas separadas
                    plt.plot(xs, ys, marker='o', linestyle='-', color='b')
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.title('Gráfico de puntos')
                    plt.show()
            elif menu4==2:
                print("Salir")
                break
            else:
                print("Intentalo de nuevo")
    elif a==5:
        while True:
            menu5=int(input("Eligue"))
            if menu5==1:
                palabra=input("Dame la palabra ").lower()
                print("La palabra tiene un total de ", len(palabra)," Palabras")
                if "reprobados" in palabra:
                    print("La palabra 'reprobados' se encuentra en la cadena.")
                else:
                    print("La palabra 'reprobados' no se encuentra en la cadena.")
            elif menu5==2:
                print("salir")
                break
            else:
                print("Intentalo de nuevo")
    elif a==6:
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")
        