import random
import sys
from PaquetesNecesarios import Ejercicio19
from PyQt5 import QtCore, QtGui, QtWidgets
from P19_211064018_AMFJ_GUI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.btnIniciar.clicked.connect(self.Iniciador)

    def Iniciador(self):
        Ejercicio19.iniciador(random.randrange(1, 10, 1))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    #window.MSalir.triggered.connect(window.MenuSalir)
    sys.exit(app.exec_())