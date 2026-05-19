from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import vehiculo as schemas_vehiculo
from app.crud import vehiculo as crud_vehiculo

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"]
)

# 1. ENDPOINT: Crear un vehículo (POST)
@router.post(
    "/", 
    response_model=schemas_vehiculo.VehiculoResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un nuevo vehículo"
)
def registrar_vehiculo(vehiculo: schemas_vehiculo.VehiculoCreate, db: Session = Depends(get_db)):
    return crud_vehiculo.create_vehiculo(db=db, vehiculo=vehiculo)


# 2. ENDPOINT: Listar todos los vehículos con sus marcas (GET)
@router.get(
    "/", 
    response_model=List[schemas_vehiculo.VehiculoConMarcaResponse],
    summary="Obtener todo el inventario de vehículos"
)
def listar_vehiculos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_vehiculo.get_vehiculos(db=db, skip=skip, limit=limit)


# 3. ENDPOINT: Obtener un vehículo por su ID (GET)
@router.get(
    "/{id_vehiculo}", 
    response_model=schemas_vehiculo.VehiculoConMarcaResponse,
    summary="Obtener los detalles de un vehículo específico"
)
def obtener_vehiculo_por_id(id_vehiculo: int, db: Session = Depends(get_db)):
    db_vehiculo = crud_vehiculo.get_vehiculo_por_id(db=db, id_vehiculo=id_vehiculo)
    if not db_vehiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehículo con ID {id_vehiculo} no encontrado."
        )
    return db_vehiculo


# 4. ENDPOINT: Actualizar un vehículo (PUT)
@router.put(
    "/{id_vehiculo}", 
    response_model=schemas_vehiculo.VehiculoResponse,
    summary="Actualizar los datos de un vehículo"
)
def modificar_vehiculo(
    id_vehiculo: int, 
    vehiculo_data: schemas_vehiculo.VehiculoUpdate, 
    db: Session = Depends(get_db)
):
    db_vehiculo = crud_vehiculo.update_vehiculo(db=db, id_vehiculo=id_vehiculo, vehiculo_data=vehiculo_data)
    if not db_vehiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se pudo actualizar. Vehículo con ID {id_vehiculo} no encontrado."
        )
    return db_vehiculo


# 5. ENDPOINT: Eliminar un vehículo (DELETE)
@router.delete(
    "/{id_vehiculo}", 
    status_code=status.HTTP_200_OK,
    summary="Eliminar un vehículo del sistema"
)
def borrar_vehiculo(id_vehiculo: int, db: Session = Depends(get_db)):
    db_vehiculo = crud_vehiculo.delete_vehiculo(db=db, id_vehiculo=id_vehiculo)
    if not db_vehiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se pudo eliminar. Vehículo con ID {id_vehiculo} no encontrado."
        )
    return {"mensaje": f"Vehículo con ID {id_vehiculo} eliminado correctamente de la base de datos."}