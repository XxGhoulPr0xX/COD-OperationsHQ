import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from datetime import datetime


class FuncionalidadKikin:
    def __init__(self, interfaz):
        self.alpha = interfaz
        self.Productos = {}
        self.carrito = []
        self.cargarProductosDesdeBD()  # Cargamos los productos desde la base de datos
        self.registro_pedidos = {}
        self.bandera = False
        self.sesionActual= ''

    def cargarProductosDesdeBD(self):
        try:
            server = 'localhost'
            database = 'MidulceK1K1N'  # Nombre de la base de datos
            username = 'sa'
            password = '123456789'
            port = '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            query = "SELECT Nombre, Precio FROM Producto"
            cursor.execute(query)
            for row in cursor.fetchall():
                nombre = row.Nombre
                precio = row.Precio
                self.Productos[nombre] = precio
            conn.close()
        except Exception as e:
            print("Error al cargar productos desde la base de datos:", str(e))

    def Registro(self):
        idCliente = random.randint(1, 1000)
        idDomicilio = random.randint(1, 1000)
        nombre = self.alpha.txtNombre.get()
        apellido = self.alpha.txtApellido.get()
        correo = self.alpha.txtEmail.get().lower()
        contraseña = self.alpha.txtContraseña.get()
        calle = self.alpha.txtCalle.get()
        ciudad = self.alpha.txtCiudad.get()
        estado = self.alpha.txtEstado.get()
        cp = self.alpha.txtCP.get()
        try:
            server = 'localhost'
            database = 'MidulceK1K1N'
            username = 'sa'
            password = '123456789'
            port = '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            insert_domicilio = "INSERT INTO Domicilio_Cliente (ID_Domicilio_Cliente, Calle, Ciudad, Estado, Código_Postal) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(insert_domicilio, (idDomicilio, calle, ciudad, estado, cp))
            insert_cliente = "INSERT INTO Cliente (ID_Cliente, Nombre, Apellido, Email, Contraseña, ID_Domicilio_Cliente) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_cliente, (idCliente, nombre, apellido, correo, contraseña, idDomicilio))
            conn.commit()
            conn.close()
            self.alpha.tlRegistro.destroy()
        except Exception as e:
            print("Error al registrar cliente:", str(e))

    def Login(self):
        usuario = self.alpha.txtUsuario.get()
        contraseña = self.alpha.txtContraseñaLogin.get()
        user=self.getUser(usuario)
        password=self.getPassword(usuario)
        self.sesionActual=user
        self.nbNavegador = ttk.Notebook(self.alpha.ventana, style="TNotebook", padding=5)
        self.nbNavegador.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky="nsew")
        if usuario == 'sa' and contraseña == '123456789':
            self.alpha.derecho.grid_remove()
            self.alpha.Administrador()
        elif usuario == 'Gerente' and contraseña == 'Gerente':
            self.alpha.derecho.grid_remove()
            self.alpha.Gerente()
        elif usuario == 'Empleado' and contraseña == 'Empleado':
            self.alpha.derecho.grid_remove()
            self.alpha.Empleado()
        elif usuario==user and contraseña==password:
            self.alpha.derecho.grid_remove()
            self.alpha.Cliente()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def getUser(self,email):
        server = 'localhost'
        database = 'MidulceK1K1N'
        username = 'sa'
        password = '123456789'
        port = '1433'
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            query = "SELECT Email FROM Cliente WHERE Email = ?"
            cursor.execute(query, email)
            self.correo = cursor.fetchone()
            if self.correo:
                return self.correo[0]
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error al obtener la contraseña:", str(e))
            return None
        finally:
            conn.close()

    def getPassword(self,email):
        server = 'localhost'
        database = 'MidulceK1K1N'
        username = 'sa'
        password = '123456789'
        port = '1433'
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            query = "SELECT Contraseña FROM Cliente WHERE Email = ?"
            cursor.execute(query, email)
            self.contrasena = cursor.fetchone()
            if self.contrasena:
                return self.contrasena[0]
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error al obtener la contraseña:", str(e))
            return None
        finally:
            conn.close()

    def Facturar(self):
        id_pedido = len(self.registro_pedidos) + random.randint(1, 1000)
        self.registro_pedidos[id_pedido] = {"productos": self.carrito, "id_cliente": self.sesionActual}
        self.alpha.Facturar()
        self.carrito = []
        self.ShowCarrito()
        self.alpha.ddPedidos.destroy()
        nombres_pedido = list(self.registro_pedidos.keys())
        self.alpha.ddPedidos = ttk.Combobox(self.alpha.frSurtir, values=nombres_pedido)
        self.alpha.ddPedidos.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.alpha.ddPedidos["state"] = "readonly"
        self.alpha.ddPedidos.set('')  # Establece el valor inicial
        self.alpha.ddPedidos.bind("<<ComboboxSelected>>", lambda event: self.getAdress())

    def UpdateCarrito(self):
        producto_seleccionado = self.alpha.ddMenu.get()
        if producto_seleccionado:
            precio_producto = self.Productos.get(producto_seleccionado)
            self.carrito.append((producto_seleccionado, precio_producto))
            self.ShowCarrito()
            self.alpha.ddMenu.set("")

    def ShowCarrito(self):
        self.alpha.lbCarrito.delete(0, tk.END)  # Borra todo el contenido anterior
        total = 0
        for producto, precio in self.carrito:
            self.alpha.lbCarrito.insert(tk.END, f"{producto}: ${precio}")
            total += precio
        lblTotalCarrito = tk.Label(self.alpha.frTienda, text=f"Total: ${total}")
        lblTotalCarrito.grid(row=7, column=2, padx=10, pady=10, sticky="w")

    def Checar(self):
        if all([self.alpha.txtNombre.get(), self.alpha.txtApellido.get(), self.alpha.txtEmail.get(), self.alpha.txtContraseña.get(),self.alpha.txtCiudad.get(),self.alpha.txtCalle.get(),self.alpha.txtEstado.get(),self.alpha.txtCP.get()]):
            self.alpha.btnContinuar["state"] = "normal"
        else:
            self.alpha.btnContinuar["state"] = "disabled"

    def ShowPassword(self):
        self.bandera = not self.bandera
        if self.bandera:
            self.alpha.txtContraseñaLogin.config(show="")
        else:
            self.alpha.txtContraseñaLogin.config(show="*")

    def getAdress(self):
        direccion_pedido = self.getDireccionCliente()
        self.alpha.lblDireccionPedido.config(text=direccion_pedido)

    def getDireccionCliente(self):
        try:
            server = 'localhost'
            database = 'MidulceK1K1N'
            username = 'sa'
            password = '123456789'
            port = '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Realiza la consulta SQL para obtener la dirección del cliente actual
            query = "SELECT D.Calle, D.Ciudad, D.Estado, D.Código_Postal " \
                    "FROM Domicilio_Cliente D " \
                    "JOIN Cliente C ON D.ID_Domicilio_Cliente = C.ID_Domicilio_Cliente " \
                    "WHERE C.Email = ?"
            cursor.execute(query, self.sesionActual)
            direccion_cliente = cursor.fetchone()

            # Formatea la dirección como un string
            if direccion_cliente:
                direccion_formatada = f"{direccion_cliente[0]}, {direccion_cliente[1]}, {direccion_cliente[2]} {direccion_cliente[3]}"
                return direccion_formatada
            else:
                return "Dirección no encontrada"

        except Exception as e:
            messagebox.showerror("Error al obtener la dirección del cliente:", str(e))
            return "Error al obtener la dirección"

        finally:
            conn.close()

    def getTiendasDesdeBD(self):
        try:
            server = 'localhost'
            database = 'MidulceK1K1N'
            username = 'sa'
            password = '123456789'
            port = '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Realiza la consulta SQL para obtener las tiendas con sus IDs
            query = "SELECT ID_Tienda, Nombre FROM Tienda"
            cursor.execute(query)
            tiendas = [{"id": row.ID_Tienda, "nombre": row.Nombre} for row in cursor.fetchall()]

            return tiendas

        except Exception as e:
            messagebox.showerror("Error al obtener las tiendas:", str(e))
            return []

        finally:
            conn.close()


    def PedidoDB(self):
        try:
            self.id_pedido = random.randint(1, 1000)
            self.fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.tienda_seleccionada = 1
            self.id_producto = self.registro_pedidos[0]["productos"][0][0]
            server = 'localhost'
            database = 'MidulceK1K1N'
            username = 'sa'
            password = '123456789'
            port = '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            query = "SELECT ID_Cliente FROM Cliente WHERE Email = ?"
            cursor.execute(query, self.sesionActual)
            self.id_cliente = cursor.fetchone()
            if self.id_cliente:
                return self.id_cliente[0]
            
            print(self.id_pedido,self.id_cliente,self.tienda_seleccionada,self.fecha_pedido)
            insert_pedido = "INSERT INTO Pedido (ID_Pedido, Fecha_Pedido, ID_Tienda, ID_Cliente, ID_Producto) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(insert_pedido, (self.id_pedido, self.fecha_pedido, self.tienda_seleccionada, self.id_cliente, self.id_producto))

            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error al facturar el pedido:", str(e))
