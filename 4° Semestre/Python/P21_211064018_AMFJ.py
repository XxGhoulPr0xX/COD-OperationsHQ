import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

resta=100
class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("P21_211064018_AMFJ_GUI.ui",self)
        self.btnMas.clicked.connect(self.Suma)

    def Suma(self):
        global resta
        resta=resta-1
        if(resta==0):
            resta=100
        self.txtSuma.setText(str(resta))

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI=mywindow()
    GUI.show()
    sys.exit(app.exec_())
