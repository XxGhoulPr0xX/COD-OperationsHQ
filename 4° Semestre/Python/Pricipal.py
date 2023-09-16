import sys
from Ui_CRUD import *
from Conexion import *
from PyQt5.QtWidgets import QTableWidgetItem

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.iu.btnMostrarR.clicked.connect(self.m_Estudiantes)
        self.ui.btnGuardar.clicked.connect(self.insert_estudiantes)

        self.ui.ListaEstudiantes.setColumnwidth(0,100)#No.Control
        self.ui.ListaEstudiantes.setColumnwidth(1,180)#Nombre
        self.ui.ListaEstudiantes.setColumnwidth(2,100)#Ap paterno
        self.ui.ListaEstudiantes.setColumnwidth(3,100)#Ap materno
        self.ui.ListaEstudiantes.setColumnwidth(4,50)#Edad

    def m_Estudiantes(self):
        datos = self.datosTotal.lista_estudiantes()
        i = len(datos)

        self.ui.ListaEstudiantes.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaEstudiantes.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaEstudiantes.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaEstudiantes.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaEstudiantes.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.ListaEstudiantes.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    def insert_estudiantes(self):
        nctrl = self.ui.txtControl.text()
        nombre = self.ui.txtNombre.text()
        appaterno = self.ui.txtApPaterno.text()
        apmaterno = self.ui.txtApMaterno.text()
        edad = self.ui.txtEdad.text()

        self.datosTotal.inserta_estudiante(nctrl,nombre,appaterno,apmaterno,edad)
        self.ui.txtControl.clear()
        self.ui.txtNombre.clear()
        self.ui.txtApPaterno.clear()
        self.ui.txtApMaterno.clear()
        self.ui.txtEdad.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
