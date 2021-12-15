from datetime import datetime
import conexion
from ventana import *
from windowaviso import *
from venCalendar import *
import sys
import var
import events
import Clientes

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgCalendar = Ui_DialogCal()
        var.dlgCalendar.setupUi(self)
        diaActual = datetime.now().day
        mesActual = datetime.now().month
        anoActual = datetime.now().year
        var.dlgCalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoActual, mesActual, diaActual)))
        var.dlgCalendar.calendarWidget.clicked.connect(Clientes.Clientes.cargarFecha)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.buttonBox.accepted.connect(self.accept)
        var.dlgsalir.buttonBox.rejected.connect(self.reject)

class Main(QtWidgets.QMainWindow):
        def __init__(self):
            super(Main, self).__init__()
            var.ui = Ui_MainWindow()
            var.ui.setupUi(self)
            var.dlgCalendar = DialogCalendar()
            var.dlgsalir = DialogSalir()
            var.ui.pushButton.clicked.connect(Clientes.Clientes.altaClientes)
            var.ui.pushButton_2.clicked.connect(Clientes.Clientes.bajaCliente)
            var.ui.lineEdit.editingFinished.connect(Clientes.Clientes.validarDNI)
            var.ui.rbtnGroup = (var.ui.rbtFem, var.ui.rbtMasc)
            var.ui.pushButton_3.clicked.connect(Clientes.Clientes.abrirCalendar)
            for i in var.ui.rbtnGroup:
                i.toggled.connect(events.Eventos.selSexo)
            var.ui.chkbxGroup = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)
            for i in var.ui.chkbxGroup:
                i.stateChanged.connect(events.Eventos.selPago)

            Clientes.Clientes.cargarProv()
            var.ui.selProv.activated[str].connect(events.Eventos.selProv)
            var.ui.tableWidget.clicked.connect(Clientes.Clientes.cargarCliente)
            var.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            conexion.Conexion.db_connect(var.fileBd)
            conexion.Conexion.mostrarCli(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())


