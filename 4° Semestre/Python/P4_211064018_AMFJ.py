import random
tamaño=50
for i in range(tamaño):
    numero = random.randrange(1, 100, 1)
    print("el obrero ",i+1," ha trabajado un total de ",numero," Horas")
    trabajadores=numero
    total=150*trabajadores
    print("al trabajador",i+1,"se le debe pagar ",total)