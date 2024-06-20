import tkinter as tk
from tkinter import ttk
from ManejoConsultas import *

class Interfaz:
    def __init__(self):
        self.delta = Logica(self)
        self.interfazPrincipal()
        self.teclados = self.delta.consultaGeneralTeclados()
        self.saxofon = self.delta.consultaGeneralSaxofon()
        self.bajo = self.delta.consultaGeneralBajo()
        self.productos=self.delta.getModeloProductos(self.delta.consultaGeneral())

    def interfazPrincipal(self):
        self.ventana = tk.Tk()
        self.ventana.title("Examen Unidad 2")
        self.ventana.state("zoomed")  # Iniciar maximizada
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.configure(bg="black")

        self.menuDesplegable()

        self.derecho = tk.Frame(self.ventana, bd=2, relief=tk.RAISED, width=200, height=100)
        self.derecho.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.derecho.pack_propagate(0)
        self.derecho.grid_columnconfigure(0, weight=1)

        self.txtResultados = tk.Text(self.derecho, bg="white", fg="black", wrap=tk.WORD, width=15, height=40)
        self.txtResultados.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def menuDesplegable(self):
        self.mnFrame = tk.Menu(self.ventana)
        self.ventana.config(menu=self.mnFrame)
    
        self.Marcas = tk.Menu(self.mnFrame, tearoff=0)
        self.mnFrame.add_cascade(label="Explorar Por Marca", menu=self.Marcas)
        self.Marcas.add_command(label="CASIO", command=lambda: self.delta.imprimirPorMarca("CASIO"))
        self.Marcas.add_command(label="YAMAHA", command=lambda: self.delta.imprimirPorMarca("YAMAHA"))
        self.Marcas.add_command(label="FENDER", command=lambda: self.delta.imprimirPorMarca("FENDER"))
        self.Marcas.add_command(label="SILVERTONE", command=lambda: self.delta.imprimirPorMarca("SILVERTONE"))
        self.Marcas.add_command(label="AMMONN", command=lambda: self.delta.imprimirPorMarca("AMMOOMM"))

        self.MostrarPorTipo = tk.Menu(self.mnFrame, tearoff=0)
        self.mnFrame.add_cascade(label="Mostrar Por Tipo", menu=self.MostrarPorTipo)

        self.subMenuSaxofon = tk.Menu(self.MostrarPorTipo, tearoff=0)
        self.tipoSilvertone = tk.Menu(self.MostrarPorTipo, tearoff=0)
        self.tipoYamaha = tk.Menu(self.MostrarPorTipo, tearoff=0)
        self.tipoAmmonn = tk.Menu(self.MostrarPorTipo, tearoff=0)

        self.subMenuBajo = tk.Menu(self.MostrarPorTipo, tearoff=0)
        self.tipoFender = tk.Menu(self.MostrarPorTipo, tearoff=0)
        self.tipoYamahaB = tk.Menu(self.MostrarPorTipo, tearoff=0)

        self.MostrarPorTipo.add_command(label="Teclado", command=lambda: self.delta.imprimirTeclados())

        self.MostrarPorTipo.add_cascade(label="Saxofon", menu=self.subMenuSaxofon)

        self.subMenuSaxofon.add_cascade(label="SILVERTONE", menu=self.tipoSilvertone)
        self.tipoSilvertone.add_command(label="Tenor", command=lambda: self.delta.imprimirSaxofon("SILVERTONE","TENOR"))
        self.tipoSilvertone.add_command(label="Soprano", command=lambda: self.delta.imprimirSaxofon("SILVERTONE","SOPRANO"))

        self.subMenuSaxofon.add_cascade(label="YAMAHA", menu=self.tipoYamaha)
        self.tipoYamaha.add_command(label="Tenor", command=lambda: self.delta.imprimirSaxofon("YAMAHA","TENOR"))
        self.tipoYamaha.add_command(label="Soprano", command=lambda: self.delta.imprimirSaxofon("YAMAHA","SOPRANO"))

        self.subMenuSaxofon.add_cascade(label="AMMONN", menu=self.tipoAmmonn)
        self.tipoAmmonn.add_command(label="Tenor", command=lambda: self.delta.imprimirSaxofon("AMMOOMM","TENOR"))
        self.tipoAmmonn.add_command(label="Soprano", command=lambda: self.delta.imprimirSaxofon("AMMOOMM","SOPRANO"))

        self.MostrarPorTipo.add_cascade(label="Bajo electronico", menu=self.subMenuBajo)

        self.subMenuBajo.add_cascade(label="FENDER", menu=self.tipoFender)
        self.tipoFender.add_command(label="Activo", command=lambda: self.delta.imprimirBajo("FENDER","ACTIVO"))
        self.tipoFender.add_command(label="Pasivo", command=lambda: self.delta.imprimirBajo("FENDER","PASIVO"))

        self.subMenuBajo.add_cascade(label="YAMAHA", menu=self.tipoYamahaB)
        self.tipoYamahaB.add_command(label="Activo", command=lambda: self.delta.imprimirBajo("YAMAHA","ACTIVO"))
        self.tipoYamahaB.add_command(label="Pasivo", command=lambda: self.delta.imprimirBajo("YAMAHA","PASIVO"))


        self.InvervalosPrecio = tk.Menu(self.mnFrame, tearoff=0)
        self.mnFrame.add_cascade(label="Invervalos Precio", menu=self.InvervalosPrecio)
        self.InvervalosPrecio.add_command(label="4000-7000",command=lambda: self.delta.filtroPrecio("4000","7000"))
        self.InvervalosPrecio.add_command(label="7000-10000",command=lambda: self.delta.filtroPrecio("7000","10000"))
        self.InvervalosPrecio.add_command(label="10000-15000",command=lambda: self.delta.filtroPrecio("10000","15000"))
        
        self.RealizarVenta = tk.Menu(self.mnFrame, tearoff=0)
        self.mnFrame.add_cascade(label="Venta", menu=self.RealizarVenta)
        self.RealizarVenta.add_command(label="Realizar Venta", command=lambda: self.menuVenta())

    def menuVenta(self):
        self.fmVenta = tk.Toplevel(self.ventana)
        self.fmVenta.title("Realizar Venta")
        self.fmVenta.geometry("300x125")
        lblModelo = tk.Label(self.fmVenta, text="Modelo")
        lblModelo.grid(row=0, column=0, padx=10, pady=10)

        all_models = [model for models_list in self.productos.values() for model in models_list]
        self.cmbModelo = ttk.Combobox(self.fmVenta, values=all_models, state="readonly")
        self.cmbModelo.grid(row=0, column=1, padx=10, pady=5)
        self.cmbModelo.bind("<<ComboboxSelected>>", lambda event: self.delta.modeloSelccionado(event))
        
        lblCantidad = tk.Label(self.fmVenta, text="Cantidad")  
        lblCantidad.grid(row=1, column=0, padx=10, pady=10)
        
        self.cmbCantidad = ttk.Combobox(self.fmVenta, values=["1", "2", "3", "4", "5","6"], state="readonly")
        self.cmbCantidad.grid(row=1, column=1, padx=10, pady=5)
        self.cmbCantidad.current(0)

        self.btnVender = tk.Button(self.fmVenta, text="Vender", state="disabled", command=self.finalizarVenta)
        self.btnVender.grid(row=2, column=1, padx=10, pady=10)

    def finalizarVenta(self):
        fmFVenta = tk.Toplevel(self.fmVenta)

        lblModelo = tk.Label(fmFVenta, text="La venta se realizó")
        lblModelo.grid(row=0, column=0, padx=10, pady=10)

        btnListo= tk.Button(fmFVenta, text="Listo", command=self.delta.fG)
        btnListo.grid(row=1, column=0, padx=10, pady=10)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.run()
