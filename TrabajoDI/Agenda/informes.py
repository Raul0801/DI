from datetime import datetime
from pathlib import Path
from PyQt5 import QtSql
from reportlab.pdfgen import canvas
import os


class Printer():

    def reportContactos():
        try:
            path = 'informes'
            exists = os.path.exists(path)
            if not exists:
                os.makedirs(path)

            file = Path('informes/listadoContactos.pdf')
            file.touch(exist_ok=True)
            open(file)

            c = canvas.Canvas('informes/listadoContactos.pdf')
            c.drawString(100, 750, 'Listado de Contactos')
            c.setTitle('INFORMES')
            c.setAuthor('Usuario')
            c.setFont('Helvetica', size= 10)
            c.line(45, 820, 525, 820)
            c.line(45, 745, 525, 745)
            c.drawString(50, 805, 'A0000000H')
            c.drawString(50, 790, 'Contactos de Usuario')

            itemContacto = ['ID', 'Nombre', 'Ocupacion', 'Email']
            c.drawString(45, 710, itemContacto[0])
            c.drawString(90, 710, itemContacto[1])
            c.drawString(180, 710, itemContacto[2])
            c.drawString(325, 710, itemContacto[3])
            c.line(45, 705, 525, 705)
            query = QtSql.QSqlQuery()
            query.prepare('select id, nombre, ocupacion, email from contactos order by id')
            c.setFont('Helvetica', size=11)

            if query.exec_():
                i = 50
                j = 690
                while query.next():
                    c.drawString(i,j,str(query.value(0)))
                    c.drawString(i+30, j, str(query.value(1)))
                    c.drawString(i+130, j, str(query.value(2)))
                    c.drawString(i+280, j, str(query.value(3)))
                    j = j-30

            c.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            c.setFont('Helvetica-Oblique', size=7)
            c.drawString(460, 40, str(fecha))
            c.drawString(275, 40, str('Página %s' % c.getPageNumber()))
            c.drawString(50,40, str('Listado de Contactos'))

            c.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reportContactos %s' % str(error))