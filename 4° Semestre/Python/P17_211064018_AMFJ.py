import threading
par=0
impar=0
def numeros():
    for i in range (1,21):
        print(i)
def imparPar():
    for i in range(1,21):
        if i%2==0:
            global par
            par=par+i
        else:
            global impar
            impar=impar+i
    print("La suma total de pares es ",par)
    print("la suma total de impares ",impar)

t1 = threading.Thread(target=numeros, args=())
t2= threading.Thread(target=imparPar(),args=())
t1.start()
t2.start()
