# Desarrollar un programa que determine la suma de numeros pares y impares de un rango de m y n numeros
par=0
impares=0
m=int(input("Dame el primer numero para el rango: "))
n=int(input("Dame el segundo numero para el rango: "))
for i in range (m,n):
    if(i%2==0):
        print("Pares:",i)
        par=par+i
    else:
        print("Impares:",i)
        impares=impares+i
print("la suma total de numeros pares es: ",par," y La suma total de numeros impares es: ",impares)