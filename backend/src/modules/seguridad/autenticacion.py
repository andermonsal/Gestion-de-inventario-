import bcrypt

class Autenticacion:
    def hashear_contrasena(self, contrasena):
        return bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verificar_contrasena(self, contrasena, hash):
        return bcrypt.checkpw(contrasena.encode('utf-8'), hash.encode('utf-8'))

    def iniciar_sesion(self, nombre_usuario, contrasena):
        from .gestor_usuarios import GestorUsuarios
        gestor_usuarios = GestorUsuarios()
        usuario = gestor_usuarios.obtener_usuario(nombre_usuario)
        if usuario and self.verificar_contrasena(contrasena, usuario["contrasena"]):
            return usuario
        raise ValueError("Credenciales inválidas")