# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# IMPORTAR MODELOS
from app.models.marca import Marca
from app.models.vehiculo import Vehiculo

# IMPORTAR ROUTERS
from app.routers import marca
from app.routers import vehiculo

# CREAR TABLAS
Base.metadata.create_all(bind=engine)

# APP
app = FastAPI(
    title="API de Control de Vehículos"
)

# CORS
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RUTA PRINCIPAL
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenida a la API de Carros, el servidor está corriendo perfectamente."
    }

# ROUTERS
app.include_router(marca.router)
app.include_router(vehiculo.router)