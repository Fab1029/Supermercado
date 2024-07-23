from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem
from src.Assets.Ui_Reportes import Ui_Reportes
from src.Servidor.DataBase import DataBase
from src.Servidor.ServidorSucursal import ServidorSucursal
from src.Servidor.ServidorReportes import ServidorReportes
class ClienteReportes(QtWidgets.QWidget, Ui_Reportes):

    def __init__(self, seccion, parent = None):
        super(ClienteReportes, self).__init__(parent)
        self.setupUi(self)

        self.showFullScreen()

        self.db = DataBase()
        self.servidor_sucursal = ServidorSucursal(self.db)
        self.servidor_reportes = ServidorReportes(self.db)

        self.init_window(seccion)
        self.init_actions(seccion)

    def init_window(self, seccion):
        #Solo opcion 3 que es con fecha se habilita las fechas de ingreso
        if seccion != 3:
            self.lblFechaFin.setVisible(False)
            self.dtpFechaFin.setVisible(False)
            self.lblFechaInicio.setVisible(False)
            self.dtpFechaInicio.setVisible(False)
        else:
            self.dtpFechaFin.setDisplayFormat('MM-yyyy')
            self.dtpFechaInicio.setDisplayFormat('MM-yyyy')
            self.dtpFechaFin.setDate(QDate().currentDate())
            self.dtpFechaInicio.setDate(QDate().currentDate())

        self.cmbSucursal.addItems([sucursal[0] for sucursal in self.servidor_sucursal.obtener_sucursales()])
        self.cmbSucursal.addItem('Supermercado')

    def init_actions(self, seccion):
        self.btnAtras.clicked.connect(self.cerrar)
        self.btnObtenerReporte.clicked.connect(lambda : self.reportes(seccion)())

    def reportes(self, reporte):

        def producto_mas_demanda():
            try:
                count = 0

                self.twReporte.clear()
                self.twReporte.setColumnCount(3)
                self.twReporte.setRowCount(len(self.servidor_reportes.productos_mas_demanda())) if self.cmbSucursal.currentText() == 'Supermercado' else self.twReporte.setRowCount(len(self.servidor_reportes.productos_mas_demanda_por_sucursal(self.cmbSucursal.currentText())))
                self.twReporte.setHorizontalHeaderLabels(['Producto', 'Cantidad total', 'Total'])

                for producto, cantidad_total, total in self.servidor_reportes.productos_mas_demanda() if self.cmbSucursal.currentText() == 'Supermercado' else self.servidor_reportes.productos_mas_demanda_por_sucursal(self.cmbSucursal.currentText()):
                    self.twReporte.setItem(count, 0, QTableWidgetItem(producto))
                    self.twReporte.setItem(count, 1, QTableWidgetItem(str(cantidad_total)))
                    self.twReporte.setItem(count, 2, QTableWidgetItem(str(total)))

                    count += 1

            except Exception as e:
                print(e)

        def producto_menos_demanda():
            try:
                count = 0

                self.twReporte.clear()
                self.twReporte.setColumnCount(3)
                self.twReporte.setRowCount(len(self.servidor_reportes.productos_menos_demanda())) if self.cmbSucursal.currentText() == 'Supermercado' else self.twReporte.setRowCount(len(self.servidor_reportes.productos_menos_demanda_por_sucursal(self.cmbSucursal.currentText())))
                self.twReporte.setHorizontalHeaderLabels(['Producto', 'Cantidad total', 'Total'])

                for producto, cantidad_total, total in self.servidor_reportes.productos_menos_demanda() if self.cmbSucursal.currentText() == 'Supermercado' else self.servidor_reportes.productos_menos_demanda_por_sucursal(self.cmbSucursal.currentText()):
                    self.twReporte.setItem(count, 0, QTableWidgetItem(producto))
                    self.twReporte.setItem(count, 1, QTableWidgetItem(str(cantidad_total)))
                    self.twReporte.setItem(count, 2, QTableWidgetItem(str(total)))

                    count += 1

            except Exception as e:
                print(e)

        def balance():
            if self.dtpFechaFin.date() < self.dtpFechaInicio.date():
                self.dialogo_informacion('Alerta', 'Fechas incorrectas')
                return

            try:
                count = 0
                fecha_incio = self.dtpFechaInicio.date()
                fecha_fin = self.dtpFechaFin.date()

                fecha_incio.setDate(fecha_incio.year(), fecha_incio.month(), 1)
                fecha_fin.setDate(fecha_fin.year(), fecha_fin.month(), 1)
                fecha_fin.addMonths(1).addDays(-1)

                self.twReporte.clear()
                self.twReporte.setColumnCount(4)
                self.twReporte.setRowCount(len(self.servidor_reportes.balance_general(fecha_incio.toString('yyyy-MM-dd'), fecha_fin.toString('yyyy-MM-dd')))) if self.cmbSucursal.currentText() == 'Supermercado' else self.twReporte.setRowCount(len(self.servidor_reportes.balance_por_sucursal(fecha_incio.toString('yyyy-MM-dd'), fecha_fin.toString('yyyy-MM-dd'), self.cmbSucursal.currentText())))
                self.twReporte.setHorizontalHeaderLabels(['Fecha', 'Total ventas', 'Total compras', 'Balance'])

                for fecha, total_ventas, total_compras, balance in self.servidor_reportes.balance_general(fecha_incio.toString('yyyy-MM-dd'), fecha_fin.toString('yyyy-MM-dd')) if self.cmbSucursal.currentText() == 'Supermercado' else self.servidor_reportes.balance_por_sucursal(fecha_incio.toString('yyyy-MM-dd'), fecha_fin.toString('yyyy-MM-dd'), self.cmbSucursal.currentText()):
                    self.twReporte.setItem(count, 0, QTableWidgetItem(fecha))
                    self.twReporte.setItem(count, 1, QTableWidgetItem(str(total_ventas)))
                    self.twReporte.setItem(count, 2, QTableWidgetItem(str(total_compras)))
                    self.twReporte.setItem(count, 3, QTableWidgetItem(str(balance)))

                    count += 1

            except Exception as e:
                print(e)


        def producto_mayor_cantidad_inventario():
            try:
                count = 0

                self.twReporte.clear()
                self.twReporte.setColumnCount(2)
                self.twReporte.setRowCount(len(self.servidor_reportes.mayor_inventario())) if self.cmbSucursal.currentText() == 'Supermercado' else self.twReporte.setRowCount(len(self.servidor_reportes.mayor_inventario_por_sucursal(self.cmbSucursal.currentText())))
                self.twReporte.setHorizontalHeaderLabels(['Producto', 'Cantidad total'])

                for producto, cantidad_total in self.servidor_reportes.mayor_inventario() if self.cmbSucursal.currentText() == 'Supermercado' else self.servidor_reportes.mayor_inventario_por_sucursal(self.cmbSucursal.currentText()):
                    self.twReporte.setItem(count, 0, QTableWidgetItem(producto))
                    self.twReporte.setItem(count, 1, QTableWidgetItem(str(cantidad_total)))

                    count += 1

            except Exception as e:
                print(e)

        def clientes_mas_frecuentes():
            try:
                count = 0

                self.twReporte.clear()
                self.twReporte.setColumnCount(4)
                self.twReporte.setRowCount(len(self.servidor_reportes.cliente_mas_frecuente())) if self.cmbSucursal.currentText() == 'Supermercado' else self.twReporte.setRowCount(len(self.servidor_reportes.cliente_mas_frecuente_en_sucursal(self.cmbSucursal.currentText())))
                self.twReporte.setHorizontalHeaderLabels(['Cedula', 'Nombre', 'Numero ventas', 'Total gastado'])

                for cedula, nombre, numero_ventas, total in self.servidor_reportes.cliente_mas_frecuente() if self.cmbSucursal.currentText() == 'Supermercado' else self.servidor_reportes.cliente_mas_frecuente_en_sucursal(self.cmbSucursal.currentText()):
                    print(cedula)
                    self.twReporte.setItem(count, 0, QTableWidgetItem(cedula))
                    self.twReporte.setItem(count, 1, QTableWidgetItem(nombre))
                    self.twReporte.setItem(count, 2, QTableWidgetItem(str(numero_ventas)))
                    self.twReporte.setItem(count, 3, QTableWidgetItem(str(total)))

                    count += 1

            except Exception as e:
                print(e)

        _ = {1: producto_mas_demanda, 2: producto_menos_demanda, 3: balance, 4: producto_mayor_cantidad_inventario,
             5: clientes_mas_frecuentes}

        return _[reporte]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def cerrar(self):
        self.close()