# backend/src/config/configuracion.py
from dotenv import load_dotenv
import os

load_dotenv()

class Configuracion:
    CLAVE_SECRETA = os.getenv("CLAVE_SECRETA", "tu-clave-secreta")
    RUTA_DATOS = "datos/"
    RUTA_LOGS = "logs/"

configuracion = Configuracion()