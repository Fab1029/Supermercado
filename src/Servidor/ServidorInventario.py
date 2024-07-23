class ServidorInventario:
    def __init__(self, db):
        self.db = db

    def insertar_inventario(self, surcursal, producto, cantidad, precio_oficial):
        query = 'Insert into inventario (sucursal, producto, cantidad, precio_oficial) values (%s, %s, %s, %s)'
        self.db.execute_query(query, (surcursal, producto, cantidad, precio_oficial))

    def modificar_inventario(self, sucursal, producto, cantidad, precio_oficial):
        query = 'Update inventario set cantidad = %s, precio_oficial = %s where sucursal = %s and producto = %s'
        self.db.execute_query(query, (cantidad, precio_oficial, sucursal, producto))

    def obtener_inventarios(self):
        query = 'Select * from inventario'
        return self.db.fetch_query(query)

    def obtener_inventario(self, sucursal, producto):
        query = 'Select * from inventario where sucursal = %s and producto = %s'
        return self.db.fetch_query(query, (sucursal, producto))

    def obtener_inventario_de_sucursal(self, sucursal):
        query = 'Select * from inventario where sucursal = %s'
        return self.db.fetch_query(query, (sucursal,))