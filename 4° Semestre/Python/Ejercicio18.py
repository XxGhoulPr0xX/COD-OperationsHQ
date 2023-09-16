import threading
import time

def compañia(n,name,llamar):
    print("Llamando a la compañia..",name)
    if(llamar==1):
        time.sleep(n)
        i = 0
        valor = 0
        while i<=n:
            valor=valor+1
            i+=1
        print("La compañia contesto..", name)
        print("La llamada a terminado..", valor)
    if(llamar==2):
        time.sleep(n)
        o = 0
        tiempo = 0
        while o <= n:
            tiempo = tiempo + 1
            o += 1
        print("La compañia de telefono ", name, " no contesto..", )
        print("La llamada ha estado en espera..", tiempo)

def iniciador(n,name,llamar):
        t1 = threading.Thread(target=compañia, args=(n,name,llamar))
        t1.start()