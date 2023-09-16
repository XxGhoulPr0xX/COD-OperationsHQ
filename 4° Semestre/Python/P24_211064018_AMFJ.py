import random
import threading
import time

suma=0
resta=100
factorial=0
def sumando():
    global suma
    for i in range(101):
        suma=i
        print(suma)
    time.sleep(random.randrange(1, 10, 1))
    print(suma)
def restando():
    global resta
    for i in range(101):
        j=resta-i
        print(j)
    time.sleep(random.randrange(1, 10, 1))
    print(j)
def factorial():
    n=random.randrange(1,10,1)
    numero=random.randrange(1,10,1)
    for i in range(n+1):
        multiplicador=numero*i
    time.sleep(random.randrange(1, 10, 1))
    print("n",numero,"factorial (n)",n,"=",multiplicador)
t1 = threading.Thread(target=sumando(), args=())
t2= threading.Thread(target=restando(),args=())
t3= threading.Thread(target=factorial(), args=())
t1.start()
t2.start()
t3.start()
