class ServidorVenta:
    def __init__(self, db):
        self.db = db

    def insertar_venta(self, codigo, fecha, cliente, sucursal, descuento):
        query = 'Insert into venta (codigo, fecha, cliente, sucursal, descuento) values (%s, %s, %s, %s, %s)'
        self.db.execute_query(query, (codigo, fecha, cliente, sucursal, descuento))

    def obtener_ventas(self):
        query = 'Select * from venta'
        return self.db.fetch_query(query)

    def obtener_venta(self, codigo):
        query = 'Select * from venta where codigo = %s'
        return self.db.fetch_query(query, (codigo,))

    def obtener_ventas_de_sucursal(self, sucursal):
        query = 'Select * from venta where sucursal = %s'
        return self.db.fetch_query(query, (sucursal,))

    def insertar_venta_producto(self, venta, producto, cantidad, precio_venta):
        query = 'Insert into venta_producto (venta, producto, cantidad, precio_venta) values (%s, %s, %s, %s)'
        self.db.execute_query(query, (venta, producto, cantidad, precio_venta))

    def modificar_venta_producto(self, venta, producto, cantidad, precio_venta):
        query = 'Update venta_producto set cantidad = %s, precio_venta = %s where venta = %s and producto = %s'
        self.db.execute_query(query, (cantidad, precio_venta, venta, producto))

    def obtener_venta_producto(self, venta, producto):
        query = 'Select * from venta_producto where venta = %s and producto = %s'
        return self.db.fetch_query(query, (venta, producto))

    def obtener_productos_de_venta(self, venta):
        query = 'Select * from venta_producto where venta = %s'
        return self.db.fetch_query(query, (venta, ))

    def total_venta(self, venta):
        query = (
            'Select vt.total * (1- v.descuento/100) '
            'From ( '
            '    Select vp.venta, sum(vp.cantidad * vp.precio_venta) as total '
            '    From venta_producto as vp '
            '    Group by vp.venta '
            ') as vt '
            '   join venta as v on v.codigo = vt.venta '
            'Where v.codigo = %s'
        )
        return self.db.fetch_query(query, (venta,))