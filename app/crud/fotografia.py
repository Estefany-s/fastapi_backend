from sqlalchemy.orm import Session
from app.models.fotografia import Fotografia
from typing import Optional
from datetime import date

def get_fotografias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Fotografia).offset(skip).limit(limit).all()

def get_fotografia_por_id(db: Session, id_fotografia: int):
    return db.query(Fotografia).filter(Fotografia.ID_Fotografia == id_fotografia).first()

def create_fotografia(db: Session, id_vehiculo: int, ruta_archivo: str, angulo: Optional[str] = None, fecha_subida: Optional[date] = None):
    db_fotografia = Fotografia(
        ID_Vehiculo=id_vehiculo,
        Ruta_Archivo=ruta_archivo,
        Angulo=angulo,
        Fecha_Subida=fecha_subida
    )
    db.add(db_fotografia)
    db.commit()
    db.refresh(db_fotografia)
    return db_fotografia

def delete_fotografia(db: Session, id_fotografia: int):
    db_fotografia = db.query(Fotografia).filter(Fotografia.ID_Fotografia == id_fotografia).first()
    if not db_fotografia:
        return None
    db.delete(db_fotografia)
    db.commit()
    return db_fotografia
