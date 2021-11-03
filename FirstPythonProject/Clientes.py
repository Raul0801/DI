from ventana import *
import sys
import var
import events

class Clientes():

    def validarDNI():
        try:
            dni = var.ui.lineEdit.text()
            var.ui.lineEdit.setText(dni.upper())
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
                    var.ui.label_5.setStyleSheet('QLabel {color:green;}')
                    var.ui.label_5.setText('V')
                else:
                    var.ui.label_5.setStyleSheet('QLabel {color:red;}')
                    var.ui.label_5.setText('X')
            else:
                var.ui.label_5.setStyleSheet('QLabel {color:red;}')
                var.ui.label_5.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def cargarProv():
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.selProv.addItem(i)
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def seleccionarProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error: %s' % str(error))
