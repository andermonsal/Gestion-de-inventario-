# CodeStock

Sistema de gestión de inventario para pequeños negocios.

## Requisitos
- Docker y Docker Compose instalados.
- Python 3.9+ (si no usas Docker).
- Node.js 18+ (si no usas Docker).

## Configuración con Docker
1. Clona el repositorio.
2. Navega a la raíz del proyecto: `cd CodeStock`.
3. Ejecuta: `docker-compose up --build`.
4. Accede al frontend en `http://localhost:5173` y al backend en `http://localhost:8000`.

## Configuración Manual
### Backend
1. Navega a `backend/`.
2. Instala dependencias: `pip install -r requirements.txt`.
3. Ejecuta el servidor: `python src/main.py`.

### Frontend
1. Navega a `frontend/`.
2. Instala dependencias: `npm install`.
3. Inicia el servidor de desarrollo: `npm run dev`.