# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware  # <-- IMPORTANTE: Añadir esta línea
from sqlalchemy.orm import Session
from typing import List
from .database import engine, get_db
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Control de Vehículos")

# --- CONFIGURACIÓN DE CORS ---
# Definimos qué orígenes (direcciones) tienen permiso de hablar con nuestra API
origins = [
    "http://localhost:3000",  # Puerto clásico de React
    "http://localhost:5173",  # Puerto estándar para Vite + React 
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Permite peticiones desde las URLs de la lista
    allow_credentials=True,
    allow_methods=["*"],              # Permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],              # Permite todos los encabezados
)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenida a la API de Carros, el servidor está corriendo perfectamente."}

# --- RUTAS DE MARCAS ---
@app.post("/marcas/", response_model=schemas.MarcaResponse, status_code=status.HTTP_201_CREATED)
def crear_marca(marca: schemas.MarcaCreate, db: Session = Depends(get_db)):
    return crud.create_marca(db=db, marca=marca)

@app.get("/marcas/", response_model=List[schemas.MarcaResponse])
def listar_marcas(db: Session = Depends(get_db)):
    return crud.get_marcas(db)

# --- RUTAS DE VEHÍCULOS ---
@app.post("/vehiculos/", response_model=schemas.VehiculoResponse, status_code=status.HTTP_201_CREATED)
def guardar_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo(db=db, vehiculo=vehiculo)

@app.get("/vehiculos/", response_model=List[schemas.VehiculoConMarcaResponse])
def listar_vehiculos(db: Session = Depends(get_db)):
    return crud.get_todos_los_vehiculos(db=db)

@app.get("/vehiculos/{id_vehiculo}", response_model=schemas.VehiculoConMarcaResponse)
def obtener_vehiculo(id_vehiculo: int, db: Session = Depends(get_db)):
    return crud.get_vehiculo_por_id(db=db, id_vehiculo=id_vehiculo)