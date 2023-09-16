import tkinter as tk
from tkinter import ttk
from TiendaFuncionalidad import TiendaFuncionalidad


class TiendaInterfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Práctica 3°")
        self.ventana.geometry("680x550")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.alpha = TiendaFuncionalidad(self)

        self.derecho = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.derecho.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")
        self.Login()

    def Login(self):
        lblUsuario = tk.Label(self.derecho, text="Usuario")
        lblUsuario.grid(row=0, column=0, padx=200, pady=15, sticky='w')
        self.txtUsuario = tk.Entry(self.derecho)
        self.txtUsuario.grid(row=1, column=0, padx=200, pady=15, sticky="w")
        lblContraseña = tk.Label(self.derecho, text="Contraseña")
        lblContraseña.grid(row=2, column=0, padx=200, pady=15, sticky="w")
        self.txtContraseña = tk.Entry(self.derecho, show="*")
        self.txtContraseña.grid(row=3, column=0, padx=200, pady=15, sticky="w")
        self.btnIniciarSesion = tk.Button(self.derecho, text="Iniciar Sesión", command=self.alpha.Login)
        self.btnIniciarSesion.grid(row=4, column=0, padx=200, pady=15, sticky="w")
        self.btnCambiar = tk.Button(self.derecho, text="Cambiar Contraseña", command=self.alpha.ChangePassword)
        self.btnCambiar.grid(row=5, column=0, padx=200, pady=15, sticky="w")
        self.btnMostrar = tk.Button(self.derecho, text="Mostrar Contraseña", command=self.alpha.ShowPassword)
        self.btnMostrar.grid(row=6, column=0, padx=200, pady=15, sticky="w")

    def Tienda(self):
        lblPreparaPedido = tk.Label(self.derecho, text="Prepara tu pedido!!")
        lblPreparaPedido.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.lblProductos = tk.Label(self.derecho, text="Productos")
        self.lblProductos.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.ddMenu = ttk.Combobox(self.derecho,
                                   values=[
                                       "Galletas", "Panques", "Paletas", "Donas", "Vizcocho"
                                   ])
        self.ddMenu.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.ddMenu["state"] = "readonly"
        lblPrecio = tk.Label(self.derecho, text="Precio")
        lblPrecio.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        lblChocolate = tk.Label(self.derecho, text="¿Cubierta con chocolate?")
        lblChocolate.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.opcion_var = tk.StringVar()
        self.opcion_var.set("No")
        opciones = [
            "Si", "No"
        ]
        row_counter = 5
        for opcion in opciones:
            btnSiNo = tk.Radiobutton(self.derecho, text=opcion, variable=self.opcion_var, value=opcion, command=self.alpha.ActualizarChocolate)
            btnSiNo.grid(row=row_counter, column=0, padx=10, pady=10, sticky="w")
            row_counter += 1
        self.lblTotal = tk.Label(self.derecho, text="Total")
        self.lblTotal.grid(row=7, column=1, padx=10, pady=10, sticky="w")
        self.btnAgregar = tk.Button(self.derecho, text="Agregar", command=self.alpha.UpdateCarrito)
        self.btnAgregar.grid(row=8, column=1, padx=10, pady=10, sticky="w")
        self.btnFinalizar = tk.Button(self.derecho, text="Finalizar",command=self.alpha.Facturar)
        self.btnFinalizar.grid(row=8, column=2, padx=10, pady=10, sticky="w")
        self.lbCarrito = tk.Listbox(self.derecho, height=10)
        self.lbCarrito.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def Facturar(self):
        factura_window = tk.Toplevel(self.ventana)
        factura_window.title("Factura de Compra")
        factura_window.geometry("200x250")
        factura_frame = tk.Frame(factura_window, bg="pink", bd=2, relief="solid")
        factura_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lblGracias = tk.Label(factura_frame, text="Gracias por tu compra")
        lblGracias.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lblTotalDeLaCompra = tk.Label(factura_frame, text="Total de tu compra:")
        lblTotalDeLaCompra.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        total = sum(precio for _, precio in self.alpha.carrito)
        lblTotal = tk.Label(factura_frame, text=f"${total}")
        lblTotal.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lblCompraste = tk.Label(factura_frame, text="Compraste:")
        lblCompraste.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        productos_comprados_text = "\n".join([f"{producto}" for producto,precio in self.alpha.carrito])
        lblProductos = tk.Label(factura_frame, text=productos_comprados_text)
        lblProductos.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.alpha.conChocolate = False


    def run(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = TiendaInterfaz()
    app.run()