from PyQt5 import QtSql
from PyQt5 import QtWidgets


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