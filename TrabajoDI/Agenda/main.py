
"""Proporciona la app."""

import sys
from PyQt5.QtWidgets import QApplication
from .baseDatos import crearConexion
from .vistas import Window

def main():
    """Crea la aplicación."""
    app = QApplication(sys.argv)
    """Conectarse a la base de datos antes de crear la ventana."""
    if not crearConexion("contactos.sqlite"):
        sys.exit(1)
    """Crea la ventana principal."""
    win = Window()
    win.show()
    sys.exit(app.exec())