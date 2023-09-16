import tkinter as tk
import random
import string

class Funcionalidad:
    def __init__(self, interfaz):
        self.selected_product = None
        self.alpha = interfaz

        self.bandera=0
        self.StockProductos = {
            "Aceite sintético": 2500,
            "Diesel": 2820,
            "Gasolina 87 octanos": 3500,
            "Gas licuado": 4000,
            "Aceite extendedor parafinico": 5000
        }
        self.carrito=[]

    def restar_stock(self, producto, cantidad):
        if producto in self.StockProductos:
            StockAnterior = self.StockProductos[producto]
            nuevo = StockAnterior - cantidad
            self.StockProductos[producto] = nuevo

    def agregar(self):
        producto = self.alpha.ddMenu.get()
        cantidad = self.alpha.txtCantidad.get()
        if producto and cantidad:
            for i, (item, item_cantidad) in enumerate(self.alpha.carrito):
                if item == producto:
                    nueva_cantidad = int(item_cantidad) + int(cantidad)
                    self.alpha.carrito[i] = (item, nueva_cantidad)
                    self.restar_stock(producto, int(cantidad))
                    break
            else:
                self.alpha.carrito.append((producto, cantidad))
                self.restar_stock(producto, int(cantidad))
            self.alpha.txtCantidad.delete(0, tk.END)
            self.alpha.txtCantidad["state"] = tk.DISABLED
            self.alpha.btnAgregar["state"] = tk.DISABLED
            self.alpha.ddMenu.set("Catálogo")
            self.ProductosBajos()
            self.UpdateList()
            self.alpha.btnFacturar["state"] = tk.NORMAL
            self.UpdateDDMenu()

    def ProductosBajos(self):
        productos_bajos_stock = [nombre for nombre, stock in self.StockProductos.items() if stock <= 1000]
        if productos_bajos_stock:
            self.alpha.btnAbastecer.configure(bg="red")
        else:
            self.alpha.btnAbastecer.configure(bg=self.alpha.ventana.cget("bg"))

    def UpdateDDMenu(self):
        selected_product = self.alpha.ddMenu.get()
        stock_actual = self.StockProductos.get(selected_product, 0)
        available_products = [product for product, stock in self.StockProductos.items() if stock > 0]
        if selected_product == "Catálogo" or stock_actual <= 0:
            selected_product = "Catálogo"
            self.alpha.txtCantidad.delete(0, tk.END)
            self.alpha.txtCantidad["state"] = tk.DISABLED
            self.alpha.btnAgregar["state"] = tk.DISABLED
        else:
            self.alpha.txtCantidad["state"] = tk.NORMAL
            self.alpha.producto_seleccionado = selected_product
        self.alpha.ddMenu["values"] = available_products
        self.alpha.ddMenu.set(selected_product)

    def UpdateProducts(self):
        self.productos = list(self.StockProductos.items())


    def ShowMenu(self):
        self.alpha.ddMenu["state"] = "readonly"
        self.alpha.ddMenu.set("Catálogo")
        self.alpha.ddMenu.bind("<<ComboboxSelected>>", self.setProducto)
        self.alpha.carrito = []
        if self.alpha.ddMenu.get() == "Catálogo":
            if self.alpha.bandera == 0:
                self.StockProductos = {
                    "Aceite sintético": 2500,
                    "Diesel": 2820,
                    "Gasolina 87 octanos": 3500,
                    "Gas licuado": 4000,
                    "Aceite extendedor parafinico": 5000
                }
                self.alpha.btnAbastecer.configure(bg=self.alpha.ventana.cget("bg"))
                self.alpha.txtCantidad.delete(0, tk.END)
                self.alpha.lbProductos.delete(0, tk.END)
                self.alpha.txtCantidad["state"] = tk.DISABLED
                self.alpha.btnAgregar["state"] = tk.DISABLED
                self.alpha.btnFacturar["state"] = tk.DISABLED
                self.UpdateDDMenu()
            else:
                self.alpha.txtCantidad.delete(0, tk.END)
                self.alpha.lbProductos.delete(0, tk.END)
                self.alpha.txtCantidad["state"] = tk.DISABLED
                self.alpha.btnAgregar["state"] = tk.DISABLED
                self.alpha.btnFacturar["state"] = tk.DISABLED


    def setProducto(self, event):
        if self.alpha.ddMenu.get() != "Catálogo":
            self.alpha.txtCantidad["state"] = tk.NORMAL
            if self.alpha.txtCantidad.get():
                self.alpha.btnAgregar["state"] = tk.NORMAL
            else:
                self.alpha.btnAgregar["state"] = tk.DISABLED
            self.StocKRango(self.alpha.txtCantidad.get())
        else:
            self.alpha.txtCantidad.delete(0, tk.END)
            self.alpha.txtCantidad["state"] = tk.DISABLED
            self.alpha.btnAgregar["state"] = tk.DISABLED

    def StocKRango(self, entrada):
        producto = self.alpha.ddMenu.get()
        cantidad_actual = self.StockProductos.get(producto, 0)
        print(cantidad_actual)
        if entrada == "":
            return True
        if entrada.isdigit():
            if cantidad_actual > 0:
                if 1 <= int(entrada) <= cantidad_actual:
                    return True
        return False

    def UpdateList(self):
        self.alpha.lbProductos.delete(0, tk.END)
        for producto, cantidad in self.alpha.carrito:
            self.alpha.lbProductos.insert(tk.END, f"{producto} x{cantidad}")

    def facturar(self):
        self.alpha.bandera = 1
        self.alpha.ddMenu.set("Catálogo")
        self.alpha.lbProductos.delete(0, tk.END)
        self.alpha.txtCantidad["state"] = tk.DISABLED
        self.alpha.btnAgregar["state"] = tk.DISABLED
        self.alpha.btnFacturar["state"] = tk.DISABLED
        ventana_factura = tk.Toplevel(self.alpha.ventana)
        ventana_factura.title("Factura")
        box = tk.Frame(ventana_factura, bd=2, relief=tk.RAISED)
        box.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky="nsew")
        empresa_compra = self.alpha.opcion_var.get()
        cadena_aleatoria = ''.join(random.choices(string.digits, k=10)) + ''.join(random.choices(string.ascii_letters, k=10))
        rfc_aleatorio = ''.join(random.choices(string.ascii_uppercase, k=4)) + ''.join(random.choices(string.digits, k=6))
        factura_texto = f"Empresa: {empresa_compra}\n\nPedido:\n"
        for producto, cantidad in self.alpha.carrito:
            factura_texto += f"{producto} x{cantidad}\n"
        total_orden = sum(int(cantidad) for _, cantidad in self.alpha.carrito)
        factura_texto += f"\nTotal de la Orden: {total_orden}\n\nCadena Aleatoria: {cadena_aleatoria}"
        factura_texto += f"\nRFC: {rfc_aleatorio}"
        lbl_factura = tk.Label(box, text=factura_texto, anchor="w")  # Justificar a la izquierda
        lbl_factura.pack()
        self.alpha.carrito = []


    def OpenInventory(self, producto):
        self.selected_product = producto
        inventory = tk.Toplevel(self.alpha.ventana)
        inventory.title(f"Inventario - {producto}")  # Muestra el nombre del producto en la ventana
        inventory.geometry("210x64")
        box = tk.Frame(inventory, bd=2, relief=tk.RAISED)
        box.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nsew")
        lblAumento = tk.Label(box, text="Cantidad")
        lblAumento.grid(row=0, column=0, padx=0, pady=0, sticky='w')
        validate_numeric = inventory.register(self.RulesTxt)
        self.txtAgregar = tk.Entry(box, validate="key", validatecommand=(validate_numeric, "%P"))
        self.txtAgregar.grid(row=0, column=1, padx=5, pady=0, sticky='w')
        btnGuardar = tk.Button(box, text="ok", command=self.UpdateInventory)
        btnGuardar.grid(row=1, column=1, columnspan=2, padx=0, pady=5, sticky='w')

    def UpdateInventory(self):
        if self.selected_product is not None:
            cantidad_nueva = int(self.txtAgregar.get())
            if self.selected_product in self.StockProductos:
                self.StockProductos[self.selected_product] += cantidad_nueva
            else:
                self.StockProductos[self.selected_product] = cantidad_nueva
            self.UpdateLabels()

    def UpdateLabels(self):
        self.row = 1
        for producto, cantidad in self.StockProductos.items():
            cantidad_var = tk.StringVar()
            cantidad_var.set(str(cantidad))
            lblCantidad = tk.Label(self.alpha.abastecer_frame, textvariable=cantidad_var)
            lblCantidad.grid(row=self.row, column=1, padx=0, pady=0, sticky='w')
            self.row += 1
        self.ProductosBajos()
        self.UpdateDDMenu()

    def RulesTxt(self, input_text):
        if input_text == "":
            return True
        if input_text.isdigit():
            cantidad_nueva = int(input_text)
            return cantidad_nueva > 0
        return False