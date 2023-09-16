import math
datos=input("Ingresa los valores: ")
res= float(datos)
if datos[0:1]==0:
    print("No debe ser cero: A")
    raiz1: float=math.sqrt((datos[2:]**2)-(datos[1:2]**2))
    print("lol")
elif datos[1:2]==0:
    print("No debe ser cero: B")
elif datos[2:]==0:
    print("No debe ser cero: C")
else:
    raiz4= math.sqrt((datos[0:1]**2)+(datos[1:2] ** 2))