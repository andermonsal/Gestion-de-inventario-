import sys
import os
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

# Agrega la raíz del backend/src al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa desde rutas y gestor_inventario
from api.rutas import app
from modules.inventario.gestor_inventario import GestorInventario


from api.rutas import app

if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:8000"]
    asyncio.run(serve(app, config))
