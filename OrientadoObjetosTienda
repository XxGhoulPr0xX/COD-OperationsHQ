class tienda():
    def __init__(self):
        self.productos= {'manzanas': 10, 'naranjas': 15, 'peras': 20}
    def usuario(self):
        while True:
            auser = int(input("Producto \n1.Cotizar \n2.salir\n"))
            if auser == 1:
                self.Cotizar()
            elif auser == 2:
                print("Menú principal")
                break
            else:
                print("Dame un valor válido")
    def Cotizar(self):
        for i, producto in enumerate(self.productos):
            print(i, ":", producto, " su precio es: $", self.productos[producto])
        productoC = int(input("Selecciona el producto que quieres comprar "))
        dinero = int(input("Cuánto tienes para comprar por el producto? "))
        alcanza = dinero // self.productos[list(self.productos.keys())[productoC]]
        print(f"{list(self.productos.keys())[productoC]} x {alcanza}")
    def administrar(self):
        contraseña = int(input("Escribe la contraseña para entrar en administración "))
        if contraseña == 1:
            while True:
                admin = int(input("Producto \n1.Nuevo \n2.Modificar \n3.Salir \n"))
                if admin == 1:
                    self.AgregarProducto()
                elif admin == 2:
                    self.ModificarProducto()
                elif admin == 3:
                    print("Menú principal")
                    break
                else:
                    print("Dame un valor válido")
    def AgregarProducto(self):
        newproducto = input("Dame el nuevo producto: \n")
        newprecio = int(input("Dame el nuevo precio \n"))
        self.productos[newproducto] = newprecio
    def ModificarProducto(self):
        for i, producto in enumerate(self.productos):
            print(i, ":", producto, " su precio es: ", self.productos[producto])
        productoM = int(input("¿Qué producto deseas modificar? "))
        modproducto = input("Dame el nuevo nombre del producto ")
        modprecio = int(input("Dame el nuevo precio "))
        self.productos[modproducto] = modprecio
        del self.productos[list(self.productos.keys())[productoM]]
        print("Se modificó")
    def toString(self):
        while True:
            try:
                self.a = int(input("Inicio dame uno de los siguientes valores \n1.usuario \n2.administrador\n3.salir\n"))
                if self.a == 1:
                    self.usuario()
                elif self.a == 2:
                    self.administrar()
                elif self.a == 3:
                    print("Salir")
                    break
                else:
                    print("Selecciona otra opción")
            except ValueError:
                print("Eso no es un número")
argumentos=tienda()
argumentos.toString()
