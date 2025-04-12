# backend/tests/prueba_inventario.py
import unittest
import json  # Agregamos esta importación
from src.modules.inventario.gestor_inventario import GestorInventario

class PruebaGestorInventario(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorInventario("tests/productos_prueba.json")
        with open("tests/productos_prueba.json", "w") as f:
            json.dump([], f)

    def test_agregar_producto(self):
        producto = {
            "id": "1",
            "nombre": "Lápiz",
            "precio": 1.0,
            "cantidad": 100,
            "categoria": "Papelería",
            "stock_minimo": 10
        }
        resultado = self.gestor.agregar_producto(producto)
        self.assertEqual(resultado["nombre"], "Lápiz")

    def test_agregar_producto_duplicado(self):
        producto = {
            "id": "1",
            "nombre": "Lápiz",
            "precio": 1.0,
            "cantidad": 100,
            "categoria": "Papelería",
            "stock_minimo": 10
        }
        self.gestor.agregar_producto(producto)
        with self.assertRaises(ValueError):
            self.gestor.agregar_producto(producto)

if __name__ == "__main__":
    unittest.main()