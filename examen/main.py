from datetime import datetime

import clients
import sys
import var
import events
from ventana import *
from windowaviso import *
from windowavisomenoredad import *
from venCalendar import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.dlgCalendar = DialogCalendar()
        var.dlgsalir = DialogSalir()
        var.dlgWarning = DialogWarning()
        var.ui.pushButtonAc.clicked.connect(events.Eventos.movimiento)
        var.ui.pushButtonSal.clicked.connect(events.Eventos.salir)
        var.ui.lineEditDni.editingFinished.connect(clients.Clients.validarDNI)
        var.ui.buttonGroupRetIn = (var.ui.rbtRet, var.ui.rbtIng)
        var.ui.pushButtonCalendar.clicked.connect(clients.Clients.abrirCalendar)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgCalendar = Ui_DialogCal()
        var.dlgCalendar.setupUi(self)
        diaActual = datetime.now().day
        mesActual = datetime.now().month
        anoActual = datetime.now().year
        var.dlgCalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoActual, mesActual, diaActual)))
        var.dlgCalendar.calendarWidget.clicked.connect(clients.Clients.cargarFecha)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.buttonBox.accepted.connect(self.accept)
        var.dlgsalir.buttonBox.rejected.connect(self.reject)

class DialogWarning(QtWidgets.QDialog):
    def __init__(self):
        super(DialogWarning, self).__init__()
        var.dlgWarning = Ui_DialogWarning()
        var.dlgWarning.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())