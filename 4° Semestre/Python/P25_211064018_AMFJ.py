import sys
from P25_211064018_AMFJ_GUI import *
from PaquetesNecesarios.Ejercicio25 import *


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        # =========================================================
        self.ui.btnMostrarR.clicked.connect(self.m_Producto)
        self.ui.btnGuardar.clicked.connect(self.insertar_producto)
        self.ui.btnBuscarProducto.clicked.connect(self.buscar_producto)
        self.ui.btnBuscarEliminar.clicked.connect(self.buscar_eliminar)
        self.ui.btnBuscarEst2.clicked.connect(self.busca_modificar)
        self.ui.btnActualizar.clicked.connect(self.actualizar_producto)
        self.ui.btnEliminarEst.clicked.connect(self.eliminar_producto)
        # =========================================================
        self.ui.btnConsultas1.clicked.connect(self.consulta1)
        self.ui.btnConsulta2.clicked.connect(self.consulta2)
        self.ui.btnConsultas3.clicked.connect(self.consulta3)
        self.ui.btnConsultas4.clicked.connect(self.consulta4)
        self.ui.btnConsultas5.clicked.connect(self.consulta5)
        self.ui.btnConsulta6.clicked.connect(self.consulta6)
        self.ui.btnConsulta7.clicked.connect(self.consulta7)
        self.ui.btnConsulta8.clicked.connect(self.consulta8)
        self.ui.btnConsulta9.clicked.connect(self.consulta9)
        self.ui.btnConsulta10.clicked.connect(self.consulta10)
        self.ui.btnConsulta11.clicked.connect(self.consulta11)
        self.ui.btnConsulta12.clicked.connect(self.consulta12)
        # =========================================================
        self.ui.ListaProducto.setColumnWidth(0, 100)  # Codigo
        self.ui.ListaProducto.setColumnWidth(1, 100)  # Nomb.Producto
        self.ui.ListaProducto.setColumnWidth(2, 100)  # Precio
        self.ui.ListaProducto.setColumnWidth(3, 100)  # Nomb.Fabricante
        self.ui.ListaProducto.setColumnWidth(4, 100)  # Nomb.Fabricante

        self.ui.tw_buscar.setColumnWidth(0, 100)  # Codigo
        self.ui.tw_buscar.setColumnWidth(1, 180)  # Nomb.Producto
        self.ui.tw_buscar.setColumnWidth(2, 100)  # Precio
        self.ui.tw_buscar.setColumnWidth(3, 100)  # Nomb.Fabricante
        self.ui.tw_buscar.setColumnWidth(4, 100)  # Nomb.Fabricante

        self.ui.tw_Eliminiar.setColumnWidth(0, 100)  # Codigo
        self.ui.tw_Eliminiar.setColumnWidth(1, 100)  # Nomb.Producto
        self.ui.tw_Eliminiar.setColumnWidth(2, 100)  # Codigo
        self.ui.tw_Eliminiar.setColumnWidth(3, 100)  # Codigo

        self.ui.tw_Modificar.setColumnWidth(0, 100)  # Codigo
        self.ui.tw_Modificar.setColumnWidth(1, 100)  # Nomb.Producto
        self.ui.tw_Modificar.setColumnWidth(2, 100)  # Codigo
        self.ui.tw_Modificar.setColumnWidth(3, 100)  # Nomb.Fabricante
        self.ui.tw_Modificar.setColumnWidth(4, 100)  # Nomb.Fabricante

    # ********************************************************************************************
    def m_Producto(self):
        datos = self.datosTotal.lista_Producto()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.ListaProducto.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    # ********************************************************************************************
    def insertar_producto(self):
        codigo = self.ui.txtCodigoProducto.text()
        nombre = self.ui.txtNombProducto.text()
        precio = self.ui.txtPrecio.text()
        nombre_fabricante = self.ui.txtNombreFabricanteProducto.text()

        self.datosTotal.inserta(codigo, nombre, precio, nombre_fabricante)
        self.ui.txtCodigoProducto.clear()
        self.ui.txtNombProducto.clear()
        self.ui.txtPrecio.clear()
        self.ui.txtNombreFabricanteProducto.clear()

    # ********************************************************************************************
    def buscar_producto(self):  # Listo
        codigo = str("'" + self.ui.txtCodigoBuscar.text() + "'")

        datosB = self.datosTotal.busca_producto(codigo)
        i = len(datosB)

        self.ui.tw_buscar.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tw_buscar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_buscar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_buscar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_buscar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tw_buscar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    # *******************************************************************************************
    def actualizar_producto(self):
        codigoProducto = str(" " + self.ui.txtCodigoModif.text() + " ")
        codigoXX = self.datosTotal.busca_producto(codigoProducto)
        if codigoXX != None:
            codigoM = self.ui.txtCodigoModif.text()
            nombreM = self.ui.txtNomProModif.text()
            precioM = self.ui.txtPrecioModif.text()
            fabricanteM = self.ui.txtFabModif.text()

            act = self.datosTotal.moodificar_producto(nombreM, precioM, fabricanteM, codigoM)
            if act == 1:
                self.ui.txtNomProModif.clear()
                self.ui.txtPrecioModif.clear()
                self.ui.txtFabModif.clear()
                self.ui.txtCodigoModif.clear()
            elif act == 0:
                self.ui.txtCodigoModif.setText("ERROR")
            else:
                self.ui.txtCodigoModif.setText("INCORRECTO")
        else:
            self.ui.txtCodigoModif.setText("NO EXISTE")

    # *******************************************************************************************
    def busca_modificar(self):  # Listo
        codigo = str("'" + self.ui.txtCodigoModif.text() + "'")
        datosB = self.datosTotal.busca_modificar(codigo)
        i = len(datosB)

        self.ui.tw_Modificar.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tw_Modificar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_Modificar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_Modificar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_Modificar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tw_Modificar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    # **************************************************************************************************
    def eliminar_producto(self):
        codigoEliminar = self.ui.txtCodigoElim.text()
        codigoEliminar = str(" " + codigoEliminar + "")

        resp = self.datosTotal.elimina_Producto(codigoEliminar)
        datos = self.datosTotal.lista_Producto()
        i = len(datos)

        self.ui.tw_Eliminiar.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.tw_Eliminiar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_Eliminiar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_Eliminiar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_Eliminiar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

        if resp == None:
            self.ui.txtCodigoElim.setText("NO EXISTE")
        elif resp == 0:
            self.ui.txtCodigoElim.setText("NO EXISTE")
        else:
            self.ui.txtCodigoElim.setText("SE ELIMINO")

    # **************************************************************************************************
    def buscar_eliminar(self):  # Listo
        codigo = str("'" + self.ui.txtCodigoElim.text() + "'")
        datosB = self.datosTotal.busca_eliminar(codigo)
        i = len(datosB)

        self.ui.tw_Eliminiar.setRowCount(i)
        tablerow = 0

        for row in datosB:
            self.ui.tw_Eliminiar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tw_Eliminiar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tw_Eliminiar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tw_Eliminiar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tw_Eliminiar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    # **************************************************************************************************
    def consulta1(self):
        datos = self.datosTotal.consulta1()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    # =================================================================================================
    def consulta2(self):
        datos = self.datosTotal.consulta2()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    # **************************************************************************************************
    def consulta3(self):
        datos = self.datosTotal.consulta3()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    # =================================================================================================
    def consulta4(self):
        datos = self.datosTotal.consulta4()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    # **************************************************************************************************
    def consulta5(self):
        datos = self.datosTotal.consulta5()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    # =================================================================================================
    def consulta6(self):
        datos = self.datosTotal.consulta6()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta7(self):
        datos = self.datosTotal.consulta7()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta8(self):
        datos = self.datosTotal.consulta8()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta9(self):
        datos = self.datosTotal.consulta9()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta10(self):
        datos = self.datosTotal.consulta10()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta11(self):
        datos = self.datosTotal.consulta11()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            self.ui.ListaProducto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))  # Precio
            tablerow += 1

    # =================================================================================================
    def consulta12(self):
        datos = self.datosTotal.consulta12()
        i = len(datos)

        self.ui.ListaProducto.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.ListaProducto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Nombre
            self.ui.ListaProducto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))  # Precio
            tablerow += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
