class ServidorCompra:
    def __init__(self, db):
        self.db = db

    def insertar_compra(self, codigo, fecha, proveedor, sucursal):
        query = 'Insert into compra (codigo, fecha, proveedor, sucursal) values (%s, %s, %s, %s)'
        self.db.execute_query(query, (codigo, fecha, proveedor, sucursal))

    def obtener_compras(self):
        query = 'Select * from compra'
        return self.db.fetch_query(query)

    def obtener_compra(self, codigo):
        query = 'Select * from compra where codigo = %s'
        return self.db.fetch_query(query, (codigo,))

    def obtener_compras_de_sucursal(self, sucursal):
        query = 'Select * from compra where sucursal = %s'
        return self.db.fetch_query(query, (sucursal,))

    def insertar_compra_producto(self, compra, producto, cantidad, precio_compra):
        query = 'Insert into compra_producto (compra, producto, cantidad, precio_compra) values (%s, %s, %s, %s)'
        self.db.execute_query(query, (compra, producto, cantidad, precio_compra))

    def modificar_compra_producto(self, compra, producto, cantidad, precio_compra):
        query = 'Update compra_producto set cantidad = %s, precio_compra = %s where compra = %s and producto = %s'
        self.db.execute_query(query, (cantidad, precio_compra, compra, producto))

    def obtener_compra_producto(self, compra, producto):
        query = 'Select * from compra_producto where compra = %s and producto = %s'
        return self.db.fetch_query(query, (compra, producto))

    def obtener_productos_de_compra(self, compra):
        query = 'Select * from compra_producto where compra = %s'
        return self.db.fetch_query(query, (compra, ))


    def total_compra(self, compra):
        query = 'Select sum(cantidad * precio_compra) from compra_producto where compra = %s'
        return self.db.fetch_query(query, (compra,))
