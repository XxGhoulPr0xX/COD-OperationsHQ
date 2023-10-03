import random

lenguaje = input("Dame las letras del lenguaje: ")
secuencias = []
contenacion=[]
contador = 1


for _ in range(5):
    secuencia = ''.join(random.choice(lenguaje) for _ in range(random.randint(1, 5)))
    secuencias.append(secuencia)

print("\nSecuencias generadas:")
for secuencia in secuencias:
    print(secuencia, "--> |w", contador, "| =", len(secuencia))
    contenacion=[[secuencias[0]+secuencias[1]],[secuencias[3]+secuencias[4]],[secuencias[2]+secuencias[1]]]
    contador = contador + 1
print("w1*w2=",contenacion[0],"w4*w5=",contenacion[1],"w3*w2=",contenacion[2])