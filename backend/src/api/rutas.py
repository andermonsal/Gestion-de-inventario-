# backend/src/api/rutas.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from ..modules.inventario.gestor_inventario import GestorInventario
from ..modules.ventas.gestor_ventas import GestorVentas
from ..modules.seguridad.autenticacion import Autenticacion
from ..modules.seguridad.gestor_usuarios import GestorUsuarios



app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
gestor_inventario = GestorInventario()
gestor_ventas = GestorVentas()
autenticacion = Autenticacion()
gestor_usuarios = GestorUsuarios()

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)):
    usuario = gestor_usuarios.obtener_usuario(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="Token inválido")
    return usuario

@app.post("/login")
async def login(nombre_usuario: str, contrasena: str):
    try:
        usuario = autenticacion.iniciar_sesion(nombre_usuario, contrasena)
        return {"token": usuario["nombre_usuario"], "rol": usuario["rol"]}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.post("/productos")
async def agregar_producto(producto: dict, usuario: dict = Depends(obtener_usuario_actual)):
    if usuario["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    try:
        return gestor_inventario.agregar_producto(producto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/productos")
async def filtrar_productos(categoria: str = None, nombre: str = None, stock_bajo: bool = False):
    return gestor_inventario.filtrar_inventario(categoria, nombre, stock_bajo)

@app.post("/ventas")
async def registrar_venta(venta: dict, usuario: dict = Depends(obtener_usuario_actual)):
    try:
        return gestor_ventas.registrar_venta({**venta, "id_empleado": usuario["nombre_usuario"]})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventas")
async def obtener_historial_ventas(fecha_inicio: str = None, fecha_fin: str = None):
    return gestor_ventas.obtener_historial_ventas(fecha_inicio, fecha_fin)