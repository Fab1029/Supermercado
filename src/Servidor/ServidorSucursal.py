class ServidorSucursal:
    def __init__(self, db):
        self.db = db

    def insertar_sucursal(self, nombre, direccion, telefono, ciudad, supermercado):
        query = 'Insert into sucursal (nombre, direccion, telefono, ciudad, supermercado) values (%s, %s, %s, %s, %s)'
        self.db.execute_query(query, (nombre,direccion,telefono,ciudad, supermercado))

    def modificar_sucursal(self, nombre, direccion, telefono, ciudad):
        query = 'Update sucursal set direccion = %s, telefono = %s, ciudad = %s, where nombre = %s'
        self.db.execute_query(query, (direccion,telefono,ciudad, nombre))

    def obtener_sucursal(self, nombre):
        query = 'Select * from sucursal where nombre = %s'
        return self.db.fetch_query(query, (nombre,))

    def obtener_sucursales(self):
        query = 'Select * from sucursal'
        return self.db.fetch_query(query)

    def eliminar_sucursal(self, nombre):
        query = 'Delete from sucursal where nombre = %s'
        self.db.execute_query(query, (nombre,))

