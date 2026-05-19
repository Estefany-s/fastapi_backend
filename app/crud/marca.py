from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.marca import Marca
from app.schemas.marca import MarcaCreate, MarcaUpdate


# Obtener todas las marcas
def get_marcas(db: Session):
    return db.query(Marca).all()


# Obtener una marca por ID
def get_marca(db: Session, id_marca: int):
    marca = db.query(Marca).filter(Marca.ID_Marca == id_marca).first()

    if not marca:
        raise HTTPException(
            status_code=404,
            detail="Marca no encontrada"
        )

    return marca


# Crear marca
def create_marca(db: Session, marca: MarcaCreate):

    # Verificar si ya existe una marca con ese nombre
    marca_existente = db.query(Marca).filter(
        Marca.Nombre_Marca == marca.Nombre_Marca
    ).first()

    if marca_existente:
        raise HTTPException(
            status_code=400,
            detail="La marca ya existe"
        )

    nueva_marca = Marca(
        Nombre_Marca=marca.Nombre_Marca,
        Pais_Origen=marca.Pais_Origen
    )

    db.add(nueva_marca)
    db.commit()
    db.refresh(nueva_marca)

    return nueva_marca


# Actualizar marca
def update_marca(db: Session, id_marca: int, datos: MarcaUpdate):

    marca = get_marca(db, id_marca)

    # Buscar otra marca con el mismo nombre
    marca_existente = db.query(Marca).filter(
        Marca.Nombre_Marca == datos.Nombre_Marca,
        Marca.ID_Marca != id_marca
    ).first()

    if marca_existente:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una marca con ese nombre"
        )

    marca.Nombre_Marca = datos.Nombre_Marca
    marca.Pais_Origen = datos.Pais_Origen

    db.commit()
    db.refresh(marca)

    return marca


# Eliminar marca
def delete_marca(db: Session, id_marca: int):

    marca = get_marca(db, id_marca)

    db.delete(marca)
    db.commit()

    return {
        "mensaje": "Marca eliminada correctamente"
    }