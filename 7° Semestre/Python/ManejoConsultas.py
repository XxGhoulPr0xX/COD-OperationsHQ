import os
import tkinter as tk
from tkinter import ttk
from ConexionCassandra import *

class Logica():
    def __init__(self,interfaz):
        self.beta=ConexionCassandra()
        self.foxtrot=interfaz
        self.teclados = []
        self.saxofon=[]
        self.bajo=[]

    def consultaGeneralTeclados(self):
        consulta = "select * from teclados" 
        resultado = self.beta.session.execute(consulta)
        for fila in resultado:
            fila_diccionario = dict(fila._asdict())
            self.teclados.append(fila_diccionario)
        return self.teclados

    def separarPorMarca(self, instrumentos, marca_filtrar=None):
        instrumentos_por_marca = {}
        for instrumento in instrumentos:
            marca = instrumento.get('marca')  
            if marca_filtrar is None or marca == marca_filtrar:
                if marca not in instrumentos_por_marca:
                    instrumentos_por_marca[marca] = []
                instrumentos_por_marca[marca].append(instrumento)
        return instrumentos_por_marca

    def consultaGeneralSaxofon(self):
        consulta = "select * from saxofon"  
        resultado = self.beta.session.execute(consulta)
        for fila in resultado:
            fila_diccionario = dict(fila._asdict())
            self.saxofon.append(fila_diccionario)
        return self.saxofon

    def consultaGeneralBajo(self):
        consulta = "select * from bajoelectronico"  
        resultado = self.beta.session.execute(consulta)
        for fila in resultado:
            fila_diccionario = dict(fila._asdict())
            self.bajo.append(fila_diccionario)
        return self.bajo

    def separarPorTipo(self, instrumentos, tipoF=None):
        instrumentos_por_tipo = {}
        for instrumento in instrumentos:
            tipo = instrumento.get('tipo')  
            if tipoF is None or tipo == tipoF:
                if tipo not in instrumentos_por_tipo:
                    instrumentos_por_tipo[tipo] = []
                instrumentos_por_tipo[tipo].append(instrumento)
        return instrumentos_por_tipo
    
    def getModeloProductos(self, instrumento):
        ids = {}
        for tipo, productos in instrumento.items():
            ids[tipo] = [producto['modelo'] for producto in productos]
        return ids

    def consultaGeneral(self):
        instrumentos = {}
        instrumentos['teclados'] = self.consultaGeneralTeclados()
        instrumentos['saxofon'] = self.consultaGeneralSaxofon()
        instrumentos['bajo'] = self.consultaGeneralBajo()
        return instrumentos
    
    def imprimirPorMarca(self, marca):
        self.foxtrot.txtResultados.delete('1.0', tk.END)
        tipos_instrumentos = {
            'teclados': self.teclados,
            'saxofon': self.saxofon,
            'bajo': self.bajo
        }
        encabezados = {
            'teclados': 'Teclados\nmodelo - precio\n',
            'saxofon': 'Saxofon\nmodelo - tipo - precio\n',
            'bajo': 'Bajo electrico\nmodelo - tipo - cuerdas -precio\n'
        }
        for tipo, instrumentos in tipos_instrumentos.items():
            filtrado = self.separarPorMarca(instrumentos, marca)
            if filtrado:
                self.foxtrot.txtResultados.insert(tk.END, encabezados[tipo])
                for marca_instrumentos in filtrado.values():
                    for instrumento in marca_instrumentos:
                        tipo_instrumento = instrumento.get('tipo') if tipo != 'teclados' else ''
                        cuerdas_instrumento = instrumento.get('cuerdas') if tipo == 'bajo' else ''
                        self.foxtrot.txtResultados.insert(tk.END, f"{instrumento['modelo']} - {tipo_instrumento} - {cuerdas_instrumento} - ${instrumento['precio']}\n")

    def imprimirTeclados(self):
        self.foxtrot.txtResultados.delete('1.0', tk.END)
        self.foxtrot.txtResultados.insert(tk.END, "Teclados\nmodelo - precio\n")
        for d in self.teclados:
            self.foxtrot.txtResultados.insert(tk.END, f"{d['modelo']} - ${d['precio']}\n")

    def imprimirSaxofon(self, marca, tipo):
        self.foxtrot.txtResultados.delete('1.0', tk.END)
        self.foxtrot.txtResultados.insert(tk.END, f"Saxofones {marca}\nmodelo - tipo - precio\n")
        filtradoM = self.separarPorMarca(self.saxofon, marca)
        filtradoM = [val for sublist in filtradoM.values() for val in sublist]
        filtradoT = self.separarPorTipo(filtradoM,tipo)
        for tipo_instrumentos in filtradoT.values():
            for instrumento in tipo_instrumentos:
                self.foxtrot.txtResultados.insert(tk.END, f"{instrumento['modelo']} - {instrumento.get('tipo')} - ${instrumento['precio']}\n")

    def imprimirBajo(self, marca, tipo):
        self.foxtrot.txtResultados.delete('1.0', tk.END)
        self.foxtrot.txtResultados.insert(tk.END, f"Bajos {marca}\nmodelo - tipo - cuerdas - precio\n")
        filtradoM = self.separarPorMarca(self.bajo, marca)
        filtradoM = [val for sublist in filtradoM.values() for val in sublist]
        filtradoT = self.separarPorTipo(filtradoM,tipo)
        for tipo_instrumentos in filtradoT.values():
            for instrumento in tipo_instrumentos:
                self.foxtrot.txtResultados.insert(tk.END, f"{instrumento['modelo']} - {instrumento.get('tipo')} - {instrumento.get('cuerdas')}- ${instrumento['precio']}\n")

    def filtroPrecio(self, p1, p2):
        self.foxtrot.txtResultados.delete('1.0', tk.END)
        self.foxtrot.txtResultados.insert(tk.END,"-------------[Teclados]----------\nmodelo - precio\n")
        for d in self.teclados:
            if int(p1)<= d['precio'] <= int(p2):
                self.foxtrot.txtResultados.insert(tk.END, f"{d['modelo']} - {d['marca']} -${d['precio']}\n")

        self.foxtrot.txtResultados.insert(tk.END,"-------------[Saxofon]----------\nmodelo - tipo - precio\n")
        for f in self.saxofon:
            if int(p1)<= f['precio'] <= int(p2):
                self.foxtrot.txtResultados.insert(tk.END, f"{f['modelo']} - {f.get('tipo')}-{f['marca']} -${f['precio']}\n")

        self.foxtrot.txtResultados.insert(tk.END,"-------------[Bajo electrico]----------\nmodelo - tipo - cuerdas - precio\n")
        for g in self.bajo:
                if int(p1)<= g['precio'] <= int(p2):
                    self.foxtrot.txtResultados.insert(tk.END, f"{g['modelo']} - {g.get('tipo')}- {g.get('cuerdas')}-{g['marca']} -${g['precio']}\n")

    def modeloSelccionado(self,event):
        if self.foxtrot.cmbModelo.get() and self.foxtrot.cmbCantidad.get():
            self.foxtrot.btnVender.config(state="normal")
        else:
            self.foxtrot.btnVender.config(state="disabled")
    
    def bD(self, modelo,cantidad):
        self.foxtrot.fmVenta.destroy()
        instrumentos = self.consultaGeneral()
        datosInstrumento = []
        for tipo, productos in instrumentos.items():
            for producto in productos:
                if producto['modelo'] == modelo:
                    instrumento = tipo.capitalize()
                    marca = producto.get('marca', 'Desconocida')
                    tipo = producto.get('tipo', 'None')
                    precio = producto.get('precio', 'Desconocido')
                    total=precio*cantidad
                    datosInstrumento.append(instrumento)
                    datosInstrumento.append(marca)
                    datosInstrumento.append(tipo)
                    datosInstrumento.append(precio)
                    datosInstrumento.append(cantidad)
                    datosInstrumento.append(total)
                    return datosInstrumento
                
    def gT(self,arreglo):
        txt1 = "Instrumento: " + arreglo[0]
        txt2 = "Marca: " + arreglo[1]
        txt3 = "Tipo: " + arreglo[2]
        txt4 = "Precio: " + str(arreglo[3]) 
        txt5 = "Cantidad: " + str(arreglo[4]) 
        txt6 = "Total: " + str(arreglo[5])
        return txt1, txt2, txt3, txt4, txt5, txt6
    
    def gA(self, texto):
        ruta = "C:/Users/XxGho/Documents/Escuela/7° Semestre/Programación General/Python/Recibos"
        nombre_archivo = "recibo.txt"
        ruta_archivo = os.path.join(ruta, nombre_archivo)
        with open(ruta_archivo, "w") as archivo:
            for linea in texto:
                archivo.write(linea + "\n")

    def fG(self):
        busqueda=self.bD(self.foxtrot.cmbModelo.get(),int(self.foxtrot.cmbCantidad.get()))
        refactorizarT=self.gT(busqueda)
        generarArchivo=self.gA(refactorizarT)