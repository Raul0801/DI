
"""Proporciona la conexión a la base de datos."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def crearConexion(nombreDb):
    """Crea y abre una conexión a base de datos."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(nombreDb)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Agenda",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    crearTablaContactos()
    return True

def crearTablaContactos():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            ocupacion VARCHAR(255),
            email VARCHAR(255) NOT NULL
        )
        """
    )
