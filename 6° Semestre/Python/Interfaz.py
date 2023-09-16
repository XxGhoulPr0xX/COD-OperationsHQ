import tkinter as tk
from tkinter import ttk
from Funcionalidad import Funcionalidad

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Práctica 2°")
        self.ventana.geometry("640x480")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)

        self.derecho = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.derecho.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")
        self.izquierdo = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.izquierdo.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nsw")
        self.alpha=Funcionalidad(self)

        self.nbNavegador = ttk.Notebook(self.derecho, style="TNotebook", padding=5)
        self.nbNavegador.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nsew")

        self.btnGenerar = tk.Button(self.izquierdo, text="Generar Pedido", command=self.GenerarPedido)
        self.btnGenerar.pack(side="top", pady=5)
        self.btnAbastecer = tk.Button(self.izquierdo, text="Abastecer Stock", command=self.Abastecer)
        self.btnAbastecer.pack(side="top", pady=5)

        self.nbAbastecerNuevo = False
        self.nbAbastecerActual = None
        self.nbPedidoNuevo = False
        self.nbPedidoActual = None


    def Abastecer(self):
        if self.nbAbastecerNuevo:
            self.nbNavegador.forget(self.nbAbastecerActual)
            self.nbAbastecerNuevo = False
        self.abastecer_frame = ttk.Frame(self.nbNavegador)
        self.nbNavegador.add(self.abastecer_frame, text="Abastecer Stock")
        self.lblCantidad = tk.Label(self.abastecer_frame, text="Cantidad")
        self.lblCantidad.grid(row=0, column=0, padx=0, pady=0, sticky='w')
        self.row = 1
        for producto, cantidad in self.alpha.StockProductos.items():
            lblProducto = tk.Label(self.abastecer_frame, text=producto)
            lblProducto.grid(row=self.row, column=0, padx=0, pady=0, sticky='w')
            lblStock = tk.Label(self.abastecer_frame, text=str(cantidad))
            lblStock.grid(row=self.row, column=1, padx=0, pady=0, sticky='w')
            btnAbastecer = tk.Button(self.abastecer_frame, text="Abastecer",
                                     command=lambda p=producto: self.alpha.OpenInventory(p))
            btnAbastecer.grid(row=self.row, column=2)
            self.row += 1
        self.nbAbastecerActual = self.abastecer_frame
        self.nbAbastecerNuevo = True
        self.nbNavegador.select(self.nbAbastecerActual)

    def GenerarPedido(self):
        if not self.nbPedidoNuevo:
            generar_frame = ttk.Frame(self.nbNavegador)
            self.nbNavegador.add(generar_frame, text="Generar Pedido")
            self.lblTexto = tk.Label(generar_frame, text="Elija la compañía:")
            self.lblTexto.grid(row=0, column=0, padx=100, pady=10)

            self.opcion_var = tk.StringVar()
            self.opcion_var.set(None)

            opciones = [
                "Chevrolet (EU)", "Hoge Motor Company (EN)", "Samsung (KO)", "Dina (MX)",
                "Sony (JP)", "Transportes Boaty’s (EU)", "Construcción Kolosing (CAN)"
            ]

            opciones_pares = [opciones[i:i + 2] for i in range(0, len(opciones), 2)]

            row_counter = 1

            for par in opciones_pares:
                frame_opciones = tk.Frame(generar_frame, bg="lightgray")
                frame_opciones.grid(row=row_counter, column=0, columnspan=2, padx=10, pady=5, sticky="w")
                for opcion in par:
                    btn = tk.Radiobutton(frame_opciones, text=opcion, variable=self.opcion_var, value=opcion,
                                         command=self.alpha.ShowMenu)
                    btn.pack(side=tk.LEFT)
                row_counter += 1

            self.ddMenu = ttk.Combobox(generar_frame, values=[
                "Aceite sintético", "Diesel", "Gasolina 87 octanos", "Gas licuado", "Aceite extendedor parafinico"
            ])
            self.ddMenu.grid(row=row_counter, column=0, padx=10, pady=5, columnspan=2, sticky="ew")
            self.ddMenu["state"] = "disabled"
            self.ddMenu.set("Catálogo")

            row_counter += 1
            self.lblAgregar = tk.Label(generar_frame, text="Cantidad")
            self.lblAgregar.grid(row=row_counter, column=0, padx=10, pady=5, sticky="w")

            self.validacion = generar_frame.register(self.alpha.StocKRango)
            self.txtCantidad = tk.Entry(generar_frame, validate="key", validatecommand=(self.validacion, "%P"))
            self.txtCantidad.grid(row=row_counter, column=1, padx=10, pady=5, sticky="ew")
            self.txtCantidad["state"] = tk.DISABLED
            self.txtCantidad.bind("<KeyRelease>", self.alpha.setProducto)

            row_counter += 1
            self.btnAgregar = tk.Button(generar_frame, text="Agregar", command=self.alpha.agregar)
            self.btnAgregar.grid(row=row_counter, column=0, padx=10, pady=5, columnspan=2)
            self.btnAgregar["state"] = tk.DISABLED

            row_counter += 1
            self.bandera = 0
            self.btnFacturar = tk.Button(generar_frame, text="Facturar", command=self.alpha.facturar)
            self.btnFacturar.grid(row=row_counter, column=0, padx=10, pady=5, columnspan=2)
            self.btnFacturar["state"] = tk.DISABLED

            row_counter += 1
            self.lbProductos = tk.Listbox(generar_frame)
            self.lbProductos.grid(row=row_counter, column=0, padx=10, pady=5, columnspan=2)
            self.nbPedidoActual = generar_frame
            self.nbPedidoNuevo = True
        else:
            self.nbNavegador.select(self.nbPedidoActual)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.run()
