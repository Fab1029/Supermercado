class ServidorReportes:
    def __init__(self, db):
        self.db = db

    def productos_mas_demanda_por_sucursal(self, sucursal):
        query = """
                Select vp.producto, sum(vp.cantidad) as total_cantidad, sum(vp.cantidad * vp.precio_venta * (1 - (vp.cantidad * vp.precio_venta * subquery1.descuento / subquery1.total) / 100)) as total_venta_aplicada_descuento
                From (
                    Select vp.venta as venta, v.descuento as descuento, sum(vp.cantidad * vp.precio_venta) as total
                    From venta_producto as vp
                        join venta as v on v.codigo = vp.venta
                    Where v.sucursal = %s
                    Group by vp.venta, v.descuento
                ) AS subquery1
                    join venta_producto as vp on vp.venta = subquery1.venta
                Group by vp.producto
                Having sum(vp.cantidad) = (
                    Select max(subquery2.num_cantidad)
                    From (
                        Select sum(vp.cantidad) as num_cantidad
                        From venta_producto as vp
                            join venta as v on v.codigo = vp.venta
                        Where v.sucursal = %s
                        Group by vp.producto
                    ) as subquery2
                )
                """
        return self.db.fetch_query(query, (sucursal, sucursal))

    def productos_mas_demanda(self):
        query = """
                Select vp.producto, sum(vp.cantidad) as total_cantidad, sum(vp.cantidad * vp.precio_venta * (1 - (vp.cantidad * vp.precio_venta * subquery1.descuento / subquery1.total) / 100)) as total_venta_aplicada_descuento
                From (
                    Select vp.venta as venta, v.descuento as descuento, sum(vp.cantidad * vp.precio_venta) as total
                    From venta_producto as vp
                        join venta as v on v.codigo = vp.venta
                    Group by vp.venta, v.descuento
                ) AS subquery1
                    join venta_producto as vp on vp.venta = subquery1.venta
                Group by vp.producto
                Having sum(vp.cantidad) = (
                    Select max(subquery2.num_cantidad)
                    From (
                        Select sum(vp.cantidad) as num_cantidad
                        From venta_producto as vp
                            join venta as v on v.codigo = vp.venta
                        Group by vp.producto
                    ) as subquery2
                )
                """
        return self.db.fetch_query(query)

    def productos_menos_demanda_por_sucursal(self, sucursal):
        query = """
                Select vp.producto, sum(vp.cantidad) as total_cantidad, sum(vp.cantidad * vp.precio_venta * (1 - (vp.cantidad * vp.precio_venta * subquery1.descuento / subquery1.total) / 100)) as total_venta_aplicada_descuento
                From (
                    Select vp.venta as venta, v.descuento as descuento, sum(vp.cantidad * vp.precio_venta) as total
                    From venta_producto as vp
                        join venta as v on v.codigo = vp.venta
                    Where v.sucursal = %s
                    Group by vp.venta, v.descuento
                ) AS subquery1
                    join venta_producto as vp on vp.venta = subquery1.venta
                Group by vp.producto
                Having sum(vp.cantidad) = (
                    Select min(subquery2.num_cantidad)
                    From (
                        Select sum(vp.cantidad) as num_cantidad
                        From venta_producto as vp
                            join venta as v on v.codigo = vp.venta
                        Where v.sucursal = %s
                        Group by vp.producto
                    ) as subquery2
                )
                """
        return self.db.fetch_query(query, (sucursal,sucursal))

    def productos_menos_demanda(self):
        query = """
                Select vp.producto, sum(vp.cantidad) as total_cantidad, sum(vp.cantidad * vp.precio_venta * (1 - (vp.cantidad * vp.precio_venta * subquery1.descuento / subquery1.total) / 100)) as total_venta_aplicada_descuento
                From (
                    Select vp.venta as venta, v.descuento as descuento, sum(vp.cantidad * vp.precio_venta) as total
                    From venta_producto as vp
                        join venta as v on v.codigo = vp.venta
                    Group by vp.venta, v.descuento
                ) AS subquery1
                    join venta_producto as vp on vp.venta = subquery1.venta
                Group by vp.producto
                Having sum(vp.cantidad) = (
                    Select min(subquery2.num_cantidad)
                    From (
                        Select sum(vp.cantidad) as num_cantidad
                        From venta_producto as vp
                            join venta as v on v.codigo = vp.venta
                        Group by vp.producto
                    ) as subquery2
                )
                """
        return self.db.fetch_query(query)


    def mayor_inventario_por_sucursal(self, sucursal):
        query = """
                Select i.producto, i.cantidad
                From inventario as i 
                Where i.cantidad = (
                    Select max(i.cantidad)
                    From inventario as i 
                    Where i.sucursal = %s
                )
                """
        return self.db.fetch_query(query, (sucursal, ))

    def mayor_inventario(self):
        query = """
                Select i.producto, i.cantidad
                From inventario as i 
                Where i.cantidad = (
                    Select max(inventario.cantidad)
                    From inventario
                )
                """
        return self.db.fetch_query(query)

    def cliente_mas_frecuente_en_sucursal(self, sucursal):
        query = """
                Select subquery2.cedula, subquery2.nombre, count(v.codigo) as num_ventas, subquery2.total_venta_aplicada_descuento
                From (
                    Select c.cedula as cedula, c.nombre as nombre, v.codigo as codigo, 
                       subquery1.total_venta * (1 - v.descuento / 100) as total_venta_aplicada_descuento
                    From (
                        Select vp.venta as venta, sum(vp.cantidad * vp.precio_venta) as total_venta
                        From venta_producto as vp
                        Group by vp.venta
                    ) as subquery1
                        join venta as v on v.codigo = subquery1.venta
                        join cliente as c on c.cedula = v.cliente
                    Where v.sucursal = %s
            ) as subquery2
                join venta as v on v.codigo = subquery2.codigo
            Where v.sucursal = %s
            Group by subquery2.cedula, subquery2.nombre, subquery2.total_venta_aplicada_descuento
            Having count(v.codigo) = (
                Select max(subquery3.num_ventas)
                From (
                    Select count(v.codigo) as num_ventas
                    From venta as v
                    Where v.sucursal = %s
                    Group by v.cliente
                ) as subquery3
            )
            """
        return self.db.fetch_query(query, (sucursal, sucursal, sucursal))

    def cliente_mas_frecuente(self):
        query = """
                Select subquery2.cedula, subquery2.nombre, count(v.codigo) as num_ventas, subquery2.total_venta_aplicada_descuento
                From (
                    Select c.cedula as cedula, c.nombre as nombre, v.codigo as codigo, 
                       subquery1.total_venta * (1 - v.descuento / 100) as total_venta_aplicada_descuento
                    From (
                        Select vp.venta as venta, sum(vp.cantidad * vp.precio_venta) as total_venta
                        From venta_producto as vp
                        Group by vp.venta
                    ) as subquery1
                        join venta as v on v.codigo = subquery1.venta
                        join cliente as c on c.cedula = v.cliente
            ) as subquery2
                join venta as v on v.codigo = subquery2.codigo
            Group by subquery2.cedula, subquery2.nombre, subquery2.total_venta_aplicada_descuento
            Having count(v.codigo) = (
                Select max(subquery3.num_ventas)
                From (
                    Select count(v.codigo) as num_ventas
                    From venta as v
                    Group by v.cliente
                ) as subquery3
            )
            """
        return self.db.fetch_query(query)


    def balance_por_sucursal(self, fecha_inicio, fecha_fin, sucursal):
        query = """
                Select 
                    coalesce(v.fecha, c.fecha) as fecha,
                    coalesce(v.total_venta, 0) as total_venta,
                    coalesce(c.total_compra, 0) as total_compra,
                    coalesce(v.total_venta, 0) - coalesce(c.total_compra, 0) as balance
                From (
                    Select 
                        to_char(v.fecha, 'MM-YYYY') as fecha, sum(vp.cantidad * vp.precio_venta * (1 - v.descuento / 100)) as total_venta
                    From venta_producto as vp
                        join venta as v ON v.codigo = vp.venta
                    Where v.fecha between to_date(%s, 'YYYY-MM-DD') and to_date(%s, 'YYYY-MM-DD') and v.sucursal = %s
                    Group by to_char(v.fecha, 'MM-YYYY')
                    ) as v
                Full outer join (
                    Select 
                        to_char(c.fecha, 'MM-YYYY') as fecha,
                        sum(cp.cantidad * cp.precio_compra) as total_compra
                    From compra_producto as cp
                        join compra as c on c.codigo = cp.compra
                    Where c.fecha between to_date(%s, 'YYYY-MM-DD') and to_date(%s, 'YYYY-MM-DD') and c.sucursal = %s
                    Group by to_char(c.fecha, 'MM-YYYY')
                    ) as c
                On v.fecha = c.fecha
                Order by fecha
                """
        return self.db.fetch_query(query, (fecha_inicio, fecha_fin, sucursal,fecha_inicio, fecha_fin, sucursal))

    def balance_general(self, fecha_inicio, fecha_fin):
        query = """
                Select 
                    coalesce(v.fecha, c.fecha) as fecha,
                    coalesce(v.total_venta, 0) as total_venta,
                    coalesce(c.total_compra, 0) as total_compra,
                    coalesce(v.total_venta, 0) - coalesce(c.total_compra, 0) as balance
                From (
                    Select 
                        to_char(v.fecha, 'MM-YYYY') as fecha, sum(vp.cantidad * vp.precio_venta * (1 - v.descuento / 100)) as total_venta
                    From venta_producto as vp
                        join venta as v ON v.codigo = vp.venta
                    Where v.fecha between to_date(%s, 'YYYY-MM-DD') and to_date(%s, 'YYYY-MM-DD')
                    Group by to_char(v.fecha, 'MM-YYYY')
                    ) as v
                Full outer join (
                    Select 
                        to_char(c.fecha, 'MM-YYYY') as fecha,
                        sum(cp.cantidad * cp.precio_compra) as total_compra
                    From compra_producto as cp
                        join compra as c on c.codigo = cp.compra
                    Where c.fecha between to_date(%s, 'YYYY-MM-DD') and to_date(%s, 'YYYY-MM-DD')
                    Group by to_char(c.fecha, 'MM-YYYY')
                    ) as c
                On v.fecha = c.fecha
                Order by fecha
                """
        return self.db.fetch_query(query, (fecha_inicio, fecha_fin,fecha_inicio, fecha_fin))



