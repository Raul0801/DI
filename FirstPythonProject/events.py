from ventana import *
from windowaviso import *
import sys
import var

class Eventos():

    def saludo(self):
        try:
            print('Aceptar pulsado')
        except Exception as error:
            print('Error: %s' % str(error))

    def salir(self):
            try:
                var.dlgsalir.show()
                if var.dlgsalir.exec():
                    sys.exit()
                else:
                    var.dlgsalir.hide()
            except Exception as error:
                print("Error %s: " %str(error))

    def selSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Femenino marcado')
            if var.ui.rbtMasc.isChecked():
                print('Masculino marcado')
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago(self):
        try:
            if var.ui.chkEfec.isChecked():
                print('Pagas con efectivo')
            if var.ui.chkTarj.isChecked():
                print('Pagas con tarjeta')
            if var.ui.chkTrans.isChecked():
                print('Pagas con transferencia')
        except Exception as error:
            print('Error: %s' % str(error))