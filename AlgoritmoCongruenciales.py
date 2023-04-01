import copy

class cm:
    def __init__(self,semilla,n):
        self.estado=semilla
        self.n=n

    def x(self,i):
        elevado = self.estado[i] ** 2
        num_str = str(elevado)
        if len(num_str) % 2 != 0:
            num_str = '0' + num_str
        medio = len(num_str) // 2
        arreglo = [int(digito) for digito in num_str[medio - 2:medio + 2]]
        self.numero_separado = int(''.join(str(digito) for digito in arreglo))
        self.estado.append(self.numero_separado)
        return self.numero_separado

    def ri(self,i):
        num_str = str(self.estado[i+1])
        num_str = '0.' + num_str
        self.r=float(num_str)
        return self.r

    def toString(self):
        print("Cuadrados Medios")
        for i in range(self.n):
            print("x",i,"=",self.x(i)," r",i,"=",self.ri(i))

class pm:
    def __init__(self,semilla,n):
        self.estado=semilla
        self.n=n

    def x(self,i):
        elevado = self.estado[i]*self.estado[i+1]
        num_str = str(elevado)
        if len(num_str) % 2 != 0:
            num_str = '0' + num_str
        medio = len(num_str) // 2
        arreglo = [int(digito) for digito in num_str[medio - 2:medio + 2]]
        self.numero_separado = int(''.join(str(digito) for digito in arreglo))
        self.estado.append(self.numero_separado)
        return self.numero_separado

    def ri(self,i):
        num_str = str(self.estado[i+1])
        num_str = '0.' + num_str
        self.r=float(num_str)
        return self.r

    def toString(self):
        print("Productos De Medios")
        for i in range(self.n):
            print("x",i,"=",self.x(i),"*",self.x(i+1)," r",i,"=",self.ri(i))

class agc:
    def __init__(self,a,b,c,m,semilla,n):
        self.estado=semilla
        self.a=a
        self.b=b
        self.c=c
        self.m=m
        self.n=n

    def x(self):
        self.xi=(self.a * self.estado**2 + self.b*self.estado + self.c)
        return self.xi

    def ximod(self):
        self.estado= (self.a * self.estado**2 + self.b*self.estado + self.c)%self.m
        return self.estado

    def ri(self):
        self.r=self.estado/(self.m-1)
        return  self.r

    def toString(self):
        print("Algoritmo Congruencial Cuadratico")
        for i in range(self.n):
            print(self.x(), " ", self.ximod(), " = {:.2f}".format(self.ri()))

class agl:
    def __init__(self,a,c,m,semilla,n):
        self.estado=semilla
        self.a=a
        self.c=c
        self.m=m
        self.n=n

    def x(self):
        self.xi=(self.a * self.estado* + self.c)
        return self.xi

    def ximod(self):
        self.estado= (self.a * self.estado + self.c)%self.m
        return self.estado

    def ri(self):
        self.r=self.estado/(self.m-1)
        return  self.r

    def toString(self):
        print("Algoritmo Congruencial Lineal")
        for i in range(self.n):
            print(self.x(), " ", self.ximod(), " = {:.2f}".format(self.ri()))

class agm:
    def __init__(self,a,m,semilla,n):
        self.estado=semilla
        self.a=a
        self.m=m
        self.n=n

    def x(self):
        self.xi=(self.a * self.estado)
        return self.xi

    def ximod(self):
        self.estado= (self.a * self.estado)%self.m
        return self.estado

    def ri(self):
        self.r=self.estado/(self.m-1)
        return  self.r

    def toString(self):
        print("Algoritmo Congruencial Multiplicativo")
        for i in range(self.n):
            print(self.x(), " ", self.ximod(), " = {:.2f}".format(self.ri()))

class aga:
    def __init__(self,datos,m,n):
        self.n=n
        self.m=m
        self.a=datos
        self.b=copy.copy(self.a)

    def xMOD(self,i):
        self.sumaMOD = ((self.a[i] + self.a[-1])%self.m)
        self.a.append(self.sumaMOD)
        self.b.append(self.sumaMOD)
        return self.sumaMOD

    def x(self,i):
        self.suma = (self.b[i] + self.b[-1])
        return self.suma

    def ri(self,i):
        self.r=self.a[i]/(self.m-1)
        return self.r

    def toString(self):
        print("Algoritmo Congruencial Aditivo")
        for i in range(self.n):
            print(self.b[i]," + ",self.a[len(self.a)-1],"=",self.x(i),"%",self.m,"=",self.xMOD(i))
            if (i>=len(self.a)/2):
                print(self.a[i],"/",self.m-1,"= {:.2f}".format(self.ri(i)))

argumentos=pm([2396,1224],10)
argumentos.toString()

argumentos=cm([3496],10)
argumentos.toString()

argumentos= aga([65,89,98,3,69],100,10)
argumentos.toString()

argumentos = agl(19,33,100,37,10)
argumentos.toString()

argumentos = agc(17, 15, 28, 36,24,10)
argumentos.toString()

argumentos = agm(21, 32, 17, 10)
argumentos.toString()

