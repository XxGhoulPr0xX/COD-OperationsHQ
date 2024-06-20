class Ejercicio6:
    def __init__(self):
        self.personal = []
        self.sucursales = []
        self.productos = []

    def get_personal_data(self):
        return self.personal

    def get_sucursales_data(self):
        return self.sucursales

    def get_productos_data(self):
        return self.productos

    def insert_data(self, arreglo, new_data):
        arreglo.append(new_data)
        return arreglo
    
    def read_data(self, arreglo):
        return arreglo
    
    def delete_data(self, arreglo):
        arreglo.clear()

    def insert_personal(self):
        datos = input("Ingrese los datos del personal separados por comas: [Id, ApellidoP, ApellidoM, Nombre, Direccion, Telefono]\n")
        new_data = datos.split(",")
        self.personal = self.insert_data(self.personal, new_data)

    def insert_sucursales(self):
        datos = input("Ingrese los datos del sucursal separados por comas: [Id, Direccion, Telefono, NomGerente]\n")
        new_data = datos.split(",")
        self.sucursales = self.insert_data(self.sucursales, new_data)

    def insert_productos(self):
        datos = input("Ingrese los datos del producto separados por comas: [Id, Tipo, IdSucursal, Stock]\n")
        new_data = datos.split(",")
        self.productos = self.insert_data(self.productos, new_data)

    def menu(self):
        while True:
            try:
                opcion_menu = int(input("¿Qué quieres hacer?\n1.-Insertar\n2.-Consultar\n3.-Eliminar\n4.-Salir\n"))
                if opcion_menu == 1:
                    while True:
                        try:
                            opcion_insertar = int(input("¿Dónde quieres insertar datos?\n1.-Personal\n2.-Sucursales\n3.-Productos\n4.-Salir\n"))
                            if opcion_insertar == 1:
                                self.insert_personal()
                            elif opcion_insertar == 2:
                                self.insert_sucursales()
                            elif opcion_insertar == 3:
                                self.insert_productos()
                            elif opcion_insertar == 4:
                                print("Saliendo...")
                                break
                            else:
                                print("Opción incorrecta. Por favor, elige otro número.")
                        except ValueError:
                            print("Por favor, ingresa un número entero válido.")
                        
                elif opcion_menu == 2:
                    while True:
                        try:
                            opcion_consulta = int(input("¿Cuáles datos quieres consultar?\n1.-Personal\n2.-Sucursales\n3.-Productos\n4.-Salir\n"))
                            if opcion_consulta == 1:
                                print(self.get_personal_data())
                            elif opcion_consulta == 2:
                                print(self.get_sucursales_data())
                            elif opcion_consulta == 3:
                                print(self.get_productos_data())
                            elif opcion_consulta == 4:
                                print("Saliendo...")
                                break
                            else:
                                print("Opción incorrecta. Por favor, elige otro número.")
                        except ValueError:
                            print("Por favor, ingresa un número entero válido.")
                            
                elif opcion_menu == 3:
                    while True:
                        try:
                            opcion_eliminar = int(input("¿Cuáles datos quieres eliminar?\n1.-Personal\n2.-Sucursales\n3.-Productos\n4.-Salir\n"))
                            if opcion_eliminar == 1:
                                self.delete_data(self.personal)
                                print("Eliminado correctamente")
                            elif opcion_eliminar == 2:
                                self.delete_data(self.sucursales)
                                print("Eliminado correctamente")
                            elif opcion_eliminar == 3:
                                self.delete_data(self.productos)
                                print("Eliminado correctamente")
                            elif opcion_eliminar == 4:
                                print("Saliendo...")
                                break
                            else:
                                print("Opción incorrecta. Por favor, elige otro número.")                
                        except ValueError:
                            print("Por favor, ingresa un número entero válido.")
                                
                elif opcion_menu == 4:
                    print("Saliendo...")
                    break
                else:
                    print("Opción incorrecta. Por favor, elige otro número.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    alpha = Ejercicio6()
    alpha.menu()
