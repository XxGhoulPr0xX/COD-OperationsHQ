from scipy.stats import kstwo

class PruebaKS:
    def __init__(self,datos,a):
        self.datos=datos
        self.fe=[]
        self.FoA=[]
        self.alpha=[]
        self.l=[]
        self.a=a
        self.n=len(datos)

    def FrecuenciaEsperada(self,i):
        for j in range (1,self.n+1):
            self.l.append(j)
        self.diviendo=self.l[i]/len(self.datos)
        self.fe.append(self.diviendo)
        return self.diviendo

    def FrecuenciaObservadaAcumulada(self,i):
        self.alpha = abs(self.datos[i] - self.fe[i])
        self.FoA.append(self.alpha)
        return self.alpha

    def Maximo(self):
        self.maximo= max(self.FoA)
        return self.maximo

    def hipotesis(self):
        self.vc = kstwo.ppf(1-self.a, len(self.datos))
        if self.maximo <= self.vc:
            self.hipotesis="Se aceptan los valores, se concluye que los números del conjunto r¡ se distribuyen uniformemente."
        else:
            self.hipotesis="Se rechaza los valores, se concluye que los números del conjunto r¡ no se distribuyen uniformemente."
        return self.hipotesis

    def toString(self):
        j=0
        k=1
        for i in range(self.n):
            print(k,"/",len(self.datos),"={:.3f}".format(self.FrecuenciaEsperada(i))," "
            "(FoA-FeA) ={:.5f}".format(self.FrecuenciaObservadaAcumulada(i)))
            j=j+1
            k=k+1
            if (j==self.n):
                print("El maximo es {:.4f}".format(self.Maximo()))
                print(self.hipotesis(),"\nValor critico = {:.4f}".format(self.vc)," Valor Maximo = {:.4f}".format(self.maximo))

argumentos=PruebaKS([0.00,0.01,0.03,0.04,0.06,0.07,0.11,0.11,0.15,0.18,0.25,0.25,0.26,0.31,0.31,0.33,0.34,0.39,0.43,0.48,
0.55,0.59,0.60,0.68,0.70,0.77,0.81,0.83,0.92,0.97],0.05)
argumentos.toString()


