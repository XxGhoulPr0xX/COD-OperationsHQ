class PruebaCorridaArribaAbajo:
    def __init__(self,datos):
        self.datos=datos
        self.s=[]
        self.c0=0
        self.c1=0
        self.n0=0
        self.count=1
        self.v11=[]
        self.numero=[]
        self.resultado=[]

    def corridas(self):
        for i in range(0,len(self.datos)-1):
            if 0.5 <=self.datos[i]:
                self.s.append(1)
            else:
                self.s.append(0)
        return self.s

    def ContarCerosUnos(self):
        for i in range(-1,len(self.datos)-1):
            if self.s[i] == 0:
                self.c0 = self.c0 + 1
            elif self.s[i] == 1:
                self.c1 = self.c1 + 1
        return self.c0

    def ContarCorridas(self):
        self.num = self.s[0]
        for i in range(1, len(self.s)):
            if self.s[i] == self.num:
                self.count += 1
            else:
                self.numero.append(self.num)
                self.resultado.append(self.count)
                self.num = self.s[i]
                self.count = 1
        self.n0 = len(self.resultado)
        return self.numero,self.resultado

    def Fo(self,i):
        self.cantidad=[0] * (max(self.resultado) + 1)
        for num in self.resultado:
            self.cantidad[num] += int(num/num)
        return self.cantidad[i]

    def Fe(self,i):
        self.fe=(len(self.datos)-i+3)/(2**(i+1))
        return self.fe

    def operador(self,i):
        self.v10=(self.fe-self.cantidad[i])**2/self.fe
        self.v11.append(self.v10)
        return self.v10

    def toString(self):
        print(self.datos)
        print(self.corridas(),"\n",self.ContarCorridas())
        print("Hay un total de ",self.ContarCerosUnos()," Ceros y hay un total de ",self.c1,"Unos \nTeniendo un total de ",self.n0," Corridas")
        for i in range(1,max(self.resultado)+1):
            print(i,"||{:.4f}".format(self.Fe(i)),"||",self.Fo(i),"||{:.4f}".format(self.operador(i)))
        print("\t\t\t\t\t{:.4f}".format(sum(self.v11)))

argumentos=PruebaCorridaArribaAbajo([0.15,0.26,0.33,0.25,0.16,0.31,0.34,0.49,0.83,0.11,0.81,0.70,0.77,
0.68,0.03,0.48,0.31,0.04,0.97,0.59,0.01,0.07,0.43,0.11,0.25,0.60,0.06,0.92,0.07,0.55])
argumentos.toString()