from PyQt6 import QtWidgets
from src.Servidor.DataBase import DataBase
from src.Cliente.ClienteVenta import ClienteVenta
from src.Cliente.ClienteCompra import ClienteCompra
from src.Cliente.ClienteListar import ClienteListar
from src.Assets.Ui_Supermercado import Ui_Supermercado
from src.Cliente.ClienteReportes import ClienteReportes
from src.Cliente.ClienteSucursal import ClienteSucursal
from src.Servidor.ServidorSucursal import ServidorSucursal
from src.Servidor.ServidorInventario import ServidorInventario
from src.Cliente.ClienteInformacionSupermercado import ClienteInformacionSupermercado

class Supermercado(QtWidgets.QMainWindow, Ui_Supermercado):
    def __init__(self, parent = None):
        super(Supermercado, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_sucursal = ServidorSucursal(self.db)
        self.servidor_inventario = ServidorInventario(self.db)
        self.init_actions()


    def init_actions(self):
        self.jmbSalir.triggered.connect(self.close)
        self.jmbListar.triggered.connect(lambda : self.init_cliente('listar')())
        self.jmbConfiguracion.triggered.connect(lambda : self.init_cliente('configuracion')())

        self.jmbIngresarSucursal.triggered.connect(lambda : self.init_cliente('sucursal')(0))
        self.jmbModificarSucursal.triggered.connect(lambda : self.init_cliente('sucursal')(1) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbEliminarSucursal.triggered.connect(lambda : self.init_cliente('sucursal')(2) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbListarSucursal.triggered.connect(lambda : self.init_cliente('sucursal')(3) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))

        self.jmbVender.triggered.connect(lambda : self.init_cliente('venta')() if self.servidor_inventario.obtener_inventarios() else self.dialogo_informacion('Informacion', 'No se tiene inventario'))
        self.jmbComprar.triggered.connect(lambda : self.init_cliente('compra')() if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))

        self.jmbBalance.triggered.connect(lambda : self.init_cliente('reportes')(3) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbProductoMasDemanda.triggered.connect(lambda : self.init_cliente('reportes')(1) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbProductoMenosDemanda.triggered.connect(lambda : self.init_cliente('reportes')(2) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbClientesMasFrecuentes.triggered.connect(lambda : self.init_cliente('reportes')(5) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))
        self.jmbProductosMayorCantidadInventario.triggered.connect(lambda : self.init_cliente('reportes')(4) if self.servidor_sucursal.obtener_sucursales() else self.dialogo_informacion('Informacion', 'No se han ingresado sucursales'))


    def init_cliente(self, cliente):

        def compra():
            self.cliente = ClienteCompra()
            self.cliente.show()
        def configuracion():
            self.cliente = ClienteInformacionSupermercado()
            self.cliente.show()
        def sucursal(indice):
            self.cliente = ClienteSucursal(indice)
            self.cliente.show()

        def venta():
            self.cliente = ClienteVenta()
            self.cliente.show()

        def listar():
            self.cliente = ClienteListar()
            self.cliente.show()

        def reportes(seccion):
            self.cliente = ClienteReportes(seccion)
            self.cliente.show()


        clientes = {'compra': compra, 'configuracion': configuracion, 'sucursal': sucursal, 'venta': venta,
                    'listar': listar, 'reportes': reportes}

        return clientes[cliente]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

