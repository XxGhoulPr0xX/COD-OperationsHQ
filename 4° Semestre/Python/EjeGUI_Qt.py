import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_EjemploGUI_Qt import Ui_Principal

class mywindow(QtWidgets.QMainWindow, Ui_Principal):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.MSalir.triggered.connect(self.MenuSalir)
        self.btnActivar.clicked.connect(self.Activar)
        self.btnDesactivar.clicked.connect(self.Desactivar)
        
    def MenuSalir(self):
        sys.exit()
        
    def Activar(self):
        self.lbMensaje.setText("Hola mundo!")
        
    def Desactivar(self):
        self.lbMensaje.setText("")
        self.btnActivar.setFocus()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    #window.MSalir.triggered.connect(window.MenuSalir)
    sys.exit(app.exec_())