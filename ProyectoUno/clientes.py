from PyQt5.QtGui import QFont

import var
from dni import Dni

class Clientes:

    def validarDNI():
        try:
            dni=var.ui.leDNI.text()
            var.ui.leDNI.setText(dni.upper())

            if (len(dni) == 9):
                numero = ""
                i = 0
                while (i < 8):
                    numero = numero + dni[i]
                    i += 1
                letra = dni[8]
                letra=letra.upper()
                dniCorrecto = Dni(numero)
                if (dniCorrecto.letra == letra):
                    print("DNI CORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('V')


                else:
                    print("DNI INCORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('X')

            else:
                print("DNI INCORRECTO")
                var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.lblValidarDNI.setFont(QFont("Forte"))
                var.ui.lblValidarDNI.setText('X')


        except Exception as error:
            print("Error %s: " % str(error))


    def selSexo(self):
        try:
            if var.ui.rbMujer.isChecked():
                print('marcado muller')
            if var.ui.rbHombre.isChecked():
                print('marcado home')
        except Exception as error:
            print('Error en módulo seleccionar sexo:',error)

    def selPago(self):
        try:
            if var.ui.cbEfectivo.isChecked():
                print('pagas con efectivo')
            if var.ui.cbTarjeta.isChecked():
                print('pagas con tajeta')
            if var.ui.cbTransferencia.isChecked():
                print('pagas con transferencia')
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarPovincia():
        try:
            prov=['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.comBoxProvincia.addItem(i)
        except Exception as error:
            print('Error: %s'% str(error))

    def seleccionarProvincia(prov):
        try:
            print('Has seleccionado la provincia de ',prov)
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    def abrirCalendario(self):
        try:
            var.dlgCalendario.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.dlgCalendario.hide()
        except Exception as error:
            print('Error: %' % str(error))