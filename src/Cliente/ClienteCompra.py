import uuid
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QTableWidgetItem
from src.Assets.Ui_Compra import Ui_Compra
from src.Servidor.DataBase import DataBase
from src.Servidor.ServidorMarca import ServidorMarca
from src.Servidor.ServidorCiudad import ServidorCiudad
from src.Servidor.ServidorCompra import ServidorCompra
from src.Servidor.ServidorSucursal import ServidorSucursal
from src.Servidor.ServidorProducto import ServidorProducto
from src.Servidor.ServidorProvincia import ServidorProvincia
from src.Servidor.ServidorCategoria import ServidorCategoria
from src.Servidor.ServidorProveedor import ServidorProveedor
from src.Servidor.ServidorInventario import ServidorInventario


class ClienteCompra(QtWidgets.QWidget, Ui_Compra):
    def __init__(self, parent = None):
        super(ClienteCompra, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()

        self.producto_categoria = set()
        self.servidor_marca = ServidorMarca(self.db)
        self.servidor_ciudad = ServidorCiudad(self.db)
        self.servidor_compra = ServidorCompra(self.db)
        self.servidor_producto = ServidorProducto(self.db)
        self.servidor_sucursal = ServidorSucursal(self.db)
        self.servidor_provincia = ServidorProvincia(self.db)
        self.servidor_categoria = ServidorCategoria(self.db)
        self.servidor_proveedor = ServidorProveedor(self.db)
        self.servidor_inventario = ServidorInventario(self.db)

        self.init_window()
        self.init_actions()

    def init_actions(self):
        self.btnAtras.clicked.connect(self.cerrar)
        self.btnAgregarCategoria.clicked.connect(self.categoria_action)
        self.cmbNombre.currentIndexChanged.connect(self.producto_action)
        self.btnLimpiarCampos.clicked.connect(self.limpiar_campos_action)
        self.btnIngresarCompra.clicked.connect(self.ingresar_compra_action)
        self.cmbProvincia.currentIndexChanged.connect(self.provincia_action)
        self.cmbNombre.currentTextChanged.connect(self.txtPrecioOficial.clear)
        self.btnIngresarProducto.clicked.connect(self.ingresar_producto_action)
        self.txtRuc.textEdited.connect(lambda : self.proveedor_action() if len(self.txtRuc.text()) == 13 else None)

    def init_window(self):
        self.init_seccion_informacion_general()
        self.init_seccion_producto()
        self.init_provincia()
        #Set validadores

        self.txtTelefono.setValidator(QIntValidator())
        self.txtCantidad.setValidator(QIntValidator())
        self.txtPrecioCompra.setValidator(QDoubleValidator())
        self.txtPrecioOficial.setValidator(QDoubleValidator())
        self.txtRuc.setValidator(QRegularExpressionValidator(QRegularExpression(r"^\d{13}$")))

    def init_provincia(self):
        self.cmbProvincia.blockSignals(True)
        self.cmbProvincia.clear()
        self.cmbProvincia.addItems([provincia[0] for provincia in self.servidor_provincia.obtener_provincias()])
        self.cmbProvincia.blockSignals(False)
        self.provincia_action()

    def generar_codigo(self):
        try:
            codigo = str(uuid.uuid4())

            while codigo in [compra[0] for compra in self.servidor_compra.obtener_compras()]:
                codigo = str(uuid.uuid4())
            return codigo
        except Exception as e:
            print(e)

    def init_seccion_informacion_general(self):
        self.cmbSucursal.clear()
        self.cmbSucursal.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])
        self.txtCodigo.setText(self.generar_codigo())
        self.dtpFecha.setDate(QDate.currentDate())

    def init_seccion_producto(self):
        self.cmbNombre.blockSignals(True)
        self.cmbMarca.clear()
        self.cmbNombre.clear()
        self.cmbCategorias.clear()
        self.cmbMarca.addItems([marca[0] for marca in self.servidor_marca.obtener_marcas()])
        self.cmbNombre.addItems([producto[0] for producto in self.servidor_producto.obtener_productos()])
        self.cmbCategorias.addItems([categoria[0] for categoria in self.servidor_categoria.obtener_categorias()])
        self.producto_action()
        self.cmbNombre.blockSignals(False)

    def init_detalle_compra(self):
        try:
            count = 0
            self.twCompra.clear()
            self.twCompra.setColumnCount(4)
            self.twCompra.setRowCount(len(self.servidor_compra.obtener_productos_de_compra(self.txtCodigo.text())))
            self.twCompra.setHorizontalHeaderLabels(['#Compra', 'Producto', 'Cantidad', 'Precio compra'])

            for compra, producto, cantidad, precio_compra in self.servidor_compra.obtener_productos_de_compra(self.txtCodigo.text()):
                self.twCompra.setItem(count, 0, QTableWidgetItem(compra))
                self.twCompra.setItem(count, 1, QTableWidgetItem(producto))
                self.twCompra.setItem(count, 2, QTableWidgetItem(str(cantidad)))
                self.twCompra.setItem(count, 3, QTableWidgetItem(str(precio_compra)))

                count += 1

            self.txtTotal.setText(str(self.servidor_compra.total_compra(self.txtCodigo.text())[0][0]))

        except Exception as e:
            print(e)

    def agregar_ciudad(self):
        if not self.servidor_ciudad.obtener_ciudad(self.cmbCiudad.currentText()):
            self.servidor_ciudad.insertar_ciudad(self.cmbCiudad.currentText(), self.cmbProvincia.currentText())

    def agregar_provincia(self):
        if not self.servidor_provincia.obtener_provincia(self.cmbProvincia.currentText()):
            self.servidor_provincia.insertar_provincia(self.cmbProvincia.currentText())


    def agregar_proveedor(self):
        if not self.servidor_proveedor.obtener_proveedor(self.txtRuc.text()):
            self.servidor_proveedor.insertar_proveedor(self.txtRuc.text(), self.txtRazonSocial.text(), self.txtTelefono.text())

        if not self.servidor_proveedor.obtener_proveedor_ciudad(self.cmbCiudad.currentText(), self.txtRuc.text()):
            self.servidor_proveedor.insertar_proveedor_ciudad(self.cmbCiudad.currentText(), self.txtRuc.text())

    def agregar_producto(self):
        if not self.servidor_producto.obtener_producto(self.cmbNombre.currentText()):
            self.servidor_producto.insertar_producto(self.cmbNombre.currentText(), self.cmbMarca.currentText())

    def agregar_marca(self):
        if not self.servidor_marca.obtener_marca(self.cmbMarca.currentText()):
            self.servidor_marca.insertar_marca(self.cmbMarca.currentText())

    def agregar_a_compra_producto(self):
        if self.servidor_compra.obtener_compra_producto(self.txtCodigo.text(), self.cmbNombre.currentText()):
            self.servidor_compra.modificar_compra_producto(self.txtCodigo.text(), self.cmbNombre.currentText(), int(self.txtCantidad.text()), float(self.txtPrecioCompra.text()))
        else:
            self.servidor_compra.insertar_compra_producto(self.txtCodigo.text(), self.cmbNombre.currentText(), int(self.txtCantidad.text()), float(self.txtPrecioCompra.text()))


    def agregar_a_producto_categoria(self):
        for categoria in self.producto_categoria:
            if not self.servidor_categoria.obtener_producto_categoria(self.cmbNombre.currentText(), categoria):
                self.servidor_categoria.insertar_producto_categoria(self.cmbNombre.currentText(), categoria)

    def agregar_inventario(self):
        if self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText()):
            informacion = self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText())[0]
            self.servidor_inventario.modificar_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText(), informacion[2] + int(self.txtCantidad.text()), float(self.txtPrecioOficial.text()))
        else:
            self.servidor_inventario.insertar_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText(), int(self.txtCantidad.text()), float(self.txtPrecioOficial.text()))

    def agregar_compra(self):
        if not self.servidor_compra.obtener_compra(self.txtCodigo.text()):
            self.servidor_compra.insertar_compra(self.txtCodigo.text(), self.dtpFecha.date().toString('yyyy-MM-dd'), self.txtRuc.text(), self.cmbSucursal.currentText())

    def ingresar_compra_action(self):
        self.cmbCiudad.setEnabled(True)
        self.cmbProvincia.setEnabled(True)

        self.txtRuc.setEnabled(True)
        self.dtpFecha.setEnabled(True)
        self.cmbSucursal.setEnabled(True)
        self.txtTelefono.setEnabled(True)
        self.txtRazonSocial.setEnabled(True)

        self.txtRuc.clear()
        self.txtTotal.clear()
        self.txtTelefono.clear()
        self.txtRazonSocial.clear()
        self.twCompra.setRowCount(0)
        self.twCompra.setColumnCount(0)

        self.init_seccion_informacion_general()
        self.init_seccion_producto()


    def ingresar_producto_action(self):
        try:
            if not(self.txtRuc.text() and self.txtRazonSocial.text() and self.txtTelefono.text() and self.cmbCiudad.currentText() and self.cmbProvincia.currentText()):
                self.dialogo_informacion('Error', 'Ingresar campos de proveedor')
                return
            if not(self.cmbNombre.currentText() and self.cmbMarca.currentText() and self.txtPrecioCompra.text() and self.txtCantidad.text() and self.txtPrecioOficial.text() and self.cmbCategorias.currentText()):
                self.dialogo_informacion('Error', 'Ingresar campos de producto')
                return

            #Se agrega toda la informacion a los servidores
            self.agregar_provincia()
            self.agregar_ciudad()
            self.agregar_proveedor()
            self.agregar_marca()
            self.agregar_producto()
            self.agregar_a_producto_categoria()

            self.agregar_compra()
            self.agregar_a_compra_producto()
            self.agregar_inventario()

            self.producto_categoria.clear()

            self.cmbCiudad.setEnabled(False)
            self.cmbProvincia.setEnabled(False)

            self.txtRuc.setEnabled(False)
            self.dtpFecha.setEnabled(False)
            self.txtTelefono.setEnabled(False)
            self.cmbSucursal.setEnabled(False)
            self.txtRazonSocial.setEnabled(False)

            self.init_provincia()
            self.init_detalle_compra()
            self.init_seccion_producto()

            self.producto_action()

            self.dialogo_informacion('Exito', 'Se agrego producto exitosamente')

        except Exception as e:
            print(e)

    def provincia_action(self):
        self.cmbCiudad.clear()
        self.cmbCiudad.addItems([ciudad[0]for ciudad in self.servidor_ciudad.obtener_ciudades(self.cmbProvincia.currentText())])

    def categoria_action(self):
        self.producto_categoria.add(self.cmbCategorias.currentText())
        self.dialogo_informacion('Exito', 'Se agrego categoria a producto')

        try:
            if not self.servidor_categoria.obtener_categoria(self.cmbCategorias.currentText()):
                self.servidor_categoria.insertar_categoria(self.cmbCategorias.currentText())
                self.dialogo_informacion('Exito', 'Se agrego categoria a supermercado')
        except Exception as e:
            print(e)

    def proveedor_action(self):
        try:
            if self.servidor_proveedor.obtener_proveedor(self.txtRuc.text()):
                informacion = self.servidor_proveedor.obtener_proveedor(self.txtRuc.text())[0]
                self.txtRazonSocial.setText(informacion[1])
                self.txtTelefono.setText(informacion[2])
                self.producto_action()

        except Exception as e:
            print(e)

    def limpiar_campos_action(self):
        try:
            self.txtCantidad.clear()
            self.txtPrecioCompra.clear()

            if self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText()):
                _, _, _, precio_oficial = self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText())[0]
                self.txtPrecioOficial.setText(str(precio_oficial))
            else:
                self.txtPrecioOficial.clear()
        except Exception as e:
            print(e)

    def producto_action(self):
        try:
            informacion = self.servidor_producto.obtener_producto(self.cmbNombre.currentText())[0]
            self.cmbMarca.setCurrentText(informacion[1])
            self.txtCantidad.clear()
            self.txtPrecioCompra.clear()

            if self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText()):
                _, _, _, precio_oficial = self.servidor_inventario.obtener_inventario(self.cmbSucursal.currentText(), self.cmbNombre.currentText())[0]
                self.txtPrecioOficial.setText(str(precio_oficial))
            else:
                self.txtPrecioOficial.clear()

        except Exception as e:
            print(e)

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def cerrar(self):
        self.close()



