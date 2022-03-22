
"""Proporciona el modelo con el que rellenar la tabla."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class Contacto:
    def __init__(self):
        self.model = self._crearContacto()

    def añadirContacto(self, data):
        """Añade un contacto a la base de datos."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for columna, campo in enumerate(data):
            self.model.setData(self.model.index(rows, columna + 1), campo)
        self.model.submitAll()
        self.model.select()

    @staticmethod
    def _crearContacto():
        """Crea y le da sus atributos al modelo."""
        tableModel = QSqlTableModel()
        tableModel.setTable("contactos")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Nombre", "Ocupación", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def borrarContacto(self, row):
        """Borra un contacto seleccionado de la base de datos y vuelve a cargar los datos."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def borrarContactos(self):
        """Borra todos los contactos de la base de datos."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()