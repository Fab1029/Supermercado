class ServidorProvincia:
    def __init__(self, db):
        self.db = db

    def insertar_provincia(self, nombre):
        query = 'Insert into provincia (nombre) values (%s)'
        self.db.execute_query(query, (nombre,))

    def obtener_provincia(self, nombre):
        query = 'Select * from provincia where nombre = %s'
        return self.db.fetch_query(query, (nombre, ))

    def obtener_provincias(self):
        query = 'Select nombre from provincia'
        return self.db.fetch_query(query)

