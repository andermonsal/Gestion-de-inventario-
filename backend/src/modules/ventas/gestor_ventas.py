from ...utils.manejador_json import leer_json, escribir_json
from datetime import datetime

class GestorVentas:
    def __init__(self, archivo_productos="datos/productos.json", archivo_ventas="datos/ventas.json"):
        self.archivo_productos = archivo_productos
        self.archivo_ventas = archivo_ventas

    def registrar_venta(self, datos_venta):
        if not all(clave in datos_venta for clave in ["productos", "id_empleado"]):
            raise ValueError("Faltan campos requeridos")
        productos = leer_json(self.archivo_productos)
        for item in datos_venta["productos"]:
            id_producto, cantidad = item["id"], item["cantidad"]
            for producto in productos:
                if producto["id"] == id_producto:
                    if producto["cantidad"] < cantidad:
                        raise ValueError(f"Stock insuficiente para {producto['nombre']}")
                    producto["cantidad"] -= cantidad
                    break
        escribir_json(self.archivo_productos, productos)
        ventas = leer_json(self.archivo_ventas)
        registro_venta = {
            "id": len(ventas) + 1,
            "productos": datos_venta["productos"],
            "id_empleado": datos_venta["id_empleado"],
            "total": sum(item["precio"] * item["cantidad"] for item in datos_venta["productos"]),
            "fecha": datetime.now().isoformat()
        }
        ventas.append(registro_venta)
        escribir_json(self.archivo_ventas, ventas)
        return registro_venta

    def obtener_historial_ventas(self, fecha_inicio=None, fecha_fin=None):
        ventas = leer_json(self.archivo_ventas)
        if fecha_inicio and fecha_fin:
            ventas = [
                v for v in ventas
                if fecha_inicio <= v["fecha"] <= fecha_fin
            ]
        return ventas