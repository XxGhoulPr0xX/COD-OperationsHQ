
class GeneracionCodigoIntermedio():
    def __init__(self):
        self.Numeros=[]

    def prefijo(self, expresion):
        caracteres = self.separarCaracteres(expresion)
        self.Numeros = self.eliminar(caracteres)
        prefijo=self.ordenarPre(self.Numeros)
        return prefijo
    
    def infijo(self, expresion):
        caracteres = self.separarCaracteres(expresion)
        self.Numeros = self.eliminar(caracteres)
        prefijo=self.ordenarIn(self.Numeros)
        return prefijo
        
    def postfijo(self, expresion):
        caracteres = self.separarCaracteres(expresion)
        self.Numeros = self.eliminar(caracteres)
        prefijo=self.ordernarPost(self.Numeros)
        return prefijo
    
    def ordenarPre(self, Num):
        prefijo=[]
        prefijo.insert(0,Num[5])
        prefijo.insert(1,Num[1])
        prefijo.insert(2,Num[0])
        prefijo.insert(3,Num[3])
        prefijo.insert(4,Num[2])
        prefijo.insert(5,Num[4])
        prefijo.insert(6,Num[7])
        prefijo.insert(7,Num[6])
        prefijo.insert(8,Num[9])
        prefijo.insert(9,Num[8])
        prefijo.insert(10,Num[10])
        return prefijo
    
    def ordenarIn(self, Num):
        infijo=[]
        infijo.insert(0,Num[0])
        infijo.insert(1,Num[1])
        infijo.insert(2,Num[2])
        infijo.insert(3,Num[3])
        infijo.insert(4,Num[4])
        infijo.insert(5,Num[5])
        infijo.insert(6,Num[6])
        infijo.insert(7,Num[7])
        infijo.insert(8,Num[8])
        infijo.insert(9,Num[9])
        infijo.insert(10,Num[10])
        return infijo
    
    def ordernarPost(self, Num):
        postfijo=[]
        postfijo.insert(0,Num[0])
        postfijo.insert(1,Num[1])
        postfijo.insert(2,Num[2])
        postfijo.insert(3,Num[4])
        postfijo.insert(4,Num[3])
        postfijo.insert(5,Num[6])
        postfijo.insert(6,Num[7])
        postfijo.insert(7,Num[8])
        postfijo.insert(8,Num[10])
        postfijo.insert(9,Num[9])
        postfijo.insert(10,Num[5])
        return postfijo

    def eliminar(self, caracteres):
        caracteres_filtrados = []
        for i in caracteres:
            if i not in '()[]{}':
                caracteres_filtrados.append(i)
        return caracteres_filtrados

    def separarCaracteres(self, expresion):
        caracteres = []
        i = 0
        while i < len(expresion):
            if expresion[i] == ' ':
                i += 1
            elif expresion[i] in '0123456789':
                j = i
                while j < len(expresion) and expresion[j] in '0123456789':
                    j += 1
                caracteres.append(expresion[i:j])
                i = j
            else:
                caracteres.append(expresion[i])
                i += 1

        return caracteres