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
        self.ui.btnMostrarR.clicked.connect(self.m_Estudiantes)
        self.ui.btnGuardar.clicked.connect(self.insert_estudiantes)
        self.ui.btnBuscarEst.clicked.connect(self.buscar_estudiante)
        self.ui.btnActualizar.clicked.connect(self.actualizar_estudiante)
        self.ui.btnEliminarEst.clicked.connect(self.eliminar_estudiante)
        
        self.ui.ListaEstudiantes.setColumnWidth(0,100)#No. control
        self.ui.ListaEstudiantes.setColumnWidth(1,180)#Nombre
        self.ui.ListaEstudiantes.setColumnWidth(2,100)#Ap paterno
        self.ui.ListaEstudiantes.setColumnWidth(3,100)#Ap materno
        self.ui.ListaEstudiantes.setColumnWidth(4,50)#Edad
        
        self.ui.tw_buscar.setColumnWidth(0,100)#No. control
        self.ui.tw_buscar.setColumnWidth(1,180)#Nombre
        self.ui.tw_buscar.setColumnWidth(2,100)#Ap paterno
        self.ui.tw_buscar.setColumnWidth(3,100)#Ap materno
        self.ui.tw_buscar.setColumnWidth(4,50)#Edad
        
        self.ui.tw_Eliminiar.setColumnWidth(0,100)#No. control
        self.ui.tw_Eliminiar.setColumnWidth(1,180)#Nombre
        self.ui.tw_Eliminiar.setColumnWidth(2,100)#Ap paterno
        self.ui.tw_Eliminiar.setColumnWidth(3,100)#Ap materno
        self.ui.tw_Eliminiar.setColumnWidth(4,50)#Edad
        
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
        
    def buscar_estudiante(self):
        nctrlEstudiante = str("'"+self.ui.txtNoCtrl.text()+"'")
        
        datosB = self.datosTotal.busca_estudiante(nctrlEstudiante)
        i = len(datosB)
        
        self.ui.tw_buscar.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tw_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tw_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1
    
    def actualizar_estudiante(self):
        nctrlEstudiante = str("'"+self.ui.txtControl_2.text()+"'")
        nctrlXX = self.datosTotal.busca_estudiante(nctrlEstudiante)
        
        if nctrlXX != None:
            nctrl = self.ui.txtControl_2.text()
            nombreM = self.ui.txtNombreModif.text()
            appaternoM = self.ui.txtApPaternoModif.text()
            apmaternoM = self.ui.txtApMaternoModif.text()
            edadM = self.ui.txtEdadModif.text()
            
            act = self.datosTotal.actualiza_estudiante(nombreM, appaternoM, apmaternoM, edadM, nctrl)
            if act == 1:
                self.ui.txtNombreModif.clear()
                self.ui.txtApPaternoModif.clear()
                self.ui.txtApMaternoModif.clear()
                self.ui.txtEdadModif.clear()
                self.ui.txtControl_2.clear()
            elif act == 0:
                self.ui.txtControl_2.setText("ERROR")
            else:
                self.ui.txtControl_2.setText("INCORRECTO")
        else:
            self.ui.txtControl_2.setText("NO EXISTE")
            
    def eliminar_estudiante(self):
        nctrlEliminar = self.ui.txtControlElim.text()
        nctrlEliminar = str("'"+nctrlEliminar+"'")
        
        resp = self.datosTotal.elimina_estudiante(nctrlEliminar)
        datos = self.datosTotal.lista_estudiantes()
        i = len(datos)
        
        self.ui.tw_Eliminiar.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tw_Eliminiar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_Eliminiar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_Eliminiar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_Eliminiar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tw_Eliminiar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1
            
        if resp == None:
            self.ui.txtControlElim.setText("NO EXISTE")
        elif resp == 0:
            self.ui.txtControlElim.setText("NO EXISTE")
        else:
            self.ui.txtControlElim.setText("SE ELIMINO")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())