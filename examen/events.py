import sys
import var

class Eventos():

    def salir(self):
            try:
                var.dlgsalir.show()
                if var.dlgsalir.exec():
                    sys.exit()
                else:
                    var.dlgsalir.hide()
            except Exception as error:
                print("Error %s: " %str(error))

    def movimiento(self):
            try:
                newValue = ''
                if var.ui.rbtRet.isChecked():
                    var.saldo -= float(var.ui.lineEditCant.text())
                    newValue = str(var.saldo)
                    var.ui.lineEditSaldo.setText(newValue)
                elif var.ui.rbtIng.isChecked():
                    var.saldo += float(var.ui.lineEditCant.text())
                    newValue = str(var.saldo)
                    var.ui.lineEditSaldo.setText(newValue)
            except Exception as error:
                print("Error %s: " %str(error))