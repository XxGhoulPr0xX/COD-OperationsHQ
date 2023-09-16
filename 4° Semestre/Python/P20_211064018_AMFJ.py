import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
suma=0
class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("P20_211064018_AMFJ_GUI.ui",self)
        self.btnMas.clicked.connect(self.Suma)

    def Suma(self):
        global suma
        suma=suma+1
        self.txtSuma.setText(str(suma))

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI=mywindow()
    GUI.show()
    sys.exit(app.exec_())
