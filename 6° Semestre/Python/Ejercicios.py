import random
import itertools
import tkinter as tk
from tkinter import ttk

class OperacionesConCadenas:
    def __init__(self):
        pass

    def Ejercicio1A(self,v):
        concatenacion = []
        concatenacion.append("ε (cadena vacía)")
        for _ in range(10):
            cadena = "".join(map(str, random.choices(v, k=random.randint(1, 10))))  # Permitir cadena vacía ε
            concatenacion.append(cadena)  # Agregar ε como primer caracter
        concatenacion.sort(key=len)  # Ordena las concatenaciones por longitud
        concatenacion.remove("ε (cadena vacía)")  # Remover ε (cadena vacía)
        concatenacion.insert(0, "ε (cadena vacía)")  # Agregar ε (cadena vacía) al inicio
        return concatenacion
    
    def Ejercicio1B(self,v):
        concatenacion = []
        for _ in range(10):
            cadena = "".join(map(str, random.choices(v, k=random.randint(1, 10))))  # Permitir cadena vacía ε
            concatenacion.append(cadena)  # Agregar ε como primer caracter
        concatenacion.sort(key=len)  # Ordena las concatenaciones por longitud
        return concatenacion

    def Ejercicio2A(self,v):
        V_pow_3 = v+v+v
        return V_pow_3
    
    def Ejercicio2B(self,v):
        self.V_star = {""}  # Incluye la cadena vacía
        for i in range(1, 3):  # Supongamos hasta longitud 3
            for combo in itertools.product(v, repeat=i):
                self.V_star.add("".join(combo))
        return self.V_star
    
    def Ejercicio2C(self,v,w):
        VW = set()
        for v_str in v:
            for w_str in w:
                VW.add(v_str + w_str)
        return VW
    
    def Ejercicio3A(self,x,y):
        xR = x[::-1]
        xy = set()
        xy.add(xR + y)
        return xy
    
    #En la teoría de autómatas
    #“λ” representa la cadena 
    # vacía dentro de una 
    # palabra1. Por ejemplo, 
    # la palabra “aaλbb” sería, 
    # simplificando, la palabra 
    # "aabb"1. Es decir, “λ” no 
    # aporta ningún carácter a 
    # la cadena.
    def Ejercicio3B(self,x,y):
        xy = set()
        xy.add(y+x)
        return xy
    
    def Ejercicio3C(self,x):
        x3 = x+x
        return x3

    def Ejercicio4A(self,w):
        w_pow_3 = w+w
        return w_pow_3
    
    def Ejercicio4B(self,v):
        self.V_star = {""}  # Incluye la cadena vacía
        for i in range(1, 5):  # Supongamos hasta longitud 3
            for combo in itertools.product(v, repeat=i):
                self.V_star.add("".join(combo))
        return self.V_star
    
    def Ejercicio4C(self,v,w):
        VW = set()
        for v_str in v:
            for w_str in w:
                VW.add(v_str + w_str)
        return VW
