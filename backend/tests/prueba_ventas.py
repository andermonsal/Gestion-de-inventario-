import unittest
from src.modules.ventas.gestor_ventas import GestorVentas
import json

class PruebaGestorVentas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorVentas("tests/productos_prueba.json", "tests/ventas_prueba.json")
        with open("tests/productos_prueba.json", "w") as f:
            json.dump([{
                "id": "1",
                "nombre": "Lápiz",
                "precio": 1.0,
                "cantidad": 100,
                "categoria": "Papelería",
                "stock_minimo": 10,
                "activo": True
            }], f)
        with open("tests/ventas_prueba.json", "w") as f:
            json.dump([], f)

    def test_registrar_venta(self):
        venta = {
            "productos": [{"id": "1", "cantidad": 5, "precio": 1.0}],
            "id_empleado": "empleado1"
        }
        resultado = self.gestor.registrar_venta(venta)
        self.assertEqual(resultado["total"], 5.0)

if __name__ == "__main__":
    unittest.main()