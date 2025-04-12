# backend/src/modules/inventario/gestor_inventario.py
from .modelos import Producto
from ...utils.manejador_json import leer_json, escribir_json
from datetime import datetime



class GestorInventario:
    def __init__(self, ruta_archivo="datos/productos.json"):
        self.ruta_archivo = ruta_archivo

    def agregar_producto(self, datos_producto):
        if not all(clave in datos_producto for clave in ["id", "nombre", "precio", "cantidad", "categoria", "stock_minimo"]):
            raise ValueError("Faltan campos requeridos")
        productos = leer_json(self.ruta_archivo)
        if any(p["nombre"] == datos_producto["nombre"] for p in productos):
            raise ValueError("El nombre del producto ya existe")
        productos.append(datos_producto)
        escribir_json(self.ruta_archivo, productos)
        return datos_producto

    def eliminar_producto(self, id_producto, responsable, motivo):
        productos = leer_json(self.ruta_archivo)
        productos_eliminados = leer_json("datos/productos_eliminados.json")
        for producto in productos:
            if producto["id"] == id_producto:
                producto["activo"] = False
                productos_eliminados.append({
                    "producto": producto,
                    "responsable": responsable,
                    "motivo": motivo,
                    "fecha": datetime.now().isoformat()
                })
                escribir_json(self.ruta_archivo, productos)
                escribir_json("datos/productos_eliminados.json", productos_eliminados)
                return producto
        raise ValueError("Producto no encontrado")

    def filtrar_inventario(self, categoria=None, nombre=None, stock_bajo=False):
        productos = leer_json(self.ruta_archivo)
        if categoria:
            productos = [p for p in productos if p["categoria"] == categoria]
        if nombre:
            productos = [p for p in productos if nombre.lower() in p["nombre"].lower()]
        if stock_bajo:
            productos = [p for p in productos if p["cantidad"] <= p["stock_minimo"]]
        return productos