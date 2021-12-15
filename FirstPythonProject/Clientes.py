import conexion
from ventana import *
import sys
import var
import events

class Clientes():

    def validarDNI():
        try:
            dni = var.ui.lineEdit.text()
            var.ui.lineEdit.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.label_5.setStyleSheet('QLabel {color:green;}')
                    var.ui.label_5.setText('V')
                else:
                    var.ui.label_5.setStyleSheet('QLabel {color:red;}')
                    var.ui.label_5.setText('X')
            else:
                var.ui.label_5.setStyleSheet('QLabel {color:red;}')
                var.ui.label_5.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def cargarProv():
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.selProv.addItem(i)
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def abrirCalendar():
        try:
            var.dlgCalendar.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data =('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lineEdit_5.setText(str(data))
            var.dlgCalendar.hide
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarCliente(self):
        try:
            fila = var.ui.tableWidget.selectedItems()
            client = [var.ui.lineEdit, var.ui.lineEdit_2, var.ui.lineEdit_3]
            if fila:
                fila = [dato.text() for dato in fila]
            print(fila)
            i = 0
            for i, dato in enumerate(client):
                dato.setText(fila[i])
        except Exception as error:
            print('Error: %s' % str(error))

    def altaClientes(self=None):
        try:
            newCli = []
            cliTab = []
            client =[var.ui.lineEdit, var.ui.lineEdit_2, var.ui.lineEdit_3, var.ui.lineEdit_5, var.ui.lineEdit_4 ]
            k = 0
            for i in client:
                newCli.append(i.text())
                if k < 3:
                    cliTab.append(i.text())
                    k += 1
            newCli.append(var.vpro)
            var.pay2 = events.Eventos.selPago(self)
            var.pay = set(var.pay)
            newCli.append(var.sex)
            if client:
                row = 0
                column = 0
                var.ui.tableWidget.insertRow(row)
                for registro in cliTab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tableWidget.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.cargarCli(newCli)
            else:
                print('Faltan datos')
            Clientes.limpiarCli(client, var.rbtnGroup , var.chkbxGroup)
            conexion.Conexion.cargarCli(newCli)
        except Exception as error:
            print('Error: %s' % str(error))

    def limpiarCli(listaEditCli, listaRbtnSex, listaChkpay):
        try:
            for i in range(len(listaEditCli)):
                listaEditCli[i].setText('')
            var.ui.chkbxGroup.setExclusive(False)
            var.ui.rbtnGroup.setExclusive(False)
            for dato in listaRbtnSex:
                dato.setChecked(False)
            for dato in listaChkpay:
                dato.setChecked(False)
            var.ui.selProv.setCurrentIndex(0)
            var.ui.label_5.setText('')
        except Exception as error:
            print('Error: %s' % str(error))

    def bajaCliente(self):
        try:
            dni = var.ui.lineEdit.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarCli(self)
            Clientes.limpiarCli(var.ui.tableWidget, var.ui.rbtnGroup, var.ui.chkbxGroup)
        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def modifCliente(self):
        try:
            newData = []
            client = [var.ui.lineEdit, var.ui.lineEdit_2, var.ui.lineEdit_3,  var.ui.lineEdit_5, var.ui.lineEdit_4]
            for i in client:
                newData.append(i.text())
            newData.append(var.ui.selProv.currentText())
            newData.append(var.sex)
            var.pay = events.Eventos.selPago(self)
            print(var.pay)
            newData.append(var.pay)
            cod = var.ui.lblCodCli.text()
            conexion.Conexion.modifCli(cod, newData)
            conexion.Conexion.mostrarCli(self)

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))