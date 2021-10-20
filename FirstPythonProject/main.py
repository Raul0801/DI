from ventana import *
import sys
import var
import events

class Main(QtWidgets.QMainWindow):
        def __init__(self):
            super(Main, self).__init__()
            var.ui = Ui_MainWindow()
            var.ui.setupUi(self)

            var.ui.pushButton.clicked.connect(events.Eventos.Saludo)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())