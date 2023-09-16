import random
import threading
import time
arreglo1= []
arreglo2= []
arreglo3= []
arreglo4= []
arreglo5= []
def arreglo1():
    i =0
    num1 = random.randrange(10, 100, 1)
    while i<=num1+1:
       #time.sleep(n)
        arreglo1.append(random.randrange(200,500,1))
        print("[",i,"] = ",arreglo1[i])
        i+=1
    if(i==len(arreglo1)):
        print("El arreglo esta lleno")

def arreglo2(n):
    i =0
    num1 = random.randrange(10, 100, 1)
    while i<=num1+1:
        time.sleep(n)
        arreglo1.append(random.randrange(200,500,1))
        print("[",i,"] = ",arreglo2[i])
        i+=1
    if(i==len(arreglo1)):
        print("El arreglo esta lleno")

def arreglo3(n):
    i =0
    num1 = random.randrange(10, 100, 1)
    while i<=num1+1:
        time.sleep(n)
        arreglo1.append(random.randrange(200,500,1))
        print("[",i,"] = ",arreglo3[i])
        i+=1
    if(i==len(arreglo1)):
        print("El arreglo esta lleno")

def arreglo4(n):
    i =0
    num1 = random.randrange(10, 100, 1)
    while i<=num1+1:
        time.sleep(n)
        arreglo1.append(random.randrange(200,500,1))
        print("[",i,"] = ",arreglo4[i])
        i+=1
    if(i==len(arreglo1)):
        print("El arreglo esta lleno")

def arreglo5():
    i =0
    num1 = random.randrange(10, 100, 1)
    while i<=num1+1:
        time.sleep(n)
        arreglo1.append(random.randrange(200,500,1))
        print("[",i,"] = ",arreglo5[i])
        i+=1
    if(i==len(arreglo1)):
        print("El arreglo esta lleno")

def iniciador(n):
    t1 = threading.Thread(target=arreglo1, args=(n))
    t1.start()
    t2 = threading.Thread(target=arreglo2, args=(n))
    t2.start()
    t3 = threading.Thread(target=arreglo3, args=(n))
    t3.start()
    t4 = threading.Thread(target=arreglo4, args=(n))
    t4.start()
    t5 = threading.Thread(target=arreglo5, args=(n))
    t5.start()