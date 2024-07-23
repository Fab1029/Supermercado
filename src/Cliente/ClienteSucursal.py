from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QTableWidgetItem
from src.Assets.Ui_Sucursal import Ui_Sucursal
from src.Servidor.DataBase import DataBase
from src.Servidor.ServidorCiudad import ServidorCiudad
from src.Servidor.ServidorSucursal import ServidorSucursal
from src.Servidor.ServidorProvincia import ServidorProvincia
from src.Servidor.ServidorInformacionSupermercado import ServidorInformacionSupermercado

class ClienteSucursal(QtWidgets.QWidget, Ui_Sucursal):
    def __init__(self, seccion, parent = None):
        super(ClienteSucursal, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_ciudad = ServidorCiudad(self.db)
        self.servidor_sucursal = ServidorSucursal(self.db)
        self.servidor_provincia = ServidorProvincia(self.db)

        self.verificar_pestana()
        self.init_actions()
        self.init_seccion(seccion)()

    def init_actions(self):
        self.cmbNombreModificar.currentIndexChanged.connect(self.nombre_action)
        self.cmbProvinciaIngresar.currentIndexChanged.connect(lambda : self.provincia_action(1)())
        self.cmbProvinciaModificar.currentIndexChanged.connect(lambda : self.provincia_action(2)())

        self.btnAtras.clicked.connect(self.cerrar)
        self.btnGuardarCambios.clicked.connect(self.modificar_sucursal_action)
        self.btnEliminarSucursal.clicked.connect(self.eliminar_sucursal_action)
        self.btnIngresarSucursal.clicked.connect(self.ingresar_sucursal_action)

        self.tbSucursal.currentChanged.connect(lambda : self.init_seccion(self.tbSucursal.currentIndex())())

    def ingresar_sucursal_action(self):
        if self.txtNombreIngresar.text() and self.txtDireccionIngresar.text() and self.txtTelefonoIngresar.text() and self.cmbProvinciaIngresar.currentText() and self.cmbCiudadIngresar.currentText():
            try:
                if self.cmbProvinciaIngresar.currentText() not in [provincia[0] for provincia in self.servidor_provincia.obtener_provincias()]: self.servidor_provincia.insertar_provincia(self.cmbProvinciaIngresar.currentText())
                if self.cmbCiudadIngresar.currentText() not in [ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvinciaIngresar.currentText())]: self.servidor_ciudad.insertar_ciudad(self.cmbCiudadIngresar.currentText(), self.cmbProvinciaIngresar.currentText())

                self.servidor_sucursal.insertar_sucursal(self.txtNombreIngresar.text(), self.txtDireccionIngresar.text(), self.txtTelefonoIngresar.text(), self.cmbCiudadIngresar.currentText(), ServidorInformacionSupermercado(self.db).obtener_informacion()[0][0])
                self.verificar_pestana()
                self.init_seccion(0)()
                self.dialogo_informacion('Éxito', 'Ingreso exitoso')
            except Exception as e:
                print(e)
        else:
            self.dialogo_informacion('Alerta', 'Ingresar todos los campos')

    def modificar_sucursal_action(self):
        if self.txtDireccionModificar.text() and self.txtTelefonoModificar.text() and self.cmbProvinciaModificar.currentText() and self.cmbCiudadModificar.currentText():
            try:
                if self.cmbProvinciaModificar.currentText() not in [provincia[0] for provincia in self.servidor_provincia.obtener_provincias()]: self.servidor_provincia.insertar_provincia(self.cmbProvinciaModificar.currentText())
                if self.cmbCiudadModificar.currentText() not in [ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvinciaModificar.currentText())]: self.servidor_ciudad.insertar_ciudad(self.cmbCiudadModificar.currentText(), self.cmbProvinciaModificar.currentText())
                self.servidor_sucursal.modificar_sucursal(self.cmbNombreModificar.currentText(), self.txtDireccionModificar.text(), self.txtTelefonoModificar.text(), self.cmbCiudadModificar.currentText())

                self.init_seccion(1)()
                self.dialogo_informacion('Éxito', 'Cambios guardados')
            except Exception as e:
                print(e)
        else:
            self.dialogo_informacion('Alerta', 'Ingresar todos los campos')


    def eliminar_sucursal_action(self):
        try:
            self.servidor_sucursal.eliminar_sucursal(self.cmbNombreEliminar.currentText())
            self.verificar_pestana()
            self.init_seccion(2)()
            self.dialogo_informacion('Éxito', 'Sucursal eliminada')
        except Exception as e:
            print(e)

    def listar_sucursales_action(self):
        try:
            count = 0
            self.twSucursales.clear()
            self.twSucursales.setColumnCount(4)
            self.twSucursales.setRowCount(len(self.servidor_sucursal.obtener_sucursales()))
            self.twSucursales.setHorizontalHeaderLabels(['Nombre', 'Direccion', 'Telefono', 'Ciudad'])
            for nombre, direccion, telefono, ciudad, _ in self.servidor_sucursal.obtener_sucursales():
                self.twSucursales.setItem(count, 0, QTableWidgetItem(nombre))
                self.twSucursales.setItem(count, 1, QTableWidgetItem(direccion))
                self.twSucursales.setItem(count, 2, QTableWidgetItem(telefono))
                self.twSucursales.setItem(count, 3, QTableWidgetItem(ciudad))
                count += 1
        except Exception as e:
            print(e)
    def provincia_action(self, accion):
        def ingresar():
            self.cmbCiudadIngresar.blockSignals(True)
            self.cmbCiudadIngresar.clear()
            self.cmbCiudadIngresar.addItems([ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvinciaIngresar.currentText())])
            self.cmbCiudadIngresar.blockSignals(False)

        def modificar():
            self.cmbCiudadModificar.blockSignals(True)
            self.cmbCiudadModificar.clear()
            self.cmbCiudadModificar.addItems([ciudad[0] for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvinciaModificar.currentText())])
            self.cmbCiudadModificar.blockSignals(False)

        action = {1: ingresar, 2: modificar}

        return action[accion]

    def nombre_action(self):
        try:
            informacion = self.servidor_sucursal.obtener_sucursal(self.cmbNombreModificar.currentText())[0]

            self.txtDireccionModificar.setText(informacion[1])
            self.txtTelefonoModificar.setText(informacion[2])
            self.cmbProvinciaModificar.setCurrentText(self.servidor_ciudad.obtener_provincia(informacion[3])[0][0])
            self.provincia_action(2)()
            self.cmbCiudadModificar.setCurrentText(informacion[3])
        except:
            pass

    def init_seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbSucursal.setCurrentIndex(0)
            self.txtNombreIngresar.clear()
            self.cmbCiudadIngresar.clear()
            self.txtTelefonoIngresar.clear()
            self.txtDireccionIngresar.clear()
            self.cmbProvinciaIngresar.clear()
            self.txtTelefonoIngresar.setValidator(QIntValidator())
            self.cmbProvinciaIngresar.addItems([provincia[0] for provincia in self.servidor_provincia.obtener_provincias()])
            self.provincia_action(1)()

            self.conectar_conexion()

        def modificar():
            self.tbSucursal.setCurrentIndex(1)
            self.cmbNombreModificar.clear()
            self.cmbCiudadModificar.clear()
            self.txtTelefonoModificar.clear()
            self.cmbProvinciaModificar.clear()
            self.txtDireccionModificar.clear()
            self.txtTelefonoModificar.setValidator(QIntValidator())
            self.cmbProvinciaModificar.addItems([provincia[0] for provincia in self.servidor_provincia.obtener_provincias()])
            self.cmbNombreModificar.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])
            self.nombre_action()

            self.conectar_conexion()

        def eliminar():
            self.tbSucursal.setCurrentIndex(2)
            self.cmbNombreEliminar.clear()
            self.cmbNombreEliminar.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])

        def listar():
            self.tbSucursal.setCurrentIndex(3)
            self.listar_sucursales_action()

        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def desconectar_conexion(self):
        try:
            self.cmbNombreModificar.blockSignals(True)
            self.cmbProvinciaIngresar.blockSignals(True)
            self.cmbProvinciaModificar.blockSignals(True)
        except Exception as e:
            print(e)
    def conectar_conexion(self):
        try:
            self.cmbNombreModificar.blockSignals(False)
            self.cmbProvinciaIngresar.blockSignals(False)
            self.cmbProvinciaModificar.blockSignals(False)
        except Exception as e:
            print(e)

    def verificar_pestana(self):
        if self.servidor_sucursal.obtener_sucursales():
            [self.tbSucursal.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbSucursal.setCurrentIndex(0)
            [self.tbSucursal.setTabEnabled(indice, False) for indice in range(1,4)]

    def cerrar(self):
        self.close()


