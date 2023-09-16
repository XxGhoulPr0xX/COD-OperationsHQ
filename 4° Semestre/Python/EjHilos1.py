import threading

#Función a ejecutar
def cuenta(n, name):
    cont = n
    while cont < 10:
        print (cont,"-",name,"\n")
        cont += 1

def saludo(n, name):
    while n < 5:
        print("Hola")
        n += 1
 
#Procesos a ejecutar en paralelo
t = threading.Thread(target = cuenta, args=(5, 'thread-1'))
t2 = threading.Thread(target = saludo, args=(1, 'thread-2'))
t3 = threading.Thread(target = cuenta, args=(8, 'thread-3'))

#Se inician los hilos
t.start()
t2.start()
#t3.start()