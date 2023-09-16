import tkinter as tk


class TiendaFuncionalidad:
    def __init__(self, xd):
        self.alpha = xd
        self.Productos = {
            "Galletas": 25,
            "Panques": 18,
            "Paletas": 12,
            "Donas": 17,
            "Vizcocho": 21
        }
        self.carrito = []
        self.contraseña = "1234"
        self.bandera = False
        self.botón_presionado = False
        self.conChocolate = False  # Variable para rastrear si se seleccionó "Si" en el radiobutton


    def Login(self):
        if self.alpha.txtUsuario.get() == "isoft" and self.alpha.txtContraseña.get() == self.contraseña:
            for widget in self.alpha.derecho.winfo_children():
                widget.destroy()
            self.alpha.Tienda()
        else:
            self.lblQP = tk.Label(self.alpha.derecho, text="Usuario o Contraseña Incorrectos")
            self.lblQP.grid(row=8, column=0, padx=200, pady=0, sticky="w")

    def ChangePassword(self):
        self.ventana_cambio = tk.Toplevel()
        self.ventana_cambio.title("Cambiar Contraseña")
        lblContraseñaAnterior = tk.Label(self.ventana_cambio, text="Contraseña Anterior:")
        lblContraseñaAnterior.grid(row=1, column=0, padx=200, pady=20, sticky="w")
        self.txtContraseñaAnterior = tk.Entry(self.ventana_cambio, show="*")
        self.txtContraseñaAnterior.grid(row=2, column=0, padx=200, pady=20, sticky="w")
        lblNuevaContraseña = tk.Label(self.ventana_cambio, text="Nueva Contraseña:")
        lblNuevaContraseña.grid(row=3, column=0, padx=200, pady=20, sticky="w")
        self.txtNuevaContraseña = tk.Entry(self.ventana_cambio, show="*")
        self.txtNuevaContraseña.grid(row=4, column=0, padx=200, pady=20, sticky="w")
        self.btnGuardar = tk.Button(self.ventana_cambio, text="Guardar Cambio", command=self.UpdatePassword)
        self.btnGuardar.grid(row=5, column=0, padx=200, pady=20, sticky="w")
        btnMostrar = tk.Button(self.ventana_cambio, text="Mostrar Contraseña", command=self.ShowPassword1)
        btnMostrar.grid(row=6, column=0, padx=200, pady=20, sticky="w")

    def UpdatePassword(self):
        if self.contraseña == self.txtContraseñaAnterior.get():
            self.contraseña = self.txtNuevaContraseña.get()
            self.ventana_cambio.destroy()
        else:
            self.lblQP = tk.Label(self.ventana_cambio, text="Contraseña Anterior Incorrecta")
            self.lblQP.grid(row=5, column=0, padx=200, pady=20, sticky="w")

    def ShowPassword(self):
        self.bandera = not self.bandera
        if self.bandera:
            self.alpha.txtContraseña.config(show="")
        else:
            self.alpha.txtContraseña.config(show="*")

    def ShowPassword1(self):
        self.botón_presionado = not self.botón_presionado
        if self.botón_presionado:
            self.txtContraseñaAnterior.config(show="")
            self.txtNuevaContraseña.config(show="")
        else:
            self.txtContraseñaAnterior.config(show="*")
            self.txtNuevaContraseña.config(show="*")

    def UpdateCarrito(self):
        producto_seleccionado = self.alpha.ddMenu.get()
        if producto_seleccionado:
            precio_producto = self.Productos.get(producto_seleccionado)
            if precio_producto is not None:
                if self.conChocolate:  # Si se seleccionó "Si" en el radiobutton, sumar 4 al precio
                    precio_producto += 4
                    self.alpha.opcion_var.set("No")  # Establece la opción en "No" después de agregar con chocolate
                self.carrito.append((producto_seleccionado, precio_producto))
                self.ShowCarrito()
                self.alpha.ddMenu.set("")

    def ShowCarrito(self):
        self.alpha.lbCarrito.delete(0, tk.END)  # Borra todo el contenido anterior
        total = 0
        for producto, precio in self.carrito:
            self.alpha.lbCarrito.insert(tk.END, f"{producto}: ${precio}")
            total += precio
        lblTotalCarrito = tk.Label(self.alpha.derecho, text=f"Total: ${total}")
        lblTotalCarrito.grid(row=7, column=2, padx=10, pady=10, sticky="w")

    def ActualizarChocolate(self):
        if self.alpha.opcion_var.get() == "Si":
            self.conChocolate = True
        else:
            self.conChocolate = False
    
    def Facturar(self):
        self.alpha.Facturar()
        self.carrito=[]
        self.ShowCarrito()