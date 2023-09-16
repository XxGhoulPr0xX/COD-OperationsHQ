import math

while True:
    try:
        a = int(input("Inicio dame uno de los siguientes valores \n1.Ejercicio \n2.Ejercicio \n3.Ejercicio \n4.ejercicio \n5.ejercicio \n6.Salir \n"))
        if a==1:
            while True:
                auser=int(input("Producto \n1.resolver \n2.salir\n"))
                if auser==1:
                    numero1 = int(input("Dame x"))
                    ecuacion1 = (numero1-6)/10
                    print("Ecuacion resulta es:", ecuacion1)
                if auser==2:
                    print("Menu principal")
                    break
                if auser>2:
                    print("Dame un valor valido")
        if a==2:
            while True:
                    auser = int(input("Producto \n1.resolver \n2.salir\n"))
                    if auser == 1:
                        numero2 = int(input("Dame x"))
                        ecuacion2 = (numero2-9)/6
                        print("Ecuacion resulta es:", ecuacion2)
                    if auser == 2:
                        print("Menu principal")
                        break
                    if auser > 2:
                        print("Dame un valor valido")
        if a==3:
            while True:
                auser=int(input("Producto \n1.resolver \n2.salir\n"))
                if auser==1:
                    numero3 = int(input("Dame para el primero y"))
                    numero31 = int(input("Dame para el segundo y"))
                    numero32 = int(input("Dame para el tercero y"))
                    ecuacion3 = 2 + 2 + 5 * (numero3)
                    ecuacion31 = 2 + 2 + 5 * (numero31)
                    ecuacion32 = 2 + 2 + 5 * (numero32)
                    print("Ecuacion resulta es: ", ecuacion3,ecuacion31,ecuacion32)
                if auser==2:
                    print("Menu principal")
                    break
                if auser>2:
                    print("Dame un valor valido")
        if a==4:
            while True:
                auser=int(input("Producto \n1.resolver \n2.salir\n"))
                if auser==1:
                    numero4 = int(input("Dame el primer x"))
                    numero41 = int(input("Dame el segundo x"))
                    numero42 = int(input("Dame el tercer x"))
                    ecuacion4 = 2 * math.sqrt(numero4)
                    ecuacion41 = 2 * math.sqrt(numero41)
                    ecuacion42 = 2 * math.sqrt(numero42)
                    print("La ecuacion resulta es: ",ecuacion4,ecuacion41,ecuacion42)
                if auser==2:
                    print("Menu principal")
                    break
                if auser>2:
                    print("Dame un valor valido")
        if a==5:
            while True:
                auser=int(input("Producto \n1.resolver \n2.salir\n"))
                if auser==1:
                    while True:
                        numero5 = int(input("X"))
                        ecuacion5 = (numero5 - 10) / 3
                        if -15 <= ecuacion5 <= 15:
                            print("Lo que resuelve la ecuacion es: ", ecuacion5)
                            break
                        else:
                            print("El resultado no está dentro del rango permitido intentalo de nuevo")
                if auser==2:
                    print("Menu principal")
                    break
                if auser>2:
                    print("Dame un valor valido")
        if a>5:
            print("Adios")
            break
    except ValueError:
        print("Eso no es un numero")