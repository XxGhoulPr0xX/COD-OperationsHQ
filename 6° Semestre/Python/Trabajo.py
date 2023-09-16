arreglo = []
flag = True
conteo = {}
while flag:
    x = input("Ingresa un valor o escribe 'Terminalo' para finalizar: ")
    if x == "Terminalo":
        flag = False
    else:
        if x.isdigit():
            x = int(x)  # Convertir la entrada a un número entero
            arreglo.append(x)
            if abs(x) in conteo:
                conteo[abs(x)] += 1
            else:
                conteo[abs(x)] = 1
        else:
            arreglo.append(x)
            if x in conteo:
                conteo[x] += 1
            else:
                conteo[x] = 1
for dato, cantidad in conteo.items():
    if cantidad % 2 != 0:
        print(f"No hay par del'{dato}'")