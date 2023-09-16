import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost",
                                                user="root",
                                                passwd="",
                                                database="tienda")
    
    def inserta(self,codigo,nombre,precio,nombre_fabricante):
        cur = self.conexion.cursor()
        sql="insert into producto (codigo,code,nombre,precio,nombre_fabricante) values ('{}','{}','{}','{}','{}')".format(codigo,codigo,nombre,precio,nombre_fabricante)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        
    def lista_Producto(self):
        cur = self.conexion.cursor()
        sql = "select * from producto"
        cur.execute(sql)
        registros = cur.fetchall()
        return registros
    
    def busca_producto(self, codigo):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo = {}".format(codigo)
        cur.execute(sql)
        code = cur.fetchall()
        cur.close
        return code

    def busca_eliminar(self, codigo):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo = {}".format(codigo)
        cur.execute(sql)
        code = cur.fetchall()
        cur.close
        return code

    def busca_modificar(self, codigo):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo = {}".format(codigo)
        cur.execute(sql)
        code = cur.fetchall()
        cur.close
        return code
    
    def moodificar_producto(self, nombre, precio, nombre_fabricante, codigo):
        cur = self.conexion.cursor()
        sql = "update producto set nombre = '{}', precio = '{}', nombre_fabricante = '{}' where codigo = '{}'".format(nombre, precio, nombre_fabricante, codigo)
        cur.execute(sql)
        act = cur.rowcount
        self.conexion.commit()
        cur.close()
        return act

    def elimina_Producto(self, codigoEliminar):
        cur = self. conexion.cursor()
        sql = "delete from producto where codigo = '{}'".format(codigoEliminar)
        cur.execute(sql)
        codigo = cur.rowcount
        self.conexion.commit()
        cur.close()
        return codigo

    def consulta1(self):
        cur = self.conexion.cursor()
        sql = "select * from producto"
        cur.execute(sql)
        consultas1 = cur.fetchall()
        return consultas1

    def consulta2(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo>=4"
        cur.execute(sql)
        consultas2 = cur.fetchall()
        return consultas2

    def consulta3(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where precio>=400"
        cur.execute(sql)
        consultas3 = cur.fetchall()
        return consultas3

    def consulta4(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where nombre='Monitor 27 LED Full HD'"
        cur.execute(sql)
        consultas4 = cur.fetchall()
        return consultas4

    def consulta5(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where precio=755"
        cur.execute(sql)
        consultas5 = cur.fetchall()
        return consultas5

    def consulta6(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo=11"
        cur.execute(sql)
        consultas6 = cur.fetchall()
        return consultas6

    def consulta7(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where precio=86.99"
        cur.execute(sql)
        consultas7 = cur.fetchall()
        return consultas7

    def consulta8(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo=10"
        cur.execute(sql)
        consultas8 = cur.fetchall()
        return consultas8

    def consulta9(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo=6"
        cur.execute(sql)
        consultas9 = cur.fetchall()
        return consultas9

    def consulta10(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo=5"
        cur.execute(sql)
        consulta10 = cur.fetchall()
        return consulta10

    def consulta11(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where precio=444"
        cur.execute(sql)
        consulta11 = cur.fetchall()
        return consulta11

    def consulta12(self):
        cur = self.conexion.cursor()
        sql = "select * from producto where codigo=9"
        cur.execute(sql)
        consulta12 = cur.fetchall()
        return consulta12