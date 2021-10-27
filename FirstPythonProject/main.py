from ventana import *
from windowaviso import *
import sys
import var
import events
import Clientes

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
            var.ui.pushButton.clicked.connect(events.Eventos.saludo)
            var.ui.pushButton_2.clicked.connect(events.Eventos.salir)
            var.ui.lineEdit.editingFinished.connect(Clientes.Clientes.validarDNI)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())


