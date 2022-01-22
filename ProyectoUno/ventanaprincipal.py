# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.clientes = QtWidgets.QWidget()
        self.clientes.setObjectName("clientes")
        self.lblNombre = QtWidgets.QLabel(self.clientes)
        self.lblNombre.setGeometry(QtCore.QRect(470, 120, 61, 21))
        self.lblNombre.setObjectName("lblNombre")
        self.lblValidarDNI = QtWidgets.QLabel(self.clientes)
        self.lblValidarDNI.setGeometry(QtCore.QRect(250, 100, 47, 21))
        self.lblValidarDNI.setObjectName("lblValidarDNI")
        self.leDireccion = QtWidgets.QLineEdit(self.clientes)
        self.leDireccion.setGeometry(QtCore.QRect(180, 170, 271, 20))
        self.leDireccion.setObjectName("leDireccion")
        self.line_2 = QtWidgets.QFrame(self.clientes)
        self.line_2.setGeometry(QtCore.QRect(20, 250, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lblApellidos = QtWidgets.QLabel(self.clientes)
        self.lblApellidos.setGeometry(QtCore.QRect(110, 120, 61, 21))
        self.lblApellidos.setObjectName("lblApellidos")
        self.leDNI = QtWidgets.QLineEdit(self.clientes)
        self.leDNI.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.leDNI.setObjectName("leDNI")
        self.leNombre = QtWidgets.QLineEdit(self.clientes)
        self.leNombre.setGeometry(QtCore.QRect(520, 120, 161, 20))
        self.leNombre.setObjectName("leNombre")
        self.btSalir = QtWidgets.QPushButton(self.clientes)
        self.btSalir.setGeometry(QtCore.QRect(380, 490, 75, 23))
        self.btSalir.setObjectName("btSalir")
        self.comBoxProvincia = QtWidgets.QComboBox(self.clientes)
        self.comBoxProvincia.setGeometry(QtCore.QRect(540, 170, 141, 22))
        self.comBoxProvincia.setObjectName("comBoxProvincia")
        self.lblDireccion = QtWidgets.QLabel(self.clientes)
        self.lblDireccion.setGeometry(QtCore.QRect(110, 170, 71, 16))
        self.lblDireccion.setObjectName("lblDireccion")
        self.lblFechaAlta = QtWidgets.QLabel(self.clientes)
        self.lblFechaAlta.setGeometry(QtCore.QRect(310, 80, 71, 16))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.clientes)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 220, 351, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.olPago = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.olPago.setContentsMargins(0, 0, 0, 0)
        self.olPago.setObjectName("olPago")
        self.btAceptar = QtWidgets.QPushButton(self.clientes)
        self.btAceptar.setGeometry(QtCore.QRect(280, 490, 75, 23))
        self.btAceptar.setObjectName("btAceptar")
        self.leApellidos = QtWidgets.QLineEdit(self.clientes)
        self.leApellidos.setGeometry(QtCore.QRect(170, 120, 281, 20))
        self.leApellidos.setObjectName("leApellidos")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.clientes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 220, 151, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.olSexo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.olSexo.setContentsMargins(0, 0, 0, 0)
        self.olSexo.setObjectName("olSexo")
        self.lblSexo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblSexo.setObjectName("lblSexo")
        self.olSexo.addWidget(self.lblSexo)
        self.rbMujer = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbMujer.setObjectName("rbMujer")
        self.bgSexo = QtWidgets.QButtonGroup(MainWindow)
        self.bgSexo.setObjectName("bgSexo")
        self.bgSexo.addButton(self.rbMujer)
        self.olSexo.addWidget(self.rbMujer)
        self.rbHombre = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbHombre.setObjectName("rbHombre")
        self.bgSexo.addButton(self.rbHombre)
        self.olSexo.addWidget(self.rbHombre)
        self.line = QtWidgets.QFrame(self.clientes)
        self.line.setGeometry(QtCore.QRect(20, 60, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblProvincia = QtWidgets.QLabel(self.clientes)
        self.lblProvincia.setGeometry(QtCore.QRect(470, 170, 71, 16))
        self.lblProvincia.setObjectName("lblProvincia")
        self.btCalendario = QtWidgets.QPushButton(self.clientes)
        self.btCalendario.setGeometry(QtCore.QRect(500, 80, 21, 21))
        self.btCalendario.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calendar-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCalendario.setIcon(icon)
        self.btCalendario.setObjectName("btCalendario")
        self.lblTitulo = QtWidgets.QLabel(self.clientes)
        self.lblTitulo.setGeometry(QtCore.QRect(270, 30, 221, 41))
        self.lblTitulo.setObjectName("lblTitulo")
        self.leFecha = QtWidgets.QLineEdit(self.clientes)
        self.leFecha.setGeometry(QtCore.QRect(380, 80, 113, 20))
        self.leFecha.setObjectName("leFecha")
        self.lblDNI = QtWidgets.QLabel(self.clientes)
        self.lblDNI.setGeometry(QtCore.QRect(110, 80, 31, 21))
        self.lblDNI.setObjectName("lblDNI")
        self.cbTransferencia = QtWidgets.QCheckBox(self.clientes)
        self.cbTransferencia.setGeometry(QtCore.QRect(561, 227, 89, 17))
        self.cbTransferencia.setObjectName("cbTransferencia")
        self.label = QtWidgets.QLabel(self.clientes)
        self.label.setGeometry(QtCore.QRect(301, 221, 117, 29))
        self.label.setObjectName("label")
        self.cbEfectivo = QtWidgets.QCheckBox(self.clientes)
        self.cbEfectivo.setGeometry(QtCore.QRect(424, 227, 63, 17))
        self.cbEfectivo.setObjectName("cbEfectivo")
        self.cbTarjeta = QtWidgets.QCheckBox(self.clientes)
        self.cbTarjeta.setGeometry(QtCore.QRect(493, 227, 62, 17))
        self.cbTarjeta.setObjectName("cbTarjeta")
        self.cliTabla = QtWidgets.QTableWidget(self.clientes)
        self.cliTabla.setGeometry(QtCore.QRect(20, 270, 751, 211))
        self.cliTabla.setObjectName("cliTabla")
        self.cliTabla.setColumnCount(3)
        self.cliTabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cliTabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cliTabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cliTabla.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.clientes, "")
        self.facturacion = QtWidgets.QWidget()
        self.facturacion.setObjectName("facturacion")
        self.tabWidget.addTab(self.facturacion, "")
        self.productos = QtWidgets.QWidget()
        self.productos.setObjectName("productos")
        self.tabWidget.addTab(self.productos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblNombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Nome:</span></p></body></html>"))
        self.lblValidarDNI.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lblApellidos.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Apelidos:</span></p></body></html>"))
        self.btSalir.setText(_translate("MainWindow", "Saír"))
        self.lblDireccion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Dirección:</span></p></body></html>"))
        self.lblFechaAlta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Data Alta:</span></p></body></html>"))
        self.btAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.lblSexo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sexo:</span></p></body></html>"))
        self.rbMujer.setText(_translate("MainWindow", "Muller"))
        self.rbHombre.setText(_translate("MainWindow", "Home"))
        self.lblProvincia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Provincia:</span></p></body></html>"))
        self.lblTitulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">XESTIÓN CLIENTES</span></p></body></html>"))
        self.lblDNI.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">DNI:</span></p></body></html>"))
        self.cbTransferencia.setText(_translate("MainWindow", "Transferencia"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Métodos de pago:</span></p></body></html>"))
        self.cbEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.cbTarjeta.setText(_translate("MainWindow", "Tarxeta"))
        item = self.cliTabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.cliTabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apelidos"))
        item = self.cliTabla.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nome"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clientes), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.facturacion), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productos), _translate("MainWindow", "Productos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+4"))
