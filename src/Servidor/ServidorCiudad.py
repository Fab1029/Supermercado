class ServidorCiudad:
    def __init__(self, db):
        self.db = db

    def insertar_ciudad(self, nombre, provincia):
        query = 'Insert into ciudad (nombre, provincia) values (%s, %s)'
        self.db.execute_query(query, (nombre, provincia))

    def obtener_ciudad(self, nombre):
        query = 'Select * from ciudad where nombre = %s'
        return self.db.fetch_query(query, (nombre,))
    def obtener_provincia(self, ciudad):
        query = 'Select provincia from ciudad where nombre = %s'
        return self.db.fetch_query(query, (ciudad,))

    def obtener_ciudades(self, provincia):
        query = 'Select nombre from ciudad where provincia = %s'
        return self.db.fetch_query(query, (provincia,))

