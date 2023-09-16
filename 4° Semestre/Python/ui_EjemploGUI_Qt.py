# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\CURSO AGO-DIC 22\Ejemplo Python\TopicosAvanzados\EjemplosGUI\EjemploGUI_Qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(375, 171)
        Principal.setStyleSheet("background-color: rgb(98, 108, 235);")
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnActivar = QtWidgets.QPushButton(self.centralwidget)
        self.btnActivar.setGeometry(QtCore.QRect(50, 40, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnActivar.setFont(font)
        self.btnActivar.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.btnActivar.setObjectName("btnActivar")
        self.btnDesactivar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDesactivar.setGeometry(QtCore.QRect(210, 40, 93, 28))
        self.btnDesactivar.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.btnDesactivar.setObjectName("btnDesactivar")
        self.lbMensaje = QtWidgets.QLabel(self.centralwidget)
        self.lbMensaje.setGeometry(QtCore.QRect(30, 100, 281, 21))
        self.lbMensaje.setStyleSheet("background-color: rgb(42, 255, 56);")
        self.lbMensaje.setText("")
        self.lbMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lbMensaje.setObjectName("lbMensaje")
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Principal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 375, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuPrincipal = QtWidgets.QMenu(self.menuBar)
        self.menuPrincipal.setObjectName("menuPrincipal")
        Principal.setMenuBar(self.menuBar)
        self.actionRegistros = QtWidgets.QAction(Principal)
        self.actionRegistros.setObjectName("actionRegistros")
        self.actionEjercicios = QtWidgets.QAction(Principal)
        self.actionEjercicios.setObjectName("actionEjercicios")
        self.MSalir = QtWidgets.QAction(Principal)
        self.MSalir.setObjectName("MSalir")
        self.menuPrincipal.addAction(self.actionRegistros)
        self.menuPrincipal.addAction(self.actionEjercicios)
        self.menuPrincipal.addSeparator()
        self.menuPrincipal.addAction(self.MSalir)
        self.menuBar.addAction(self.menuPrincipal.menuAction())

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Principal"))
        self.btnActivar.setText(_translate("Principal", "Activar"))
        self.btnDesactivar.setText(_translate("Principal", "Desactivar"))
        self.menuPrincipal.setTitle(_translate("Principal", "Principal"))
        self.actionRegistros.setText(_translate("Principal", "Registros"))
        self.actionEjercicios.setText(_translate("Principal", "Ejercicios"))
        self.MSalir.setText(_translate("Principal", "Salir"))
        self.MSalir.setShortcut(_translate("Principal", "Ctrl+Del"))
