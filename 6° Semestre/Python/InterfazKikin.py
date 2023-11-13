import tkinter as tk
from tkinter import ttk
from FuncionalidadKikin import *

class TiendaInterfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dulceria Kikin")
        self.ventana.geometry("640x480")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.derecho = tk.Frame(self.ventana)
        self.derecho.grid(row=0, column=0, sticky="nsew")
        self.alpha=FuncionalidadKikin(self)
        self.Login()

    def Login(self):
        lblUsuario = tk.Label(self.derecho, text="Usuario (Correo Electronico)")
        lblUsuario.grid(row=0, column=0, padx=200, pady=0, sticky='w')
        self.txtUsuario = tk.Entry(self.derecho)
        self.txtUsuario.grid(row=2, column=0, padx=200, pady=0, sticky="w")
        lblContraseña = tk.Label(self.derecho, text="Contraseña")
        lblContraseña.grid(row=3, column=0, padx=200, pady=0, sticky="w")
        self.txtContraseñaLogin = tk.Entry(self.derecho, show="*")
        self.txtContraseñaLogin.grid(row=4, column=0, padx=200, pady=0, sticky="w")
        self.btnIniciarSesion = tk.Button(self.derecho, text="Iniciar Sesión", command=self.alpha.Login)
        self.btnIniciarSesion.grid(row=5, column=0, padx=200, pady=0, sticky="w")
        self.btnMostrar = tk.Button(self.derecho, text="Mostrar Contraseña", command=self.alpha.ShowPassword)
        self.btnMostrar.grid(row=6, column=0, padx=200, pady=0, sticky="w")
        self.btnRegistrarse = tk.Button(self.derecho, text="Registrarse", command=self.Registro)
        self.btnRegistrarse.grid(row=7, column=0, padx=200, pady=0, sticky="w")
    
    def Registro(self):
        self.tlRegistro = tk.Toplevel(self.ventana)
        self.tlRegistro.title("Factura de Compra")
        self.tlRegistro.geometry("320x240")
        lblNombre = tk.Label(self.tlRegistro,text="Nombre")
        lblNombre.grid(row=0,column=0,sticky="w")
        self.txtNombre= tk.Entry(self.tlRegistro)
        self.txtNombre.grid(row=0,column=1,sticky="w")
        self.txtNombre.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblApellido = tk.Label(self.tlRegistro,text="Apellido")
        lblApellido.grid(row=1,column=0,sticky="w")
        self.txtApellido= tk.Entry(self.tlRegistro)
        self.txtApellido.grid(row=1,column=1,sticky="w")
        self.txtApellido.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblEmail = tk.Label(self.tlRegistro,text="Correo Electronico")
        lblEmail.grid(row=2,column=0,sticky="w")
        self.txtEmail= tk.Entry(self.tlRegistro)
        self.txtEmail.grid(row=2,column=1,sticky="w")
        self.txtEmail.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblContraseña = tk.Label(self.tlRegistro,text="Contraseña")
        lblContraseña.grid(row=3,column=0,sticky="w")
        self.txtContraseña= tk.Entry(self.tlRegistro, show="*")
        self.txtContraseña.grid(row=3,column=1,sticky="w")
        self.txtContraseña.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblMensaje = tk.Label(self.tlRegistro, text="Calle")
        lblMensaje.grid(row=4,column=0,sticky="w")
        self.txtCalle=tk.Entry(self.tlRegistro)
        self.txtCalle.grid(row=4,column=1,sticky="w")
        self.txtCalle.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblCiudad = tk.Label(self.tlRegistro, text="Ciudad")
        lblCiudad.grid(row=5,column=0,sticky="w")
        self.txtCiudad=tk.Entry(self.tlRegistro)
        self.txtCiudad.grid(row=5,column=1,sticky="w")
        self.txtCiudad.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblEstado = tk.Label(self.tlRegistro, text="Estado")
        lblEstado.grid(row=6,column=0,sticky="w")
        self.txtEstado=tk.Entry(self.tlRegistro)
        self.txtEstado.grid(row=6,column=1,sticky="w")
        self.txtEstado.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        lblCP = tk.Label(self.tlRegistro, text="Codigo Postal")
        lblCP.grid(row=7,column=0,sticky="w")
        self.txtCP=tk.Entry(self.tlRegistro)
        self.txtCP.grid(row=7,column=1,sticky="w")
        self.txtCP.bind("<KeyRelease>", lambda event: self.alpha.Checar())
        self.btnContinuar= tk.Button(self.tlRegistro, text="Continuar", command=self.alpha.Registro)
        self.btnContinuar.grid(row=8, column=0, sticky="w")
        self.btnContinuar["state"]="disabled"

    def Administrador(self):
        self.Tienda()
        self.surtirPedido()
        self.abastecerStock()
        
    def Gerente(self):
        self.surtirPedido()
        self.abastecerStock()

    def Cliente(self):
        self.Tienda()

    def Empleado(self):
        self.surtirPedido()

    def Tienda(self):
        self.frTienda = ttk.Frame(self.alpha.nbNavegador)
        self.alpha.nbNavegador.add(self.frTienda, text="Tienda")
        lblPreparaPedido = tk.Label(self.frTienda, text="Prepara tu pedido!!")
        lblPreparaPedido.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.lblProductos = tk.Label(self.frTienda, text="Productos")
        self.lblProductos.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        nombres_productos = list(self.alpha.Productos.keys())
        self.ddMenu = ttk.Combobox(self.frTienda, values=nombres_productos)
        self.ddMenu.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.ddMenu["state"] = "readonly"
        lblPrecio = tk.Label(self.frTienda, text="Precio")
        lblPrecio.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.lblTotal = tk.Label(self.frTienda, text="Total")
        self.lblTotal.grid(row=7, column=1, padx=10, pady=10, sticky="w")
        self.btnAgregar = tk.Button(self.frTienda, text="Agregar", command=self.alpha.UpdateCarrito)
        self.btnAgregar.grid(row=8, column=1, padx=10, pady=10, sticky="w")
        self.btnFinalizar = tk.Button(self.frTienda, text="Finalizar",command=self.alpha.Facturar)
        self.btnFinalizar.grid(row=8, column=2, padx=10, pady=10, sticky="w")
        self.lbCarrito = tk.Listbox(self.frTienda, height=10)
        self.lbCarrito.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def surtirPedido(self):
        self.frSurtir = ttk.Frame(self.alpha.nbNavegador)
        self.alpha.nbNavegador.add(self.frSurtir, text="Pedido")
        lblIdPedido = tk.Label(self.frSurtir, text="Selecciona el Id del pedido:")
        lblIdPedido.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        nombres_pedido = list(self.alpha.registro_pedidos.keys())
        self.ddPedidos = ttk.Combobox(self.frSurtir, values=nombres_pedido)
        self.ddPedidos.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.ddPedidos["state"] = "readonly"
        lblDireccionUsuario = tk.Label(self.frSurtir, text="Dirección de entrega:")
        lblDireccionUsuario.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.lblDireccionPedido = tk.Label(self.frSurtir, text="")
        self.lblDireccionPedido.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        btnPedido = tk.Button(self.frSurtir, text="Surtir Pedido", command=self.alpha.PedidoDB)
        btnPedido.grid(row=9, column=1, padx=10, pady=5, sticky="ew")
        tiendas = self.alpha.getTiendasDesdeBD()
        self.radio_var = tk.StringVar(value=tiendas[0])  # Valor predeterminado
        row = 4
        column = 0
        for tienda in tiendas:
            tk.Radiobutton(self.frSurtir, text=tienda, variable=self.radio_var, value=tienda).grid(row=row, column=column, padx=10, pady=5, sticky="w")
            column += 1
            if column > 1:
                column = 0
                row += 1

    def abastecerStock(self):
        self.frAbastecer = ttk.Frame(self.alpha.nbNavegador)
        self.alpha.nbNavegador.add(self.frAbastecer, text="Abastecer Stock")
        lblProducto = tk.Label(self.frAbastecer, text="Producto:")
        lblProducto.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.txtProductoAbastecer = tk.Entry(self.frAbastecer)
        self.txtProductoAbastecer.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        lblCantidad = tk.Label(self.frAbastecer, text="Cantidad:")
        lblCantidad.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.txtCantidadAbastecer = tk.Entry(self.frAbastecer)
        self.txtCantidadAbastecer.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        btnAbastecer = tk.Button(self.frAbastecer, text="Abastecer Stock")
        btnAbastecer.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    def Facturar(self):
        factura_window = tk.Toplevel(self.ventana)
        factura_window.title("Pedido")
        factura_window.geometry("200x250")
        factura_frame = tk.Frame(factura_window, bg="pink", bd=2, relief="solid")
        factura_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        factura_frame.grid_columnconfigure(0, weight=1)
        factura_frame.grid_columnconfigure(1, weight=1)  # Si tienes dos columnas
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

    def Pedido(self):
        tlPedido = tk.Toplevel(self.ventana)
        tlPedido.title("Factura de Compra")
        tlPedido.geometry("200x250")
        lblGracias = tk.Label(tlPedido, text="Gracias por tu compra")
        lblGracias.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lblTotalDeLaCompra = tk.Label(tlPedido, text="Total de tu compra:")
        lblTotalDeLaCompra.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        total = sum(precio for _, precio in self.alpha.carrito)
        lblTotal = tk.Label(tlPedido, text=f"${total}")
        lblTotal.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lblCompraste = tk.Label(tlPedido, text="Compraste:")
        lblCompraste.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        productos_comprados_text = "\n".join([f"{producto}" for producto,precio in self.alpha.carrito])
        lblProductos = tk.Label(tlPedido, text=productos_comprados_text)
        lblProductos.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def run(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = TiendaInterfaz()
    app.run()