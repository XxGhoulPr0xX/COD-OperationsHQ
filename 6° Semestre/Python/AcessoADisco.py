class LectorArchivo:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_archivo(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            return f"El archivo {self.ruta_archivo} no se encontró."
        except Exception as e:
            return f"Ocurrió un error al leer el archivo: {str(e)}"

ruta_del_archivo = 'C:\\Users\\XxGho\\Documents\\Escuela\\6° Semestre\\Redes de Computadoras\\Ip Telefonos.txt'  # Reemplaza 'ejemplo.txt' con la ruta de tu archivo
lector = LectorArchivo(ruta_del_archivo)

contenido_archivo = lector.leer_archivo()
print(contenido_archivo)
