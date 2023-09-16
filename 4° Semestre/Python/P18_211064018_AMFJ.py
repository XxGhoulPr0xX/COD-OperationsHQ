import random
from PaquetesNecesarios import Ejercicio18
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("P18_211064018_AMFJ_GUI.ui",self)
        self.btnMovistar.clicked.connect(self.Movistar)
        self.btnUnefon.clicked.connect(self.Unefon)
        self.btnTelcel.clicked.connect(self.Telcel)
        self.btnATT.clicked.connect(self.ATT)
        self.btnLLamarTodos.clicked.connect(self.LlamarTodos)
    def Movistar(self):
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Movistar", random.randint(1, 2))
    def Unefon(self):
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Unefon", random.randint(1, 2))
    def Telcel(self):
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Telcel", random.randint(1, 2))
    def ATT(self):
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "ATT", random.randint(1, 2))
    def LlamarTodos(self):
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "ATT", random.randint(1, 2))
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Telcel", random.randint(1, 2))
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Unefon", random.randint(1, 2))
        Ejercicio18.iniciador(random.randrange(1, 10, 1), "Movistar", random.randint(1, 2))

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI=mywindow()
    GUI.show()
    sys.exit(app.exec_())