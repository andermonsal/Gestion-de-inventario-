from dataclasses import dataclass
from datetime import datetime

@dataclass
class Venta:
    id: int
    productos: list
    id_empleado: str
    total: float
    fecha: str