import threading
import time

def print_time(n, name):
    cont = 0
    while cont < 5:
        time.sleep(n)
        cont += 1
        print(cont, "%s: %s" % (name, time.ctime(time.time())))
        
try:
    t1 = threading.Thread(target=print_time, args=(3,"Hilo1", ))
    t2 = threading.Thread(target=print_time, args=(8,"Hilo2", ))
except:
    print("No se pudo ejecutar el hilo")


t1.start()
t2.start()