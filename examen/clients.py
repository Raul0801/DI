import var
import datetime

class Clients():

    def validarDNI():
        try:
            dni = var.ui.lineEditDni.text()
            var.ui.lineEditDni.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.labelValDni.setStyleSheet('QLabel {color:green;}')
                    var.ui.labelValDni.setText('V')
                else:
                    var.ui.labelValDni.setStyleSheet('QLabel {color:red;}')
                    var.ui.labelValDni.setText('X')
            else:
                var.ui.labelValDni.setStyleSheet('QLabel {color:red;}')
                var.ui.labelValDni.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def abrirCalendar():
        try:
            var.dlgCalendar.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data =('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lineEditFecha.setText(str(data))
            var.dlgCalendar.hide
            chosenDate = datetime.datetime(qDate.year(), qDate.month(), qDate.day())
            if Clients.calcularEdad(chosenDate) < 18:
                var.ui.lineEditFecha.setText('')
                var.dlgWarning.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def calcularEdad(chosenDate):
        today = datetime.date.today()
        years = today.year - chosenDate.year
        if today.month < chosenDate.month or (today.month == chosenDate.month and today.day < chosenDate.day):
            years -= 1
        return years