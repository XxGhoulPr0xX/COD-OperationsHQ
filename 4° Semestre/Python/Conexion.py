import mysql.connector

class Registros_datos():
    def __int__(self):
        self.conexion= mysql.connector.connect(host="localhost",user="root",passwd="Valeverga616",database="tienda")

    def inserta_estudiante(self,nctrl,nombre,appaterno,apmaterno,edad):
        cur=self.conexion.cursor()
        sql="insert int estudiantes (nctrl,nombre,apppaterno,appmaterno,edad) values ('{}','{}','{}','{}','{}')".format(nctrl,nombre,appaterno,apmaterno,edad)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def lista_estudiantes(self):
        cur = self.conexion.cursor()
        sql= "select * from estudiantes"
        cur.execute(sql)
        registros = cur.fetchall()
        return registros