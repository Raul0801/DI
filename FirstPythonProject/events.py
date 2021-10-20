import var

class Eventos():

    def Saludo():
        try:
            var.ui.label.setText('Aceptar pulsado')
        except Exception as error:
            print('Error: %s' % str(error))