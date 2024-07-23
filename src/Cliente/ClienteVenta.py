import uuid
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator
from PyQt6.QtGui import QDoubleValidator
from src.Assets.Ui_Venta import Ui_Venta
from src.Servidor.DataBase import DataBase
from PyQt6.QtWidgets import QTableWidgetItem
from src.Servidor.ServidorVenta import ServidorVenta
from src.Servidor.ServidorCliente import ServidorCliente
from src.Servidor.ServidorSucursal import ServidorSucursal
from src.Servidor.ServidorInventario import ServidorInventario

class ClienteVenta(QtWidgets.QWidget, Ui_Venta):
    def __init__(self, parent = None):
        super(ClienteVenta, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_venta = ServidorVenta(self.db)
        self.servidor_cliente = ServidorCliente(self.db)
        self.servidor_sucursal = ServidorSucursal(self.db)
        self.servidor_inventario = ServidorInventario(self.db)

        self.init_window()
        self.init_actions()

    def init_actions(self):
        self.btnAtras.clicked.connect(self.cerrar)
        self.btnIngresarVenta.clicked.connect(self.ingresar_venta_action)
        self.btnIngresarProducto.clicked.connect(self.ingresar_producto_action)
        self.cmbNombreProducto.currentIndexChanged.connect(self.producto_action)
        self.cbTarjeta.checkStateChanged.connect(lambda : self.txtDescuento.setEnabled(self.cbTarjeta.isChecked()))
        self.txtCedula.textEdited.connect(lambda : self.cliente_action() if len(self.txtCedula.text()) == 10 else None)

    #Ya esta verificada
    def init_window(self):
        self.init_seccion_informacion_general()
        self.init_seccion_producto()
        self.txtDescuento.setText('0')
        #Set validadores

        self.txtCedula.setValidator(QIntValidator())
        self.txtTelefono.setValidator(QIntValidator())
        self.txtCantidad.setValidator(QIntValidator())
        self.txtDescuento.setValidator(QDoubleValidator())
        self.txtPrecioVenta.setValidator(QDoubleValidator())

    #Ya esta verificada
    def generar_codigo(self):
        try:
            codigo = str(uuid.uuid4())

            while codigo in [venta[0] for venta in self.servidor_venta.obtener_ventas()]:
                codigo = str(uuid.uuid4())
            return codigo
        except Exception as e:
            print(e)

    #Ya esta verificada
    def init_seccion_informacion_general(self):
        self.cmbSucursal.clear()
        self.cmbSucursal.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])
        self.txtCodigo.setText(self.generar_codigo())
        self.dtpFecha.setDate(QDate.currentDate())

    #Ya esta verificada
    def init_seccion_producto(self):
        self.cmbNombreProducto.blockSignals(True)
        self.cmbNombreProducto.clear()

        self.cmbNombreProducto.addItems([inventario[1] for inventario in self.servidor_inventario.obtener_inventario_de_sucursal(self.cmbSucursal.currentText()) if inventario[2] > 0])

        self.producto_action()
        self.cmbNombreProducto.blockSignals(False)

    #Esta debo realizar
    def init_detalle_venta(self):
        try:
            count = 0
            self.twVenta.clear()
            self.twVenta.setColumnCount(4)
            self.twVenta.setRowCount(len(self.servidor_venta.obtener_productos_de_venta(self.txtCodigo.text())))
            self.twVenta.setHorizontalHeaderLabels(['#Venta', 'Producto', 'Cantidad', 'Precio venta'])

            for venta, producto, cantidad, precio_venta in self.servidor_venta.obtener_productos_de_venta(self.txtCodigo.text()):
                self.twVenta.setItem(count, 0, QTableWidgetItem(venta))
                self.twVenta.setItem(count, 1, QTableWidgetItem(producto))
                self.twVenta.setItem(count, 2, QTableWidgetItem(str(cantidad)))
                self.twVenta.setItem(count, 3, QTableWidgetItem(str(precio_venta)))

                count += 1

            self.txtTotal.setText(str(self.servidor_venta.total_venta(self.txtCodigo.text())[0][0]))
        except Exception as e:
            print(e)

    #Ya esta verificada
    def agregar_cliente(self):
        if not self.servidor_cliente.obtener_cliente(self.txtCedula.text()):
            self.servidor_cliente.insertar_cliente(self.txtCedula.text(), self.txtNombreCliente.text(), self.txtTelefono.text(), self.txtCorreo.text(), self.cbTarjeta.isChecked())

    #Ya esta verificada
    def agregar_a_venta_producto(self):
        if self.servidor_venta.obtener_venta_producto(self.txtCodigo.text(), self.cmbNombreProducto.currentText()):
            self.servidor_venta.modificar_venta_producto(self.txtCodigo.text(), self.cmbNombreProducto.currentText(), int(self.txtCantidad.text()), float(self.txtPrecioVenta.text()))
        else:
            self.servidor_venta.insertar_venta_producto(self.txtCodigo.text(), self.cmbNombreProducto.currentText(), int(self.txtCantidad.text()), float(self.txtPrecioVenta.text()))

    #Ya esta verifcada
    def modificar_inventario(self):
        if self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombreProducto.currentText()):
            informacion = self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombreProducto.currentText())[0]
            self.servidor_inventario.modificar_inventario(self.cmbSucursal.currentText(), self.cmbNombreProducto.currentText(), informacion[2] - int(self.txtCantidad.text()), float(self.txtPrecioVenta.text()))

    #Ya esta verificada
    def agregar_venta(self):
        if not self.servidor_venta.obtener_venta(self.txtCodigo.text()):
            self.servidor_venta.insertar_venta(self.txtCodigo.text(), self.dtpFecha.date().toString('yyyy-MM-dd'), self.txtCedula.text(), self.cmbSucursal.currentText(), float(self.txtDescuento.text()))


    def ingresar_venta_action(self):
        self.dtpFecha.setEnabled(True)
        self.txtCorreo.setEnabled(True)
        self.cbTarjeta.setEnabled(True)
        self.txtCedula.setEnabled(True)
        self.cmbSucursal.setEnabled(True)
        self.txtTelefono.setEnabled(True)
        self.txtNombreCliente.setEnabled(True)

        self.txtTotal.clear()
        self.txtCorreo.clear()
        self.txtCedula.clear()
        self.txtCantidad.clear()
        self.txtTelefono.clear()
        self.txtNombreCliente.clear()
        self.txtDescuento.setText('0')
        self.cbTarjeta.setChecked(False)

        self.twVenta.setRowCount(0)
        self.twVenta.setColumnCount(0)

        self.init_seccion_informacion_general()
        self.init_seccion_producto()

    def ingresar_producto_action(self):
        try:
            if not(self.txtCedula.text() and self.txtNombreCliente.text() and self.txtTelefono.text() and self.txtCorreo.text()):
                self.dialogo_informacion('Error', 'Ingresar campos de cliente')
                return
            if not(self.txtCantidad.text() and self.txtPrecioVenta.text() and int(self.txtCantidad.text()) <= self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombreProducto.currentText())[0][2]):
                self.dialogo_informacion('Error', 'Ingresar campos de producto')
                return

            #Se agrega toda la informacion a los servidores
            self.agregar_cliente()

            self.agregar_venta()
            self.agregar_a_venta_producto()
            self.modificar_inventario()

            self.dtpFecha.setEnabled(False)
            self.txtCedula.setEnabled(False)
            self.txtCorreo.setEnabled(False)
            self.cbTarjeta.setEnabled(False)
            self.txtTelefono.setEnabled(False)
            self.cmbSucursal.setEnabled(False)
            self.txtDescuento.setEnabled(False)
            self.txtNombreCliente.setEnabled(False)

            self.init_detalle_venta()
            self.init_seccion_producto()
            self.producto_action()

            self.dialogo_informacion('Exito', 'Se agrego producto exitosamente')

        except Exception as e:
            print(e)

    #Ya esta verificada
    def cliente_action(self):
        try:
            if self.servidor_cliente.obtener_cliente(self.txtCedula.text()):
                informacion = self.servidor_cliente.obtener_cliente(self.txtCedula.text())[0]

                self.txtNombreCliente.setText(informacion[1])
                self.txtTelefono.setText(informacion[2])
                self.txtCorreo.setText(informacion[3])
                self.cbTarjeta.setChecked(informacion[4])

        except Exception as e:
            print(e)


    #Ya esta verificada
    def producto_action(self):
        try:
            _,_,cantidad,precio_oficial = self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombreProducto.currentText())[0]
            self.txtPrecioVenta.setText(str(precio_oficial))
            self.txtCantidad.setPlaceholderText(f'Cantidad maxima {cantidad}')
        except Exception as e:
            print(e)

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def cerrar(self):
        self.close()
