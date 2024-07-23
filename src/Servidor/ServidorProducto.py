class ServidorProducto:
    def __init__(self, db):
        self.db = db

    def insertar_producto(self, nombre, marca):
        query = 'Insert into producto (nombre, marca) values (%s, %s)'
        self.db.execute_query(query, (nombre, marca))

    def obtener_productos(self):
        query = 'Select * from producto'
        return self.db.fetch_query(query)

    def obtener_producto(self, nombre):
        query = 'Select * from producto where nombre = %s'
        return self.db.fetch_query(query, (nombre, ))
