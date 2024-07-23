class ServidorProveedor:
    def __init__(self, db):
        self.db = db

    def insertar_proveedor(self, ruc, razon_social, telefono):
        query = 'Insert into proveedor (ruc, razon_social, telefono) values (%s, %s, %s)'
        self.db.execute_query(query, (ruc, razon_social, telefono))

    def obtener_proveedor(self, ruc):
        query = 'Select * from proveedor where ruc = %s'
        return self.db.fetch_query(query, (ruc,))

    def obtener_proveedores(self):
        query = 'Select * from proveedor'
        return self.db.fetch_query(query)

    def insertar_proveedor_ciudad(self, ciudad, proveedor):
        query = 'Insert into proveedor_ciudad (ciudad, proveedor) values (%s, %s)'
        self.db.execute_query(query, (ciudad, proveedor))

    def obtener_proveedor_ciudad(self, ciudad, proveedor):
        query = 'Select * from proveedor_ciudad where ciudad = %s and proveedor = %s'
        return self.db.fetch_query(query, (ciudad, proveedor))

