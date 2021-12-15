from PyQt5 import QtSql
from PyQt5 import QtWidgets

import var


class Conexion() :
    def db_connect(file):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(file)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión.\n' 'Haz click para cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida.')
            return True

    def cargarCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes(dni, apellidos, nombre, fechalta,direccion, provincia, sexo, formaspago)'
                      'VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formaspago)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        query.bindValue(':formaspago', str(cliente[7]))

        if query.exec_():
            print("Inserción correcta")
            Conexion.mostrarCli()
        else:
            print("Error: ", query.lastError().text())

    def mostrarCli(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tableWidget.setRowCount(index+1)
                var.ui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def bajaCli(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblStatus.setText('Cliente con dni ' + dni + ' dado de baja')
        else:
            print("Error mostrar clientes: ", query.lastError().text())
    def modifCli(codigo, newData):
        query = QtSql.QSqlQuery()
        codigo = int(codigo)
        query.prepare('update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, fechalta=:fechalta, '
                      'direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago where codigo=:codigo')
        query.bindValue(':codigo', int(codigo))
        query.bindValue(':dni', str(newData[0]))
        query.bindValue(':apellidos', str(newData[1]))
        query.bindValue(':nombre', str(newData[2]))
        query.bindValue(':fechalta', str(newData[3]))
        query.bindValue(':direccion', str(newData[4]))
        query.bindValue(':provincia', str(newData[5]))
        query.bindValue(':sexo', str(newData[6]))
        query.bindValue(':formaspago', str(newData[7]))
        if query.exec_():
            print('Cliente modificado')
            var.ui.lblStatus.setText('Cliente con dni ' + str(newData[0]) + ' modificado')
        else:
            print("Error modificar cliente: ", query.lastError().text())