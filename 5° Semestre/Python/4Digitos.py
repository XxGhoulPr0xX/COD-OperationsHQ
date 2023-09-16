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
            print(i+1,"(",self.estado[i],")^2 = ",self.estado[i]**2,"=",self.x(i),"Ri = ",self.ri(i))

argumentos=cm([3487],10)
argumentos.toString()