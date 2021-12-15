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
            var.pay = []
            for i, data in enumerate(var.ui.chkbxGroup.buttons()):
                if data.isChecked() and i == 0:
                    var.pay.append('Efectivo')
                if data.isChecked() and i == 1:
                    var.pay.append('Tarjeta')
                if data.isChecked() and i == 2:
                    var.pay.append('Transferencia')
            print(var.pay)
            return var.pay
        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            var.vpro = prov
            print('Has seleccionado la provincia de ', prov)
        except Exception as error:
            print('Error: %s' % str(error))