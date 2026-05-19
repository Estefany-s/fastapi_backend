from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status

def get_marcas(db: Session):
    return db.query(models.Marca).all()

def create_marca(db: Session, marca: schemas.MarcaCreate):
    db_marca = models.Marca(Nombre_Marca=marca.Nombre_Marca, Pais_Origen=marca.Pais_Origen)
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return db_marca

def create_vehiculo(db: Session, vehiculo: schemas.VehiculoCreate):
    marca_existe = db.query(models.Marca).filter(models.Marca.ID_Marca == vehiculo.ID_Marca).first()
    if not marca_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede crear el vehículo. La marca con ID {vehiculo.ID_Marca} no existe."
        )
    db_vehiculo = models.Vehiculo(
        Modelo=vehiculo.Modelo,
        Anio=vehiculo.Anio,
        Color=vehiculo.Color,
        ID_Marca=vehiculo.ID_Marca
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def get_todos_los_vehiculos(db: Session):
    return db.query(models.Vehiculo).all()

def get_vehiculo_por_id(db: Session, id_vehiculo: int):
    vehiculo = db.query(models.Vehiculo).filter(models.Vehiculo.ID_Vehiculo == id_vehiculo).first()
    if not vehiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehículo con ID {id_vehiculo} no encontrado."
        )
    return vehiculo