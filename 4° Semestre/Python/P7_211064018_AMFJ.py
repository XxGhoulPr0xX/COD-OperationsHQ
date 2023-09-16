año= int(input("Ingresa un número: "))
if año <= 12:
    print("Es un niño")
elif año <= 13 and año<=17:
    print("Adolescente")
elif año <= 18 and año<=25:
    print("Joven")
elif año <= 26 and año<=55:
    print("Adulto")
elif año > 56:
    print("Mayor Adulto")
else:
    print("Error de edad")