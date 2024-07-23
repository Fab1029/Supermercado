class ServidorMarca:
    def __init__(self, db):
        self.db = db

    def insertar_marca(self, nombre):
        query = 'Insert into marca (nombre) values (%s)'
        self.db.execute_query(query, (nombre,))

    def obtener_marcas(self):
        query = 'Select * from marca'
        return self.db.fetch_query(query)

    def obtener_marca(self, nombre):
        query = 'Select * from marca where nombre = %s'
        return self.db.fetch_query(query, (nombre, ))

