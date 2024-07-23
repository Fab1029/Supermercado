class ServidorInformacionSupermercado:
    def __init__(self, db):
        self.db = db

    def insertar_informacion(self, ruc, razon_social, ciudad):
        query = 'Insert into supermercado (ruc, razon_social, ciudad) values (%s, %s, %s)'
        self.db.execute_query(query, (ruc, razon_social, ciudad))

    def modificar_informacion(self, ruc, razon_social, ciudad):
        query = 'Update supermercado set razon_social = %s, ciudad = %s where ruc = %s'
        self.db.execute_query(query, (razon_social, ciudad, ruc))

    def obtener_informacion(self):
        query = 'Select * from supermercado'
        return self.db.fetch_query(query)


