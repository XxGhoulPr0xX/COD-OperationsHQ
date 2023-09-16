import sys
from PyQt5 import QtWidgets, uic
from ui_EjemploGUI_Qt import Ui_MainWindow
from Ui_Registros import Ui_RegistrosGUI

class VentanasPrueba(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Condigo de instancia a menu#
        self.MRegistros.triggered.connect(self.mostrar)
        self.MSalir.triggered.connect(self.MenuSalir)
        #Condigo de instancia a botones#
        self.btnActivar.clicked.connect(self.Activar)
        self.btnDesactivar.clicked.connect(self.Desactivar)
    
    #Creación e instanciación a la segunda ventana#
    def mostrar(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_RegistrosGUI()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        #Instancia a la función para cerrar la ventana actual#
        self.ui.btnCancelar.clicked.connect(self.CerraVentana)
    
    def CerraVentana(self):
        self.ventana.close()
    
    def MenuSalir(self):
        sys.exit()
        
    def Activar(self):
        self.lbMensaje.setText("Hola mundo!")
        
    def Desactivar(self):
        self.lbMensaje.setText("")
        self.btnActivar.setFocus()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanasPrueba()
    window.show()
    sys.exit(app.exec_())