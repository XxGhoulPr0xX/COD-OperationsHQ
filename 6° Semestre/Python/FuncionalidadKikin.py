import random
import re
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
        self.carritoProductos= []
        self.cargarProductosDesdeBD()  # Cargamos los productos desde la base de datos
        self.registro_pedidos = {}
        self.bandera = False
        self.sesionActual= ''
        self.fecha_actual = datetime.now()

    def conexionDesdeBD(self):
        try:
            server='localhost'
            database='MidulceK1K1N'
            username= 'sa'
            password= '123456789'
            port= '1433'
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Error al cargar desde la base de datos:", str(e))

    def cargarPedidosDesdeDB(self):
        self.conexionDesdeBD()
        try:
            query= "Select IdPedido,CorreoCliente from RegistroPedido"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                IdPedido= row.IdPedido
                CorreoCliente = row.CorreoCliente
                self.registro_pedidos[IdPedido] = CorreoCliente
        except Exception as e:
            print("Error al cargar productos desde la base de datos:", str(e))

    def cargarProductosDesdeBD(self):
        try:
            self.conexionDesdeBD()
            query = "SELECT Nombre, Precio FROM Producto"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                nombre = row.Nombre
                precio = row.Precio
                self.Productos[nombre] = precio
            self.conn.close()
        except Exception as e:
            print("Error al cargar productos desde la base de datos:", str(e))

    def recargarDDPedidos(self):
        nombres_pedido = list(self.registro_pedidos.keys())
        self.ddPedidos = ttk.Combobox(self.alpha.frSurtir, values=nombres_pedido)
        self.ddPedidos.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.ddPedidos["state"] = "readonly"

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
            self.conexionDesdeBD()
            insert_domicilio = "INSERT INTO Domicilio_Cliente (ID_Domicilio_Cliente, Calle, Ciudad, Estado, Código_Postal) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(insert_domicilio, (idDomicilio, calle, ciudad, estado, cp))
            insert_cliente = "INSERT INTO Cliente (ID_Cliente, Nombre, Apellido, Email, Contraseña, ID_Domicilio_Cliente) VALUES (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(insert_cliente, (idCliente, nombre, apellido, correo, contraseña, idDomicilio))
            self.conn.commit()
            self.conn.close()
            self.alpha.tlRegistro.destroy()
        except Exception as e:
            print("Error al registrar cliente:", str(e))

    def Login(self):
        usuario = self.alpha.txtUsuario.get()
        contraseña = self.alpha.txtContraseñaLogin.get()
        user = self.getUser(usuario)
        password = self.getPassword(usuario)
        self.sesionActual = user
        if usuario == 'sa@gmail.com' and contraseña == 'sa':
            self.cargarPedidosDesdeDB()
            self.alpha.derecho.grid_remove()
            self.nbNavegador = ttk.Notebook(self.alpha.ventana, style="TNotebook", padding=5)
            self.nbNavegador.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.alpha.Administrador()
        elif usuario == 'Gerente' and contraseña == 'Gerente':
            self.cargarPedidosDesdeDB()
            self.alpha.derecho.grid_remove()
            self.nbNavegador = ttk.Notebook(self.alpha.ventana, style="TNotebook", padding=5)
            self.nbNavegador.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.alpha.Gerente()
        elif usuario == 'Empleado' and contraseña == 'Empleado':
            self.cargarPedidosDesdeDB()
            self.alpha.derecho.grid_remove()
            self.nbNavegador = ttk.Notebook(self.alpha.ventana, style="TNotebook", padding=5)
            self.nbNavegador.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.alpha.Empleado()
        elif usuario == user and contraseña == password:
            self.alpha.derecho.grid_remove()
            self.nbNavegador = ttk.Notebook(self.alpha.ventana, style="TNotebook", padding=5)
            self.nbNavegador.grid(row=0, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.alpha.Cliente()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def getUser(self,email):
        self.conexionDesdeBD()
        try:
            query = "SELECT Email FROM Cliente WHERE Email = ?"
            self.cursor.execute(query, email)
            self.correo = self.cursor.fetchone()
            if self.correo:
                return self.correo[0]
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error al obtener la contraseña:", str(e))
            return None
        finally:
            self.conn.close()

    def getPassword(self,email):
        self.conexionDesdeBD()
        try:
            query = "SELECT Contraseña FROM Cliente WHERE Email = ?"
            self.cursor.execute(query, email)
            self.contrasena = self.cursor.fetchone()
            if self.contrasena:
                return self.contrasena[0]
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error al obtener la contraseña:", str(e))
            return None
        finally:
            self.conn.close()

    def Facturar(self):
        self.alpha.btnFinalizar["state"] = "disabled"
        id_pedido = len(self.registro_pedidos) + random.randint(1, 1000)
        IdCarrito = random.randint(1,100)+20
        self.setCarrito(IdCarrito)
        self.RegistroPedido(id_pedido,self.sesionActual,IdCarrito)
        self.guardarDatos()
        i=0
        while(i<len(self.Idproducto)):
            self.setDetallesCarrito(IdCarrito,self.Idproducto[i],self.Ptotal[i])
            i+=1
        self.alpha.Facturar()
        self.carrito = []
        self.ShowCarrito()
        self.cargarPedidosDesdeDB()

    def getCorreo(self,IdRegistro):
        self.conexionDesdeBD()
        try:
            query="Select CorreoCliente from RegistroPedido where IdPedido= ?"
            self.cursor.execute(query,IdRegistro)
            resultado = self.cursor.fetchone()
            if resultado:
                Correo = resultado[0]
                return Correo
        except Exception as e:
            messagebox.showerror("Error al llenar el carrito de compras del pedido del cliente:", str(e))

    def guardarDatos(self):
        productos_pedido = self.carritoProductos
        self.Idproducto=[]
        self.Ptotal=[]
        recuentoProductos=self.contarProductos(self.getIdProductos(productos_pedido))
        for producto,total in recuentoProductos:
            self.Idproducto.append(producto)
            self.Ptotal.append(total)

    def setDetallesCarrito(self,IdCarrito,IdProducto,Cantidad):
        self.conexionDesdeBD()
        IdDetalles=random.randint(1,1000)+31
        try:
            queryDetalleCarrito='insert into DetallesCarrito values(?,?,?,?)'
            self.cursor.execute(queryDetalleCarrito,IdDetalles,IdCarrito,IdProducto,Cantidad)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            messagebox.showerror("Error al llenar el carrito de compras del pedido del cliente:", str(e))

    def setCarrito(self,IdCarrito):
        self.conexionDesdeBD()
        try:
            queryCarrito='insert into CarritoCompras values(?)'
            self.cursor.execute(queryCarrito,IdCarrito)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            messagebox.showerror("Error al llenar el carrito de compras del pedido del cliente:", str(e))

    def RegistroPedido(self,IdPedido,ClienteActual,IdCarrito):
        self.conexionDesdeBD()
        try:
            query='insert into RegistroPedido values(?,?,?)'
            self.cursor.execute(query, IdPedido,ClienteActual,IdCarrito)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            messagebox.showerror("Error al registrar el pedido del cliente:", str(e))

    def UpdateCarrito(self):
        producto_seleccionado = self.alpha.ddMenu.get()
        if producto_seleccionado:
            precio_producto = self.Productos.get(producto_seleccionado)
            self.carrito.append((producto_seleccionado, precio_producto))
            self.carritoProductos.append(producto_seleccionado)
            self.ShowCarrito()
            self.alpha.ddMenu.set("")
            self.ActualizarEstadoBoton()

    def ActualizarEstadoBoton(self):
        if self.alpha.lbCarrito.get(0, "end"):
            self.alpha.btnFinalizar["state"] = "normal"

    def ShowCarrito(self):
        self.alpha.lbCarrito.delete(0, tk.END)  # Borra todo el contenido anterior
        total = 0
        for producto, precio in self.carrito:
            self.alpha.lbCarrito.insert(tk.END, f"{producto}: ${precio}")
            total += precio
        if hasattr(self.alpha, 'lblTotalCarrito'):
            self.alpha.lblTotalCarrito.destroy()
        self.alpha.lblTotalCarrito = tk.Label(self.alpha.frTienda, text=f"Total: ${total}")
        self.alpha.lblTotalCarrito.grid(row=7, column=2, padx=10, pady=10, sticky="w")

    def Checar(self):
        nombre = self.alpha.txtNombre.get()
        apellido = self.alpha.txtApellido.get()
        email = self.alpha.txtEmail.get()
        contraseña = self.alpha.txtContraseña.get()
        ciudad = self.alpha.txtCiudad.get()
        calle = self.alpha.txtCalle.get()
        estado = self.alpha.txtEstado.get()
        cp = self.alpha.txtCP.get()

        if all([
            nombre and len(nombre) <= 50,
            apellido and len(apellido) <= 50,
            email and re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(email) <= 100,
            contraseña and len(contraseña) <= 10,
            ciudad and len(ciudad) <= 30,
            calle and len(calle) <= 50,
            estado and len(estado) <= 100,
            cp and len(cp) <= 5
        ]):
            self.alpha.btnContinuar["state"] = "normal"
            return
        self.alpha.btnContinuar["state"] = "disabled"


    def ShowPassword(self):
        self.bandera = not self.bandera
        if self.bandera:
            self.alpha.txtContraseñaLogin.config(show="")
        else:
            self.alpha.txtContraseñaLogin.config(show="*")

    def getAdress(self,Correo):
        direccion_pedido = self.getDireccionCliente(Correo)
        self.alpha.lblDireccionPedido.destroy()
        self.alpha.lblDireccionPedido = tk.Label(self.alpha.frSurtir, text="")
        self.alpha.lblDireccionPedido.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.alpha.lblDireccionPedido.config(text=direccion_pedido)

    def getDireccionCliente(self,Correo):
        self.conexionDesdeBD()
        try:
            query = "SELECT D.Calle, D.Ciudad, D.Estado, D.Código_Postal " \
                    "FROM Domicilio_Cliente D " \
                    "JOIN Cliente C ON D.ID_Domicilio_Cliente = C.ID_Domicilio_Cliente " \
                    "WHERE C.Email = ?"
            self.cursor.execute(query, Correo)
            direccion_cliente = self.cursor.fetchone()
            if direccion_cliente:
                direccion_formatada = f"{direccion_cliente[0]}, {direccion_cliente[1]}, {direccion_cliente[2]} {direccion_cliente[3]}"
                return direccion_formatada
            else:
                return "Dirección no encontrada"
        except Exception as e:
            messagebox.showerror("Error al obtener la dirección del cliente:", str(e))
            return "Error al obtener la dirección"
        finally:
            self.conn.close()

    def getTiendasDesdeBD(self):
        self.conexionDesdeBD()
        try:
            query = "SELECT Nombre FROM Tienda"
            self.cursor.execute(query)
            nombres_tiendas = [row.Nombre for row in self.cursor.fetchall()]
            return nombres_tiendas
        except Exception as e:
            messagebox.showerror("Error al obtener los nombres de las tiendas:", str(e))
            return []
        finally:
            self.conn.close()

    def PedidoDB(self):
        self.conexionDesdeBD()
        IdRegistroPedido=self.alpha.ddPedidos.get()
        Correo=self.getCorreo(IdRegistroPedido)
        IdPedido=self.alpha.ddPedidos.get()
        try:
            self.correo_cliente =self.ObtenerIdMedianteCorreo(Correo)
            self.nombre_tienda = self.getIdTienda(self.alpha.radio_var.get())
            self.fecha_formateada = self.fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
            self.recuento_productos =self.ObtenerProductoCantidad(IdPedido)
            self.listaIdproductos = []
            self.totalIdproductos = []
            for producto, total in self.recuento_productos:
                self.listaIdproductos.append(producto)
                self.totalIdproductos.append(total)
            self.DivideAndExecute()
        except Exception as e:
            messagebox.showerror("Error en la transacción", str(e))
            print("Error en la transacción", str(e))

    def DivideAndExecute(self):
        i=0
        while i<len(self.listaIdproductos):
            self.idPedido= len(self.registro_pedidos)+ random.randint(1,1000)
            self.ejecutarProcedimiento(self.idPedido,self.fecha_formateada,self.nombre_tienda,self.correo_cliente,self.listaIdproductos[i],self.totalIdproductos[i])
            i=i+1

    def getIdTienda(self,nombre_tienda):
            self.conexionDesdeBD()
            try:
                query_tienda = "SELECT ID_Tienda FROM Tienda WHERE Nombre = ?"
                self.cursor.execute(query_tienda, (nombre_tienda,))
                resultado_tienda = self.cursor.fetchone()
                id_tienda= resultado_tienda[0]
                return id_tienda
            except Exception as e:
                messagebox.showerror("Error en la transacción", str(e))

    def getIdCliente(self,correo_cliente):
        self.conexionDesdeBD()
        try:
            query_cliente = "SELECT ID_Cliente FROM Cliente WHERE Email = ?"
            self.cursor.execute(query_cliente, (correo_cliente,))
            resultado_cliente = self.cursor.fetchone()
            id_cliente= resultado_cliente[0]
            return id_cliente
        except Exception as e:
            messagebox.showerror("Error en la transacción", str(e))

    def contarProductos(self, productos):
        recuento = {}
        for producto in productos:
            if producto in recuento:
                recuento[producto] += 1
            else:
                recuento[producto] = 1
        total = list(recuento.items())
        return total

    def getIdProductos(self, lista_productos):
        self.conexionDesdeBD()
        ids_productos = []
        try:
            query = "SELECT ID_Producto FROM Producto WHERE Nombre = ?"
            for producto in lista_productos:
                self.cursor.execute(query, (producto,))
                resultado = self.cursor.fetchone()
                if resultado:
                    id_producto = resultado[0]
                    ids_productos.append(id_producto)
                else:
                    print(f"No se encontró ID para el producto: {producto}")
            return ids_productos
        except Exception as e:
            print(f"Error al obtener IDs de productos: {str(e)}")
            return None
        
    def ejecutarProcedimiento(self, idPedido,fecha, id_tienda, id_cliente, id_producto, cantidad):
        self.conexionDesdeBD()
        try:
            query_procedimiento = "EXEC RealizarPedido ? ,?, ?, ?, ?, ?"  # Ajusta según tu implementación
            self.cursor.execute(query_procedimiento, (idPedido,fecha, id_tienda, id_cliente, id_producto, cantidad))
            self.conn.commit()
            textoA="El producto llegará en ",random.randint(1,100)," Minutos"
            messagebox.showinfo("El producto será surtido por la tienda",textoA)
        except Exception as e:
            messagebox.showerror("Error al ejecutar el procedimiento almacenado", str(e))
            print("Error al ejecutar el procedimiento almacenado", str(e))
        finally:
            IdPedidoR=self.alpha.ddPedidos.get()
            self.EliminarDeBD(IdPedidoR)
            indice_seleccionado = self.alpha.ddPedidos.current()
            if indice_seleccionado is not None:
                self.alpha.ddPedidos['values'] = (
                    self.alpha.ddPedidos['values'][:indice_seleccionado] +
                    self.alpha.ddPedidos['values'][indice_seleccionado+1:]
                )
            self.alpha.ddPedidos.set('')
            self.alpha.lblDireccionPedido.destroy()
            self.alpha.lblDireccionPedido = tk.Label(self.alpha.frSurtir, text="")
            self.alpha.lblDireccionPedido.grid(row=2, column=1, padx=10, pady=5, sticky="w")
            self.conn.close()

    def updateStock(self):
        idProducto=self.alpha.txtProductoAbastecer.get()
        cantidadProducto=self.alpha.txtCantidadAbastecer.get()
        try:
            self.conexionDesdeBD()
            query_stock="UPDATE Producto set Stock = Stock + ? Where ID_Producto = ?"
            self.cursor.execute(query_stock,(cantidadProducto,idProducto))
            self.conn.commit()
            print("Update listo")
        except Exception as e:
            messagebox.showerror("Error al ejecutar el procedimiento almacenado", str(e))
        finally:
            self.alpha.txtProductoAbastecer.delete(0, tk.END)
            self.alpha.txtCantidadAbastecer.delete(0, tk.END)
            self.alpha.lblProductoA.destroy()
            self.alpha.lblProductoA = tk.Label(self.alpha.frAbastecer, text="")
            self.alpha.lblProductoA.grid(row=0, column=2, padx=10, pady=5, sticky="w")

    def ActualizarProducto(self):
        idProducto=self.alpha.txtProductoAbastecer.get()
        productoActual=self.getNombreProducto(idProducto)
        self.alpha.lblProductoA.destroy()
        self.alpha.lblProductoA = tk.Label(self.alpha.frAbastecer, text="")
        self.alpha.lblProductoA.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.alpha.lblProductoA.config(text=productoActual)
    
    def getNombreProducto(self, ID_Producto):
        self.conexionDesdeBD()
        try:
            query="SELECT nombre from Producto where ID_Producto= ?"
            self.cursor.execute(query,(ID_Producto))
            resultado = self.cursor.fetchone()
            if resultado:
                NombreProducto = resultado[0]
                return NombreProducto
            else:
                return f"No se encontró ID para el producto: {ID_Producto}"
        except Exception as e:
            messagebox.showerror("Error al ejecutar el procedimiento almacenado", str(e))

    def DireccionActual(self):
        IdRegistroPedido=self.alpha.ddPedidos.get()
        Correo=self.getCorreo(IdRegistroPedido)
        self.getAdress(Correo)
    
    def ObtenerIdMedianteCorreo(self,Correo):
        self.conexionDesdeBD()
        try:
            query="Select ID_Cliente from Cliente where Email= ?"
            self.cursor.execute(query,Correo)
            resultado = self.cursor.fetchone()
            if resultado:
                IdCliente = resultado[0]
                return IdCliente
        except Exception as e:
            messagebox.showerror("Error al buscar el Id del cliente", str(e))

    def ObtenerProductoCantidad(self, IdPedido):
        self.conexionDesdeBD()
        try:
            query = 'SELECT D.ID_Producto, D.Cantidad FROM RegistroPedido R INNER JOIN DetallesCarrito D ON R.IdCarrito = D.CarritoID WHERE R.IdPedido = ?'
            self.cursor.execute(query, IdPedido)
            resultados = self.cursor.fetchall()
            if resultados:
                return resultados
            else:
                return []  # Devuelve una lista vacía si no hay resultados
        except Exception as e:
            messagebox.showerror("Error al buscar el Id del cliente", str(e))

    def EliminarDeBD(self,IdPedido):
        self.conexionDesdeBD()
        try:
            query="Delete from RegistroPedido where IdPedido=?"
            self.cursor.execute(query,IdPedido)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error al buscar el Id del cliente", str(e))

    def LimpiarCarrito(self):
        self.alpha.lbCarrito.delete(0, tk.END)
        self.carrito = []
        self.alpha.btnFinalizar["state"] = "disabled"
        self.alpha.lblTotalCarrito.destroy()

    def CerrarSesion(self):
        self.nbNavegador.destroy()
        self.alpha.derecho.grid()
        self.alpha.Login()
