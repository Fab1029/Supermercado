import psycopg2

class DataBase:
    def __init__(self):
        self.dbname = 'Supermercado'
        self.user = 'postgres'
        self.password = 'admin'
        self.host = 'localhost'
        self.port = 5432

    def connect(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def execute_query(self, query, params=None):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_query(self, query, params=None):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            return results
        except Exception as e:
            print(f"Error fetching query: {e}")
            raise
