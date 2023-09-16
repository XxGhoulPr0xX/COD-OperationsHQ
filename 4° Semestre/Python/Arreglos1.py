n1=5
n2=6
n3=7
n4=8
n5=9

datos=[5,6,7,8,9]
datos.append(15)
print("Datos 0 y 2")
print(datos[0])
print(datos[2])

print("Todos los datos")
for i in range(0,6):#len es la longitud del arreglo, para agregar datos al arreglo se usa append
    print(datos[i])

print("Todos los datos al revés")
for i in range (5, -1, -1):
    print(datos[i])