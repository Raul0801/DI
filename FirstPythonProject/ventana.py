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
        MainWindow.resize(682, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 134, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 133, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 25, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 110, 251, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 110, 37, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 110, 251, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 661, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 240, 661, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 260, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 260, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 110, 49, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_sx = QtWidgets.QLabel(self.centralwidget)
        self.label_sx.setGeometry(QtCore.QRect(20, 190, 49, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_sx.setFont(font)
        self.label_sx.setObjectName("label_sx")
        self.label_sx_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sx_2.setGeometry(QtCore.QRect(280, 190, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_sx_2.setFont(font)
        self.label_sx_2.setObjectName("label_sx_2")
        self.rbtFem = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtFem.setGeometry(QtCore.QRect(80, 190, 89, 20))
        self.rbtFem.setObjectName("rbtFem")
        self.rbtnGroup = QtWidgets.QButtonGroup(MainWindow)
        self.rbtnGroup.setObjectName("rbtnGroup")
        self.rbtnGroup.addButton(self.rbtFem)
        self.rbtMasc = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtMasc.setGeometry(QtCore.QRect(170, 190, 89, 20))
        self.rbtMasc.setObjectName("rbtMasc")
        self.rbtnGroup.addButton(self.rbtMasc)
        self.chkEfec = QtWidgets.QCheckBox(self.centralwidget)
        self.chkEfec.setGeometry(QtCore.QRect(400, 190, 76, 20))
        self.chkEfec.setObjectName("chkEfec")
        self.chkbxGroup = QtWidgets.QButtonGroup(MainWindow)
        self.chkbxGroup.setObjectName("chkbxGroup")
        self.chkbxGroup.addButton(self.chkEfec)
        self.chkTarj = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTarj.setGeometry(QtCore.QRect(470, 190, 76, 20))
        self.chkTarj.setObjectName("chkTarj")
        self.chkbxGroup.addButton(self.chkTarj)
        self.chkTrans = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTrans.setGeometry(QtCore.QRect(540, 190, 91, 20))
        self.chkTrans.setObjectName("chkTrans")
        self.chkbxGroup.addButton(self.chkTrans)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 150, 49, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setGeometry(QtCore.QRect(10, 150, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 150, 251, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_prov = QtWidgets.QLabel(self.centralwidget)
        self.label_prov.setGeometry(QtCore.QRect(360, 150, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_prov.setFont(font)
        self.label_prov.setObjectName("label_prov")
        self.selProv = QtWidgets.QComboBox(self.centralwidget)
        self.selProv.setGeometry(QtCore.QRect(430, 150, 211, 22))
        self.selProv.setObjectName("selProv")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 70, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 70, 133, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 70, 31, 24))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Xestión Clientes"))
        self.label_2.setText(_translate("MainWindow", "DNI:"))
        self.label_3.setText(_translate("MainWindow", "Apelidos: "))
        self.label_4.setText(_translate("MainWindow", "Nome:"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
        self.label_sx.setText(_translate("MainWindow", "Sexo:"))
        self.label_sx_2.setText(_translate("MainWindow", "Métodos de Pago:"))
        self.rbtFem.setText(_translate("MainWindow", "Femenino"))
        self.rbtMasc.setText(_translate("MainWindow", "Masculino"))
        self.chkEfec.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarj.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTrans.setText(_translate("MainWindow", "Transferencia"))
        self.label_dir.setText(_translate("MainWindow", "Dirección:"))
        self.label_prov.setText(_translate("MainWindow", "Provincia:"))
        self.label_7.setText(_translate("MainWindow", "Fecha Alta: "))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
