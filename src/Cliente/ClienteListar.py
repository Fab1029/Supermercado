from PyQt6 import QtWidgets
from src.Assets.Ui_Listar import Ui_Listar
from src.Servidor.DataBase import DataBase
from PyQt6.QtWidgets import QTableWidgetItem
from src.Servidor.ServidorVenta import ServidorVenta
from src.Servidor.ServidorCompra import ServidorCompra
from src.Servidor.ServidorSucursal import ServidorSucursal

class ClienteListar(QtWidgets.QWidget, Ui_Listar):
    def __init__(self, parent = None):
        super(ClienteListar, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_venta = ServidorVenta(self.db)
        self.servidor_compra = ServidorCompra(self.db)
        self.servidor_sucursal = ServidorSucursal(self.db)

        self.init_window()
        self.init_actions()


    def init_window(self):
        self.init_seleccion()
        self.init_sucursales()

    def init_actions(self):
        self.btnAtras.clicked.connect(self.cerrar)
        self.btnListar.clicked.connect(self.listar_action)

    def listar_action(self):
        self.twListado.setRowCount(0)
        self.twListado.setColumnCount(0)
        self.listar_compra() if self.cmbCompraVenta.currentIndex() == 0 else self.listar_venta()

    def listar_compra(self):
        try:
            count = 0

            self.twListado.clear()
            self.twListado.setColumnCount(5)
            self.twListado.setRowCount(len(self.servidor_compra.obtener_compras_de_sucursal(self.cmbSucursal.currentText())))
            self.twListado.setHorizontalHeaderLabels(['Codigo', 'Fecha', 'Proveedor', 'Productos', 'Total'])

            for codigo, fecha, proveedor, _ in self.servidor_compra.obtener_compras_de_sucursal(self.cmbSucursal.currentText()):
                self.twListado.setItem(count, 0, QTableWidgetItem(codigo))
                self.twListado.setItem(count, 1, QTableWidgetItem(str(fecha)))
                self.twListado.setItem(count, 2, QTableWidgetItem(proveedor))
                self.twListado.setItem(count, 3, QTableWidgetItem(','.join([producto[1] for producto in self.servidor_compra.obtener_productos_de_compra(codigo)])))
                self.twListado.setItem(count, 4, QTableWidgetItem(str(self.servidor_compra.total_compra(codigo)[0][0])))

                count += 1

        except Exception as e:
            print(e)

    def listar_venta(self):
        try:
            count = 0

            self.twListado.clear()
            self.twListado.setColumnCount(5)
            self.twListado.setRowCount(len(self.servidor_venta.obtener_ventas_de_sucursal(self.cmbSucursal.currentText())))
            self.twListado.setHorizontalHeaderLabels(['Codigo', 'Fecha', 'Cliente', 'Productos', 'Total'])

            for codigo, fecha, cliente, _, _ in self.servidor_venta.obtener_ventas_de_sucursal(self.cmbSucursal.currentText()):
                self.twListado.setItem(count, 0, QTableWidgetItem(codigo))
                self.twListado.setItem(count, 1, QTableWidgetItem(str(fecha)))
                self.twListado.setItem(count, 2, QTableWidgetItem(cliente))
                self.twListado.setItem(count, 3, QTableWidgetItem(','.join([producto[1] for producto in self.servidor_venta.obtener_productos_de_venta(codigo)])))
                self.twListado.setItem(count, 4, QTableWidgetItem(str(self.servidor_venta.total_venta(codigo)[0][0])))

                count += 1

        except Exception as e:
            print(e)

    def init_sucursales(self):
        try:
            self.cmbSucursal.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])
        except Exception as e:
            print(e)

    def init_seleccion(self):
        self.cmbCompraVenta.addItems(['Compra', 'Venta'])

    def cerrar(self):
        self.close()
