from PyQt6 import QtWidgets
from src.Servidor.ServidorCiudad import ServidorCiudad
from src.Servidor.DataBase import DataBase
from src.Servidor.ServidorProvincia import ServidorProvincia
from src.Servidor.ServidorInformacionSupermercado import ServidorInformacionSupermercado
from src.Assets.Ui_InformacionSupermercado import Ui_InformacionSupermercado

class ClienteInformacionSupermercado(QtWidgets.QWidget, Ui_InformacionSupermercado):
    def __init__(self, parent = None):
        super(ClienteInformacionSupermercado, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_ciudad = ServidorCiudad(self.db)
        self.servidor_provincia = ServidorProvincia(self.db)
        self.servidor_supermercado = ServidorInformacionSupermercado(self.db)

        self.init_window()
        self.init_actions()

    def init_actions(self):
        self.btnAtras.clicked.connect(self.cerrar)
        self.cmbProvincia.currentIndexChanged.connect(self.init_ciudades)
        self.btnGuardarCambios.clicked.connect(self.modficar_supermercado if self.txtRuc.text() else self.insertar_supermercado)

    def init_window(self):

        if self.servidor_provincia.obtener_provincias():
            self.init_provincias()
            self.init_ciudades()

        if self.servidor_supermercado.obtener_informacion():
            informacion = self.servidor_supermercado.obtener_informacion()[0]

            self.txtRuc.setEnabled(False)
            self.txtRuc.setText(informacion[0])
            self.txtRazonSocial.setText(informacion[1])
            self.cmbCiudad.setCurrentText(informacion[2])
            self.cmbProvincia.setCurrentText(self.servidor_ciudad.obtener_provincia(informacion[2])[0][0])

    def init_provincias(self):
        self.cmbProvincia.addItems([provincia[0] for provincia in self.servidor_provincia.obtener_provincias()])

    def init_ciudades(self):
        self.cmbCiudad.blockSignals(True)
        self.cmbCiudad.clear()
        self.cmbCiudad.addItems([ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText())])
        self.cmbCiudad.blockSignals(False)

    def insertar_ciudad(self):
        self.servidor_ciudad.insertar_ciudad(self.cmbCiudad.currentText(), self.cmbProvincia.currentText())

    def insertar_provincia(self):
        self.servidor_provincia.insertar_provincia(self.cmbProvincia.currentText())

    def modficar_supermercado(self):
        if self.txtRazonSocial.text() and self.cmbProvincia.currentText() and self.cmbCiudad.currentText():
            try:
                if not self.servidor_provincia.obtener_provincias() or self.cmbProvincia.currentText() not in [provincia[0] for provincia in self.servidor_provincia.obtener_provincias()]: self.insertar_provincia()
                if not self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText()) or self.cmbCiudad.currentText() not in [ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText())]: self.insertar_ciudad()

                self.servidor_supermercado.modificar_informacion(self.txtRuc.text(), self.txtRazonSocial.text(), self.cmbCiudad.currentText())
                self.dialogo_informacion('Exito', 'Cambios guardados')
            except Exception as e:
                print(e)

        else:
            self.dialogo_informacion('Error', 'Ingresar todos los campos')

    def insertar_supermercado(self):
        if self.txtRuc.text() and self.txtRazonSocial.text() and self.cmbProvincia.currentText() and self.cmbCiudad.currentText():
            try:
                if not self.servidor_provincia.obtener_provincias() or self.cmbProvincia.currentText() not in [provincia[0] for provincia in self.servidor_provincia.obtener_provincias()]: self.insertar_provincia()
                if not self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText()) or self.cmbCiudad.currentText() not in [ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText())]: self.insertar_ciudad()

                self.servidor_supermercado.insertar_informacion(self.txtRuc.text(), self.txtRazonSocial.text(), self.cmbCiudad.currentText())
                self.dialogo_informacion('Exito', 'Ingreso exitoso')
            except Exception as e:
                print(e)

        else:
            self.dialogo_informacion('Error', 'Ingresar todos los campos')

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def cerrar(self):
        self.close()


