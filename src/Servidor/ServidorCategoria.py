class ServidorCategoria:
    def __init__(self, db):
        self.db = db

    def insertar_categoria(self, nombre):
        query = 'Insert into categoria (nombre) values (%s)'
        self.db.execute_query(query, (nombre,))

    def obtener_categorias(self):
        query = 'Select * from categoria'
        return self.db.fetch_query(query)

    def obtener_categoria(self, nombre):
        query = 'Select * from categoria where nombre = %s'
        return self.db.fetch_query(query, (nombre,))

    def insertar_producto_categoria(self, producto, categoria):
        query = 'Insert into producto_categoria (producto, categoria) values (%s, %s)'
        self.db.execute_query(query, (producto, categoria))

    def obtener_producto_categoria(self, producto, categoria):
        query = 'Select * from producto_categoria where producto = %s and categoria = %s'
        return self.db.fetch_query(query, (producto,categoria))
