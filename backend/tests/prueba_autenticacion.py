import unittest
from src.modules.seguridad.autenticacion import Autenticacion
from src.modules.seguridad.gestor_usuarios import GestorUsuarios
import json

class PruebaAutenticacion(unittest.TestCase):
    def setUp(self):
        self.autenticacion = Autenticacion()
        self.gestor_usuarios = GestorUsuarios("tests/usuarios_prueba.json")
        with open("tests/usuarios_prueba.json", "w") as f:
            json.dump([{
                "nombre_usuario": "admin",
                "contrasena": self.autenticacion.hashear_contrasena("admin123"),
                "rol": "admin"
            }], f)

    def test_iniciar_sesion(self):
        usuario = self.autenticacion.iniciar_sesion("admin", "admin123")
        self.assertEqual(usuario["nombre_usuario"], "admin")

    def test_iniciar_sesion_fallido(self):
        with self.assertRaises(ValueError):
            self.autenticacion.iniciar_sesion("admin", "wrongpassword")

if __name__ == "__main__":
    unittest.main()