#3.Dada las cadenas X=2000 y Y= Compiladores.
# a)x^r y(R=Reversa)
# b)y ∆(lamda) x
# c) X²
class InterfazOperaciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Operaciones con Cadenas")
        self.geometry("400x400")
        self.alpha = OperacionesConCadenas()

        self.ventana = ttk.Notebook(self)
        self.ventana.grid(row=0, column=0)
        self.ejercicio1 = ttk.Frame(self.ventana)
        self.ejercicio2 = ttk.Frame(self.ventana)
        self.ejercicio3 = ttk.Frame(self.ventana)
        self.ejercicio4 = ttk.Frame(self.ventana)
        self.ventana.add(self.ejercicio1, text="Ejercicio 1")
        self.ventana.add(self.ejercicio2, text="Ejercicio 2")
        self.ventana.add(self.ejercicio3, text="Ejercicio 3")
        self.ventana.add(self.ejercicio4, text="Ejercicio 4")

        self.Pestaña1()
        self.Pestaña2()
        self.Pestaña3()
        self.Pestaña4()

    def Pestaña1(self):
        lblEjercico1 = ttk.Label(self.ejercicio1, text="Ejercicio 1")
        lblEjercico1.grid(row=1, column=0)

        lblVocabulario = ttk.Label(self.ejercicio1, text="Vocabulario (separe los elementos por comas):")
        lblVocabulario.grid(row=2, column=1)
        self.txtVocabulario1 = ttk.Entry(self.ejercicio1)
        self.txtVocabulario1.grid(row=3, column=1)
        self.txtVocabulario1.bind("<KeyRelease>", self.verificar_contenido1)

        lblResultado = ttk.Label(self.ejercicio1, text="Resultado:")
        lblResultado.grid(row=4, column=1)
        self.txtResultado1 = tk.Text(self.ejercicio1, wrap=tk.WORD, width=40, height=5)
        self.txtResultado1.grid(row=5, column=1)
        self.txtResultado1.config(state="normal")
        self.btnEjercicio1 = ttk.Button(self.ejercicio1, text="Ejecutar Ejercicio 1", command=self.Ejercicio1)
        self.btnEjercicio1.grid(row=6, column=1)
        self.btnEjercicio1.config(state="disabled")

    def Pestaña2(self):
        lblEjercico1 = ttk.Label(self.ejercicio2, text="Ejercicio 2")
        lblEjercico1.grid(row=1, column=0)

        lblVocabulario = ttk.Label(self.ejercicio2, text="V (separe los elementos por comas):")
        lblVocabulario.grid(row=2, column=1)
        self.txtV = ttk.Entry(self.ejercicio2)
        self.txtV.grid(row=3, column=1)
        self.txtV.bind("<KeyRelease>", self.verificar_contenido2)
        lblVocabulario = ttk.Label(self.ejercicio2, text="W (separe los elementos por comas):")
        lblVocabulario.grid(row=4, column=1)
        self.txtW = ttk.Entry(self.ejercicio2)
        self.txtW.grid(row=5, column=1)
        self.txtW.bind("<KeyRelease>", self.verificar_contenido2)

        lblResultado = ttk.Label(self.ejercicio2, text="Resultado:")
        lblResultado.grid(row=6, column=1)
        self.txtResultado2 = tk.Text(self.ejercicio2, wrap=tk.WORD, width=40, height=5)
        self.txtResultado2.grid(row=7, column=1)
        self.txtResultado2.config(state="normal")
        self.btnEjercicio2 = ttk.Button(self.ejercicio2, text="Ejecutar Ejercicio 2", command=self.Ejercicio2)
        self.btnEjercicio2.grid(row=8, column=1)
        self.btnEjercicio2.config(state="disabled")

    def Pestaña3(self):
        lblEjercico1 = ttk.Label(self.ejercicio3, text="Ejercicio 3")
        lblEjercico1.grid(row=1, column=0)

        lblVocabulario = ttk.Label(self.ejercicio3, text="X (separe los elementos por comas):")
        lblVocabulario.grid(row=2, column=1)
        self.txtX = ttk.Entry(self.ejercicio3)
        self.txtX.grid(row=3, column=1)
        self.txtX.bind("<KeyRelease>", self.verificar_contenido3)
        lblVocabulario = ttk.Label(self.ejercicio3, text="Y (separe los elementos por comas):")
        lblVocabulario.grid(row=4, column=1)
        self.txtY = ttk.Entry(self.ejercicio3)
        self.txtY.grid(row=5, column=1)
        self.txtY.bind("<KeyRelease>", self.verificar_contenido3)

        lblResultado = ttk.Label(self.ejercicio3, text="Resultado:")
        lblResultado.grid(row=6, column=1)
        self.txtResultado3 = tk.Text(self.ejercicio3, wrap=tk.WORD, width=40, height=5)
        self.txtResultado3.grid(row=7, column=1)
        self.txtResultado3.config(state="normal")
        self.btnEjercicio3 = ttk.Button(self.ejercicio3, text="Ejecutar Ejercicio 3", command=self.Ejercicio3)
        self.btnEjercicio3.grid(row=8, column=1)
        self.btnEjercicio3.config(state="disabled")

    def Pestaña4(self):
        lblEjercico1 = ttk.Label(self.ejercicio4, text="Ejercicio 4")
        lblEjercico1.grid(row=1, column=0)

        lblVocabulario = ttk.Label(self.ejercicio4, text="V (separe los elementos por comas):")
        lblVocabulario.grid(row=2, column=1)
        self.txtV2 = ttk.Entry(self.ejercicio4)
        self.txtV2.grid(row=3, column=1)
        self.txtV2.bind("<KeyRelease>", self.verificar_contenido4)
        lblVocabulario = ttk.Label(self.ejercicio4, text="W (separe los elementos por comas):")
        lblVocabulario.grid(row=4, column=1)
        self.txtW2 = ttk.Entry(self.ejercicio4)
        self.txtW2.grid(row=5, column=1)
        self.txtW2.bind("<KeyRelease>", self.verificar_contenido4)

        lblResultado = ttk.Label(self.ejercicio4, text="Resultado:")
        lblResultado.grid(row=6, column=1)
        self.txtResultado4 = tk.Text(self.ejercicio4, wrap=tk.WORD, width=40, height=5)
        self.txtResultado4.grid(row=7, column=1)
        self.txtResultado4.config(state="normal")
        self.btnEjercicio4 = ttk.Button(self.ejercicio4, text="Ejecutar Ejercicio 4", command=self.Ejercicio4)
        self.btnEjercicio4.grid(row=8, column=1)
        self.btnEjercicio4.config(state="disabled")


    def verificar_contenido1(self, event):
            contenido = self.txtVocabulario1.get()
            if contenido.strip() == "":
                self.btnEjercicio1.config(state="disabled")
            else:
                self.btnEjercicio1.config(state="normal")

    def verificar_contenido2(self, event):
            if self.txtW.get().strip() == "" or self.txtV.get().strip() == "":
                self.btnEjercicio2.config(state="disabled")
            else:
                self.btnEjercicio2.config(state="normal")

    def verificar_contenido3(self, event):
            if self.txtX.get().strip() == "" or self.txtY.get().strip() == "":
                self.btnEjercicio3.config(state="disabled")
            else:
                self.btnEjercicio3.config(state="normal")

    def verificar_contenido4(self, event):
            if self.txtW2.get().strip() == "" or self.txtV2.get().strip() == "":
                self.btnEjercicio4.config(state="disabled")
            else:
                self.btnEjercicio4.config(state="normal")
                
    def Ejercicio1(self):
        v = self.txtVocabulario1.get().split(',')
        resultado1A = self.alpha.Ejercicio1A(v)
        resultado1B = self.alpha.Ejercicio1B(v)
        self.txtResultado1.delete(1.0, tk.END)
        self.txtResultado1.insert(tk.END, "v^* \n")  # Agrega una línea en blanco
        for item in resultado1A[0:5]:
            self.txtResultado1.insert(tk.END, item + "\n")
        self.txtResultado1.insert(tk.END, "\nv^+ \n")  # Agrega una línea en blanco
        for item in resultado1B[0:5]:
            self.txtResultado1.insert(tk.END, item + "\n")

    def Ejercicio2(self):
        v = self.txtV.get().split(',')
        w = self.txtW.get().split(',')
        resultado2A = self.alpha.Ejercicio2A(v)
        resultado2B = self.alpha.Ejercicio2B(w)
        resultado2C = self.alpha.Ejercicio2C(v,w)
        self.txtResultado2.delete(1.0, tk.END)
        self.txtResultado2.insert(tk.END, "v^3 \n")  # Agrega una línea en blanco
        for item in resultado2A:
            self.txtResultado2.insert(tk.END, item +"\n")
        self.txtResultado2.insert(tk.END, "\nw^*")  # Agrega una línea en blanco
        for item in resultado2B:
            self.txtResultado2.insert(tk.END, item + "\n")

        self.txtResultado2.insert(tk.END, "\nVW \n")  # Agrega una línea en blanco
        for item in resultado2C:
            self.txtResultado2.insert(tk.END, item + "\n")

    def Ejercicio3(self):
        x = self.txtX.get()
        y = self.txtY.get()
        resultado3A = self.alpha.Ejercicio3A(x,y)
        resultado3B = self.alpha.Ejercicio3B(x,y)
        resultado3C = self.alpha.Ejercicio3C(x)
        self.txtResultado3.delete(1.0, tk.END)
        self.txtResultado3.insert(tk.END, "x^ry \n")  # Agrega una línea en blanco
        for item in resultado3A:
            self.txtResultado3.insert(tk.END, item + "\n")

        self.txtResultado3.insert(tk.END, "\ny∆x\n")  # Agrega una línea en blanco
        for item in resultado3B:
            self.txtResultado3.insert(tk.END, item + "\n")

        self.txtResultado3.insert(tk.END, "\nX²\n")  # Agrega una línea en blanco
        self.txtResultado3.insert(tk.END, resultado3C + "\n")
    #4. Sean los vocabularios V={a,b} y W={0,1,2}, defina:
    #a) W²={
    #b) W*={
    #c) VW={
    def Ejercicio4(self):
        v = self.txtV2.get().split(',')
        w = self.txtW2.get().split(',')
        resultado4A = self.alpha.Ejercicio4A(w)
        resultado4B = self.alpha.Ejercicio4B(w)
        resultado4C = self.alpha.Ejercicio4C(v,w)
        self.txtResultado4.delete(1.0, tk.END)
        self.txtResultado4.insert(tk.END, "w^2 \n")  # Agrega una línea en blanco
        for item in resultado4A:
            self.txtResultado4.insert(tk.END, item + "\n")

        self.txtResultado4.insert(tk.END, "\nw^*")  # Agrega una línea en blanco
        for item in resultado4B:
            self.txtResultado4.insert(tk.END, item + "\n")

        self.txtResultado4.insert(tk.END, "\nVW \n")  # Agrega una línea en blanco
        for item in resultado4C:
            self.txtResultado4.insert(tk.END, item + "\n")


if __name__ == "__main__":
    app = InterfazOperaciones()
    app.mainloop()