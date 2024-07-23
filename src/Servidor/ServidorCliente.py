class ServidorCliente:
    def __init__(self, db):
        self.db = db

    def insertar_cliente(self, cedula, nombre, telefono, email, tarjeta):
        query = 'Insert into cliente (cedula, nombre, telefono, email, tarjeta) values (%s, %s, %s, %s, %s)'
        self.db.execute_query(query, (cedula, nombre, telefono, email, tarjeta))

    def obtener_cliente(self, cedula):
        query = 'Select * from cliente where cedula= %s'
        return self.db.fetch_query(query, (cedula,))

    def obtener_clientes(self):
        query = 'Select * from cliente'
        return self.db.fetch_query(query)