# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonDel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDel.setGeometry(QtCore.QRect(220, 130, 61, 31))
        self.buttonDel.setObjectName("buttonDel")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(80, 170, 61, 51))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(150, 170, 61, 51))
        self.button3.setObjectName("button3")
        self.buttonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlus.setGeometry(QtCore.QRect(220, 170, 61, 51))
        self.buttonPlus.setObjectName("buttonPlus")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(80, 220, 61, 51))
        self.button5.setObjectName("button5")
        self.buttonMin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMin.setGeometry(QtCore.QRect(220, 220, 61, 51))
        self.buttonMin.setObjectName("buttonMin")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(150, 220, 61, 51))
        self.button6.setObjectName("button6")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(10, 220, 61, 51))
        self.button4.setObjectName("button4")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(80, 270, 61, 51))
        self.button8.setObjectName("button8")
        self.buttonMul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMul.setGeometry(QtCore.QRect(220, 270, 61, 51))
        self.buttonMul.setObjectName("buttonMul")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(150, 270, 61, 51))
        self.button9.setObjectName("button9")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(10, 270, 61, 51))
        self.button7.setObjectName("button7")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(80, 320, 61, 51))
        self.button0.setObjectName("button0")
        self.buttonDiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDiv.setGeometry(QtCore.QRect(220, 320, 61, 51))
        self.buttonDiv.setObjectName("buttonDiv")
        self.buttonEq = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEq.setGeometry(QtCore.QRect(150, 320, 61, 51))
        self.buttonEq.setObjectName("buttonEq")
        self.buttonC = QtWidgets.QPushButton(self.centralwidget)
        self.buttonC.setGeometry(QtCore.QRect(10, 320, 61, 51))
        self.buttonC.setObjectName("buttonC")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.buttonDel.setText(_translate("MainWindow", "DEL"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.buttonPlus.setText(_translate("MainWindow", "+"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.buttonMin.setText(_translate("MainWindow", "-"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.buttonMul.setText(_translate("MainWindow", "*"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.buttonDiv.setText(_translate("MainWindow", "/"))
        self.buttonEq.setText(_translate("MainWindow", "="))
        self.buttonC.setText(_translate("MainWindow", "C"))
