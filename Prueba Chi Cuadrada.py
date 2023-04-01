import math
from scipy.stats import chi2


class ChiCuadrada:
    def __init__(self,datos,m):
        self.datos=datos
        self.m=m
        self.e=0
        self.intervalo=[0]
        self.oi=[]
        self.x=[]

    def CalcularN(self):
        self.n=math.sqrt(self.m)
        return int(self.n)

    def CalcularE(self):
        self.e=self.n/self.m
        return self.e

    def CalcularIntevarlo(self,i):
        self.rango=0
        if i==0:
            self.intervalo.append(0)
        else:
            self.rango=self.intervalo[i]+self.e
            self.intervalo.append(self.rango)
        return self.rango

    def NumerosDentroDelIntervalo(self,i):
        cantidad = 0
        for numero in self.datos:
            if self.intervalo[i] <= numero <= self.intervalo[i+1]:
                cantidad += 1
        self.oi.append(cantidad)
        return cantidad

    def XCuadrada(self,i):
        self.xi=0
        if i==0:
            self.x.append(0)
        else:
            self.xi=(self.oi[i]-self.n)**2/self.n
            self.x.append(self.xi)
        return self.xi

    def hipotesis(self):
        chi_cuadrado=sum(self.x)
        grados_libertad = len(self.datos) - 1
        valor_critico = chi2.ppf(0.95, df=grados_libertad)
        if chi_cuadrado > valor_critico:
            self.h="verdadera"
        else:
            self.h="falsa"
        return self.h

    def toString(self):
        print("N\tE\tIntervalo\tOi")
        for i in range(0,int(self.CalcularN())+1):
            print(self.CalcularN(),"|",self.CalcularE(),"| {:.2f}".format(self.CalcularIntevarlo(i)),"|",self.NumerosDentroDelIntervalo(i),"|",self.XCuadrada(i))
        print("total",sum(self.x),"\nLa hipotesis es",self.hipotesis())

argumentos=ChiCuadrada([0.011,0.022,0.054,0.055,0.056,0.057,0.067,0.101,0.112,0.123,0.178,0.178,0.189,0.189,0.190,0.191,
0.224,0.235,0.246,0.252,0.280,0.303,0.303,0.303,0.314,0.347,0.347,0.347,0.370,0.371,0.393,0.393,0.404,0.404,0.415,0.426,
0.437,0.444,0.459,0.460,0.461,0.472,0.472,0.494,0.494,0.516,0.527,0.549,0.562,0.562,0.562,0.584,0.603,0.628,0.640,0.641,
0.641,0.646,0.652,0.663,0.674,0.674,0.707,0.729,0.730,0.731,0.742,0.742,0.742,0.742,0.753,0.764,0.775,0.786,0.786,0.797,
0.797,0.797,0.797,0.819,0.819,0.821,0.821,0.832,0.843,0.876,0.881,0.898,0.909,0.933,0.944,0.945,0.966,0.966,0.977,0.977,
0.990,0.992,0.993,0.999],100)
argumentos.toString()