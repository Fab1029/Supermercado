import psycopg2
from psycopg2.extras import execute_values
import random
from faker import Faker

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    dbname = 'Supermercado',
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = 5432,
)
cur = conn.cursor()

fake = Faker()

# Poblar tabla provincia
def poblar_provincias():
    provincias = ['Pichincha', 'Guayas', 'Azuay']
    execute_values(cur, "INSERT INTO provincia (nombre) VALUES %s ON CONFLICT DO NOTHING", [(prov,) for prov in provincias])

# Poblar tabla ciudad
def poblar_ciudades():
    ciudades = [
        ('Quito', 'Pichincha'),
        ('Guayaquil', 'Guayas'),
        ('Cuenca', 'Azuay'),
        ('Samborondón', 'Guayas')
    ]
    execute_values(cur, "INSERT INTO ciudad (nombre, provincia) VALUES %s ON CONFLICT DO NOTHING", ciudades)

# Poblar tabla supermercado
def poblar_supermercados():
    supermercados = [
        ('1790011122001', 'Supermercado La Favorita', 'Quito')
    ]
    execute_values(cur, "INSERT INTO supermercado (ruc, razon_social, ciudad) VALUES %s ON CONFLICT DO NOTHING", supermercados)

# Poblar tabla sucursal
def poblar_sucursales():
    sucursales = [
        ('Sucursal Quito Norte', 'Av. Amazonas y Naciones Unidas', '022234567', 'Quito', '1790011122001'),
        ('Sucursal Quito Sur', 'Av. Maldonado y Morán Valverde', '022234568', 'Quito', '1790011122001'),
        ('Sucursal Guayaquil Norte', 'Av. Francisco de Orellana', '042345678', 'Guayaquil', '1790011122001'),
        ('Sucursal Samborondón', 'Km 1.5 Vía Samborondón', '042345679', 'Samborondón', '1790011122001')
    ]
    execute_values(cur, "INSERT INTO sucursal (nombre, direccion, telefono, ciudad, supermercado) VALUES %s ON CONFLICT DO NOTHING", sucursales)

# Poblar tabla proveedor
def poblar_proveedores():
    proveedores = []
    for _ in range(10):
        ruc = fake.unique.numerify(text='##########')
        razon_social = fake.company()
        telefono = fake.phone_number()[:10]
        proveedores.append((ruc, razon_social, telefono))
    execute_values(cur, "INSERT INTO proveedor (ruc, razon_social, telefono) VALUES %s ON CONFLICT DO NOTHING", proveedores)

# Poblar tabla proveedor_ciudad
def poblar_proveedor_ciudad():
    ciudades = ['Quito', 'Guayaquil', 'Cuenca', 'Samborondón']
    cur.execute("SELECT ruc FROM proveedor")
    proveedores = cur.fetchall()
    proveedor_ciudad = []
    for proveedor in proveedores:
        ciudad = random.choice(ciudades)
        proveedor_ciudad.append((ciudad, proveedor[0]))
    execute_values(cur, "INSERT INTO proveedor_ciudad (ciudad, proveedor) VALUES %s ON CONFLICT DO NOTHING", proveedor_ciudad)

# Poblar tabla compra
def poblar_compras():
    cur.execute("SELECT nombre FROM sucursal")
    sucursales = cur.fetchall()
    cur.execute("SELECT ruc FROM proveedor")
    proveedores = cur.fetchall()
    compras = []
    for i in range(50):
        codigo = f'COMP{i:03d}'
        fecha = fake.date_between(start_date='-1y', end_date='today')
        proveedor = random.choice(proveedores)[0]
        sucursal = random.choice(sucursales)[0]
        compras.append((codigo, fecha, proveedor, sucursal))
    execute_values(cur, "INSERT INTO compra (codigo, fecha, proveedor, sucursal) VALUES %s ON CONFLICT DO NOTHING", compras)

# Poblar tabla marca
def poblar_marcas():
    marcas = ['Marca A', 'Marca B', 'Marca C']
    execute_values(cur, "INSERT INTO marca (nombre) VALUES %s ON CONFLICT DO NOTHING", [(marca,) for marca in marcas])

# Poblar tabla producto
def poblar_productos():
    cur.execute("SELECT nombre FROM marca")
    marcas = cur.fetchall()
    productos = []
    for i in range(20):
        nombre = f'Producto {i+1}'
        marca = random.choice(marcas)[0]
        productos.append((nombre, marca))
    execute_values(cur, "INSERT INTO producto (nombre, marca) VALUES %s ON CONFLICT DO NOTHING", productos)

