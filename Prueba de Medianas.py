import math
from scipy.stats import norm

class PruebaMedia:

    def __init__(self, datos,a,h1,h0):
        self.datos = datos
        self.a=a
        self.hipotesis1=h1
        self.hipotesis0=h0

    def calcular_media(self):
        return sum(self.datos) / len(self.datos)

    def calcular_Z(self):
        media = self.calcular_media()
        acumulado = norm.cdf(media)
        posicion = norm.ppf(acumulado)
        return posicion

    def Superior(self):
        inferior=(0.5)-(((self.calcular_Z()*self.a)/2)/(math.sqrt(12*sum(self.datos))))
        return inferior

    def Inferior(self):
        superior=(0.5)+(((self.calcular_Z()*self.a)/2)/(math.sqrt(12*sum(self.datos))))
        return superior

    def toString(self):
        print(self.datos)
        print("la media de los datos es {:.2f}".format(self.calcular_media())," al mismo tiempo que Z se encuentra en "
        "{:.2f}".format(self.calcular_Z())," al mismo tiempo sabemos que el limite superior es {:.4f}".format(self.Superior()),""
        "y el inferior es {:.4f}".format(self.Inferior()))
        if((self.hipotesis1<=self.Superior())or(self.hipotesis0)>=self.Inferior()):
            print("se acepta la hipotesis")
        else:
            print("No se acepta la hipotesis")

argumentos = PruebaMedia([0.013,0.021,0.032,0.045,0.049,0.106,0.107,0.125,0.159,0.173,0.175,0.198,0.252,0.253,0.255,0.256,
0.304,0.336,0.359,0.359,0.373,0.397,0.415,0.551,0.575,0.592,0.602,0.630,0.648,0.669,0.697,0.703,0.704,0.830,0.835,0.841,
0.852,0.909,0.920,0.958],0.05,0.5,0.5)
argumentos.toString()