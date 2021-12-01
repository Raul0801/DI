# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(220, 20, 101, 16))
        self.labelTitulo.setObjectName("labelTitulo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelDni = QtWidgets.QLabel(self.centralwidget)
        self.labelDni.setGeometry(QtCore.QRect(10, 70, 25, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelDni.setFont(font)
        self.labelDni.setObjectName("labelDni")
        self.lineEditDni = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDni.setGeometry(QtCore.QRect(50, 70, 133, 22))
        self.lineEditDni.setObjectName("lineEditDni")
        self.labelFecha = QtWidgets.QLabel(self.centralwidget)
        self.labelFecha.setGeometry(QtCore.QRect(250, 70, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelFecha.setFont(font)
        self.labelFecha.setObjectName("labelFecha")
        self.lineEditFecha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFecha.setEnabled(False)
        self.lineEditFecha.setGeometry(QtCore.QRect(370, 70, 133, 22))
        self.lineEditFecha.setObjectName("lineEditFecha")
        self.pushButtonCalendar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalendar.setGeometry(QtCore.QRect(520, 70, 31, 24))
        self.pushButtonCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCalendar.setIcon(icon)
        self.pushButtonCalendar.setObjectName("pushButtonCalendar")
        self.labelAp1 = QtWidgets.QLabel(self.centralwidget)
        self.labelAp1.setGeometry(QtCore.QRect(10, 120, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelAp1.setFont(font)
        self.labelAp1.setObjectName("labelAp1")
        self.labelAp2 = QtWidgets.QLabel(self.centralwidget)
        self.labelAp2.setGeometry(QtCore.QRect(260, 120, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelAp2.setFont(font)
        self.labelAp2.setObjectName("labelAp2")
        self.lineEditAp1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAp1.setGeometry(QtCore.QRect(80, 120, 161, 22))
        self.lineEditAp1.setObjectName("lineEditAp1")
        self.lineEditAp2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAp2.setGeometry(QtCore.QRect(330, 120, 161, 22))
        self.lineEditAp2.setObjectName("lineEditAp2")
        self.labelNom = QtWidgets.QLabel(self.centralwidget)
        self.labelNom.setGeometry(QtCore.QRect(20, 170, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelNom.setFont(font)
        self.labelNom.setObjectName("labelNom")
        self.lineEditNom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNom.setGeometry(QtCore.QRect(80, 170, 161, 22))
        self.lineEditNom.setObjectName("lineEditNom")
        self.rbtRet = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtRet.setGeometry(QtCore.QRect(70, 220, 89, 20))
        self.rbtRet.setObjectName("rbtRet")
        self.buttonGroupRetIn = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroupRetIn.setObjectName("buttonGroupRetIn")
        self.buttonGroupRetIn.addButton(self.rbtRet)
        self.rbtIng = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtIng.setGeometry(QtCore.QRect(160, 220, 89, 20))
        self.rbtIng.setObjectName("rbtIng")
        self.buttonGroupRetIn.addButton(self.rbtIng)
        self.lineEditCant = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCant.setGeometry(QtCore.QRect(100, 270, 161, 22))
        self.lineEditCant.setObjectName("lineEditCant")
        self.labelCant = QtWidgets.QLabel(self.centralwidget)
        self.labelCant.setGeometry(QtCore.QRect(20, 270, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelCant.setFont(font)
        self.labelCant.setObjectName("labelCant")
        self.pushButtonAc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAc.setGeometry(QtCore.QRect(140, 380, 75, 24))
        self.pushButtonAc.setObjectName("pushButtonAc")
        self.pushButtonSal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSal.setGeometry(QtCore.QRect(270, 380, 75, 24))
        self.pushButtonSal.setObjectName("pushButtonSal")
        self.lineEditSaldo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSaldo.setEnabled(False)
        self.lineEditSaldo.setGeometry(QtCore.QRect(370, 251, 161, 61))
        self.lineEditSaldo.setObjectName("lineEditSaldo")
        self.labelSaldo = QtWidgets.QLabel(self.centralwidget)
        self.labelSaldo.setGeometry(QtCore.QRect(290, 270, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelSaldo.setFont(font)
        self.labelSaldo.setObjectName("labelSaldo")
        self.labelValDni = QtWidgets.QLabel(self.centralwidget)
        self.labelValDni.setGeometry(QtCore.QRect(210, 60, 31, 31))
        self.labelValDni.setText("")
        self.labelValDni.setObjectName("labelValDni")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", "CUENTA CLIENTES"))
        self.labelDni.setText(_translate("MainWindow", "DNI:"))
        self.labelFecha.setText(_translate("MainWindow", "Fecha Nacimiento:"))
        self.labelAp1.setText(_translate("MainWindow", "Apelidos 1: "))
        self.labelAp2.setText(_translate("MainWindow", "Apelidos 2: "))
        self.labelNom.setText(_translate("MainWindow", "Nombre:"))
        self.rbtRet.setText(_translate("MainWindow", "Retirar"))
        self.rbtIng.setText(_translate("MainWindow", "Ingresar"))
        self.labelCant.setText(_translate("MainWindow", "Cantidad:"))
        self.pushButtonAc.setText(_translate("MainWindow", "Aceptar"))
        self.pushButtonSal.setText(_translate("MainWindow", "Salir"))
        self.lineEditSaldo.setText(_translate("MainWindow", "0"))
        self.labelSaldo.setText(_translate("MainWindow", "SALDO:"))
