from ventana import *
from windowaviso import *
import sys
import var

class Eventos():

    def saludo(self):
        try:
            var.ui.label.setText('Aceptar pulsado')
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