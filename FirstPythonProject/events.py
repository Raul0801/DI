from ventana import *
from windowaviso import *
import sys
import var

class Eventos():

    def saludo(self):
        try:
            print('Hola!')
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
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago(self):
        try:
            if var.ui.chkEfec.isChecked():
                print('Pagas con efectivo')
                var.pay.append('Efectivo')
            if var.ui.chkTarj.isChecked():
                print('Pagas con tarjeta')
                var.pay.append('Tarjeta')
            if var.ui.chkTrans.isChecked():
                print('Pagas con transferencia')
                var.pay.append('Transferencia')
        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            var.vpro = prov
            print('Has seleccionado la provincia de ', prov)
        except Exception as error:
            print('Error: %s' % str(error))