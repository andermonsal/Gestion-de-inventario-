import json
import os

def leer_json(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []
    with open(ruta_archivo, 'r') as f:
        return json.load(f)

def escribir_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f, indent=4)