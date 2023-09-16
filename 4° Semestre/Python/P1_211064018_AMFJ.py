import math
radio= int(input("Introduce el radio "))
altura= int(input("Introduce la altura "))
A=2*math.pi*radio*(radio+altura)
V=math.pi*(radio**2)*altura

print("El Área es: ",A)
print("El Volumen es: ",V)