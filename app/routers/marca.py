from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.marca import *
from app.crud import marca as crud

router = APIRouter(
    prefix="/marcas",
    tags=["Marcas"]
)


# Conexión DB
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# GET -> listar
@router.get("/", response_model=list[MarcaResponse])
def listar_marcas(db: Session = Depends(get_db)):
    return crud.get_marcas(db)


# GET -> por id
@router.get("/{id_marca}", response_model=MarcaResponse)
def obtener_marca(id_marca: int, db: Session = Depends(get_db)):
    return crud.get_marca(db, id_marca)


# POST
@router.post("/", response_model=MarcaResponse)
def crear_marca(
    marca: MarcaCreate,
    db: Session = Depends(get_db)
):
    return crud.create_marca(db, marca)


# PUT
@router.put("/{id_marca}", response_model=MarcaResponse)
def actualizar_marca(
    id_marca: int,
    marca: MarcaUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_marca(db, id_marca, marca)


# DELETE
@router.delete("/{id_marca}")
def eliminar_marca(
    id_marca: int,
    db: Session = Depends(get_db)
):
    return crud.delete_marca(db, id_marca)