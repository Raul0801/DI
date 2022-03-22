
"""Proporciona las vistas para manejar la tabla de contactos."""
from .informes import Printer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QAbstractItemView,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QMainWindow,
    QLineEdit,
    QMessageBox,
)
from .contactoModelo import Contacto

class Window(QMainWindow):
    """Ventana principal."""
    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Agenda")
        self.resize(700, 350)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.modeloContactos = Contacto()
        self.setupUI()

    def setupUI(self):
        """Hace el setup a la UI."""
        """Crea la table view."""
        self.tabla = QTableView()
        self.tabla.setModel(self.modeloContactos.model)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.resizeColumnsToContents()
        """Crea los botones."""
        self.botonAñadir = QPushButton("Añadir Contacto")
        self.botonAñadir.clicked.connect(self.abrirDialogo)
        self.botonBorrar = QPushButton("Borrar Contacto")
        self.botonBorrar.clicked.connect(self.borrarContacto)
        self.botonInforme = QPushButton("Generar Informe")
        self.botonInforme.clicked.connect(Printer.reportContactos)
        self.botonBorrarTodo = QPushButton("Borrar Todos")
        self.botonBorrarTodo.clicked.connect(self.borrarContactos)
        """Coloca el layout"""
        layout = QVBoxLayout()
        layout.addWidget(self.botonAñadir)
        layout.addWidget(self.botonBorrar)
        layout.addStretch()
        layout.addWidget(self.botonInforme)
        layout.addWidget(self.botonBorrarTodo)
        self.layout.addWidget(self.tabla)
        self.layout.addLayout(layout)

    def abrirDialogo(self):
        """Abre el diálogo para añadir contactos."""
        dialogo = DialogoDeAñadir(self)
        if dialogo.exec() == QDialog.Accepted:
            self.modeloContactos.añadirContacto(dialogo.data)
            self.tabla.resizeColumnsToContents()

    def borrarContacto(self):
        """Borra el contacto seleccionado."""
        row = self.tabla.currentIndex().row()
        if row < 0:
            return

        aviso = QMessageBox.warning(
            self,
            "Aviso!",
            "¿Quieres borrar el contacto seleccionado?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if aviso == QMessageBox.Ok:
            self.modeloContactos.borrarContacto(row)

    def borrarContactos(self):
        """Vacía la agenda."""
        aviso = QMessageBox.warning(
            self,
            "Aviso!",
            "¿Quieres vaciar la agenda?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if aviso == QMessageBox.Ok:
            self.modeloContactos.borrarContactos()

class DialogoDeAñadir(QDialog):
    """Ventana de diálogo para rellenar un contacto."""
    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent=parent)
        self.setWindowTitle("Añadir Contacto")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Hace el setup a la UI para el diálogo del contacto."""
        """Crea los line edit para rellenarlos."""
        self.campoNombre = QLineEdit()
        self.campoNombre.setObjectName("nombre")
        self.campoOcupacion = QLineEdit()
        self.campoOcupacion.setObjectName("ocupacion")
        self.campoEmail = QLineEdit()
        self.campoEmail.setObjectName("email")
        layout = QFormLayout()
        layout.addRow("Nombre:", self.campoNombre)
        layout.addRow("Ocupación:", self.campoOcupacion)
        layout.addRow("Email:", self.campoEmail)
        self.layout.addLayout(layout)
        """Añade los botones al diálogo y los conecta."""
        self.cajaDeBotones = QDialogButtonBox(self)
        self.cajaDeBotones.setOrientation(Qt.Horizontal)
        self.cajaDeBotones.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.cajaDeBotones.accepted.connect(self.aceptar)
        self.cajaDeBotones.rejected.connect(self.reject)
        self.layout.addWidget(self.cajaDeBotones)

    def aceptar(self):
        """Acepta la información introducida."""
        self.data = []
        for field in (self.campoNombre, self.campoOcupacion, self.campoEmail):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Debes rellenar el campo: {field.objectName()}",
                )
                self.data = None
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()