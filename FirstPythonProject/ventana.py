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
        MainWindow.resize(742, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 721, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(290, 10, 134, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 420, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 251, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.chkEfec = QtWidgets.QCheckBox(self.tab)
        self.chkEfec.setGeometry(QtCore.QRect(430, 180, 76, 20))
        self.chkEfec.setObjectName("chkEfec")
        self.chkbxGroup = QtWidgets.QButtonGroup(MainWindow)
        self.chkbxGroup.setObjectName("chkbxGroup")
        self.chkbxGroup.addButton(self.chkEfec)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 661, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(370, 100, 37, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(260, 140, 49, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 60, 31, 24))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 60, 133, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_sx_2 = QtWidgets.QLabel(self.tab)
        self.label_sx_2.setGeometry(QtCore.QRect(310, 180, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_sx_2.setFont(font)
        self.label_sx_2.setObjectName("label_sx_2")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(40, 200, 661, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.chkTarj = QtWidgets.QCheckBox(self.tab)
        self.chkTarj.setGeometry(QtCore.QRect(500, 180, 76, 20))
        self.chkTarj.setObjectName("chkTarj")
        self.chkbxGroup.addButton(self.chkTarj)
        self.chkTrans = QtWidgets.QCheckBox(self.tab)
        self.chkTrans.setGeometry(QtCore.QRect(570, 180, 91, 20))
        self.chkTrans.setObjectName("chkTrans")
        self.chkbxGroup.addButton(self.chkTrans)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 133, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_sx = QtWidgets.QLabel(self.tab)
        self.label_sx.setGeometry(QtCore.QRect(50, 180, 49, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_sx.setFont(font)
        self.label_sx.setObjectName("label_sx")
        self.selProv = QtWidgets.QComboBox(self.tab)
        self.selProv.setGeometry(QtCore.QRect(460, 140, 211, 22))
        self.selProv.setObjectName("selProv")
        self.label_dir = QtWidgets.QLabel(self.tab)
        self.label_dir.setGeometry(QtCore.QRect(40, 140, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(40, 40, 661, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.rbtMasc = QtWidgets.QRadioButton(self.tab)
        self.rbtMasc.setGeometry(QtCore.QRect(200, 180, 89, 20))
        self.rbtMasc.setObjectName("rbtMasc")
        self.rbtnGroup = QtWidgets.QButtonGroup(MainWindow)
        self.rbtnGroup.setObjectName("rbtnGroup")
        self.rbtnGroup.addButton(self.rbtMasc)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 25, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_prov = QtWidgets.QLabel(self.tab)
        self.label_prov.setGeometry(QtCore.QRect(390, 140, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_prov.setFont(font)
        self.label_prov.setObjectName("label_prov")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(250, 420, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(280, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 140, 251, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(250, 50, 31, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 100, 251, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rbtFem = QtWidgets.QRadioButton(self.tab)
        self.rbtFem.setGeometry(QtCore.QRect(110, 180, 89, 20))
        self.rbtFem.setObjectName("rbtFem")
        self.rbtnGroup.addButton(self.rbtFem)
        self.lblStatus = QtWidgets.QLabel(self.tab)
        self.lblStatus.setGeometry(QtCore.QRect(10, 440, 671, 20))
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.saveDbButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDbButton.setGeometry(QtCore.QRect(10, 0, 31, 31))
        self.saveDbButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("SaveIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveDbButton.setIcon(icon1)
        self.saveDbButton.setObjectName("saveDbButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Xestión Clientes"))
        self.pushButton_2.setText(_translate("MainWindow", "Baja"))
        self.chkEfec.setText(_translate("MainWindow", "Efectivo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Nome:"))
        self.label_sx_2.setText(_translate("MainWindow", "Métodos de Pago:"))
        self.chkTarj.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTrans.setText(_translate("MainWindow", "Transferencia"))
        self.label_sx.setText(_translate("MainWindow", "Sexo:"))
        self.label_dir.setText(_translate("MainWindow", "Dirección:"))
        self.rbtMasc.setText(_translate("MainWindow", "Masculino"))
        self.label_2.setText(_translate("MainWindow", "DNI:"))
        self.label_prov.setText(_translate("MainWindow", "Provincia:"))
        self.pushButton.setText(_translate("MainWindow", "Alta"))
        self.label_7.setText(_translate("MainWindow", "Fecha Alta: "))
        self.label_3.setText(_translate("MainWindow", "Apelidos: "))
        self.rbtFem.setText(_translate("MainWindow", "Femenino"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab Número 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab Número 3"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
