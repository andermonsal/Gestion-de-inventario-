from ...utils.manejador_json import leer_json, escribir_json

class GestorUsuarios:
    def __init__(self, ruta_archivo="datos/usuarios.json"):
        self.ruta_archivo = ruta_archivo

    def agregar_usuario(self, datos_usuario):
        if not all(clave in datos_usuario for clave in ["nombre_usuario", "contrasena", "rol"]):
            raise ValueError("Faltan campos requeridos")
        usuarios = leer_json(self.ruta_archivo)
        if any(u["nombre_usuario"] == datos_usuario["nombre_usuario"] for u in usuarios):
            raise ValueError("El nombre de usuario ya existe")
        usuarios.append(datos_usuario)
        escribir_json(self.ruta_archivo, usuarios)
        return datos_usuario

    def obtener_usuario(self, nombre_usuario):
        usuarios = leer_json(self.ruta_archivo)
        for usuario in usuarios:
            if usuario["nombre_usuario"] == nombre_usuario:
                return usuario
        return None