# Poblar tabla compra_producto
def poblar_compra_producto():
    cur.execute("SELECT codigo FROM compra")
    compras = cur.fetchall()
    cur.execute("SELECT nombre FROM producto")
    productos = cur.fetchall()
    compra_producto = []
    existing_combos = set()
    for compra in compras:
        for _ in range(random.randint(1, 5)):
            producto = random.choice(productos)[0]
            if (compra[0], producto) not in existing_combos:
                cantidad = random.randint(50, 300)
                precio_compra = round(random.uniform(1.0, 3.0), 2)
                compra_producto.append((compra[0], producto, cantidad, precio_compra))
                existing_combos.add((compra[0], producto))
    execute_values(cur, "INSERT INTO compra_producto (compra, producto, cantidad, precio_compra) VALUES %s ON CONFLICT DO NOTHING", compra_producto)

# Poblar tabla inventario
def poblar_inventario():
    cur.execute("SELECT nombre FROM sucursal")
    sucursales = cur.fetchall()
    cur.execute("SELECT nombre FROM producto")
    productos = cur.fetchall()
    inventario = []
    existing_combos = set()
    for sucursal in sucursales:
        for producto in productos:
            if (sucursal[0], producto[0]) not in existing_combos:
                cantidad = random.randint(50, 300)
                precio_oficial = round(random.uniform(1.5, 4.0), 2)
                inventario.append((sucursal[0], producto[0], cantidad, precio_oficial))
                existing_combos.add((sucursal[0], producto[0]))
    execute_values(cur, "INSERT INTO inventario (sucursal, producto, cantidad, precio_oficial) VALUES %s ON CONFLICT DO NOTHING", inventario)

# Poblar tabla categoria
def poblar_categorias():
    categorias = ['Categoria A', 'Categoria B', 'Categoria C']
    execute_values(cur, "INSERT INTO categoria (nombre) VALUES %s ON CONFLICT DO NOTHING", [(cat,) for cat in categorias])

# Poblar tabla producto_categoria
def poblar_producto_categoria():
    cur.execute("SELECT nombre FROM producto")
    productos = cur.fetchall()
    cur.execute("SELECT nombre FROM categoria")
    categorias = cur.fetchall()
    producto_categoria = []
    existing_combos = set()
    for producto in productos:
        categoria = random.choice(categorias)[0]
        if (producto[0], categoria) not in existing_combos:
            producto_categoria.append((producto[0], categoria))
            existing_combos.add((producto[0], categoria))
    execute_values(cur, "INSERT INTO producto_categoria (producto, categoria) VALUES %s ON CONFLICT DO NOTHING", producto_categoria)

# Poblar tabla cliente
def poblar_clientes():
    clientes = []
    for _ in range(30):
        cedula = fake.unique.numerify(text='##########')
        nombre = fake.name()
        telefono = fake.phone_number()[:10]
        email = fake.email()
        tarjeta = fake.boolean()
        clientes.append((cedula, nombre, telefono, email, tarjeta))
    execute_values(cur, "INSERT INTO cliente (cedula, nombre, telefono, email, tarjeta) VALUES %s ON CONFLICT DO NOTHING", clientes)

# Poblar tabla venta
def poblar_ventas():
    cur.execute("SELECT cedula FROM cliente")
    clientes = cur.fetchall()
    cur.execute("SELECT nombre FROM sucursal")
    sucursales = cur.fetchall()
    ventas = []
    for i in range(50):
        codigo = f'VENTA{i:03d}'
        fecha = fake.date_between(start_date='-6mo', end_date='today')
        cliente = random.choice(clientes)[0]
        sucursal = random.choice(sucursales)[0]
        descuento = round(random.uniform(0.0, 0.3), 2)
        ventas.append((codigo, fecha, cliente, sucursal, descuento))
    execute_values(cur, "INSERT INTO venta (codigo, fecha, cliente, sucursal, descuento) VALUES %s ON CONFLICT DO NOTHING", ventas)

# Poblar tabla venta_producto
def poblar_venta_producto():
    cur.execute("SELECT codigo FROM venta")
    ventas = cur.fetchall()
    cur.execute("SELECT nombre FROM producto")
    productos = cur.fetchall()
    venta_producto = []
    existing_combos = set()
    for venta in ventas:
        for _ in range(random.randint(1, 5)):
            producto = random.choice(productos)[0]
            if (venta[0], producto) not in existing_combos:
                cantidad = random.randint(1, 10)
                precio_venta = round(random.uniform(2.0, 5.0), 2)
                venta_producto.append((venta[0], producto, cantidad, precio_venta))
                existing_combos.add((venta[0], producto))
    execute_values(cur, "INSERT INTO venta_producto (venta, producto, cantidad, precio_venta) VALUES %s ON CONFLICT DO NOTHING", venta_producto)

# Ejecutar las funciones para poblar las tablas
try:
    poblar_provincias()
    poblar_ciudades()
    poblar_supermercados()
    poblar_sucursales()
    poblar_proveedores()
    poblar_proveedor_ciudad()
    poblar_compras()
    poblar_marcas()
    poblar_productos()
    poblar_compra_producto()
    poblar_inventario()
    poblar_categorias()
    poblar_producto_categoria()
    poblar_clientes()
    poblar_ventas()
    poblar_venta_producto()
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cur.close()
    conn.close()

