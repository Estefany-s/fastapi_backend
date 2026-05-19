from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
import httpx

from app.database import get_db
from app.schemas import fotografia as schemas_fotografia
from app.crud import fotografia as crud_fotografia

router = APIRouter(
    prefix="/fotografias",
    tags=["Fotografías"]
)

IMGBB_API_KEY = "d24a08caf60108ec78da0814f93ba3fb"
IMGBB_URL = "https://api.imgbb.com/1/upload"

@router.post("/", response_model=schemas_fotografia.FotografiaResponse, status_code=status.HTTP_201_CREATED)
async def upload_fotografia(
    id_vehiculo: int = Form(...),
    angulo: Optional[str] = Form(None),
    fecha_subida: Optional[date] = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Leer el archivo
    file_bytes = await file.read()
    
    # Subir a Imgbb
    async with httpx.AsyncClient() as client:
        files = {'image': (file.filename, file_bytes, file.content_type)}
        data = {'key': IMGBB_API_KEY}
        response = await client.post(IMGBB_URL, data=data, files=files)
        
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al subir la imagen a Imgbb")
        
    imgbb_data = response.json()
    ruta_archivo = imgbb_data["data"]["url"]
    
    # Si no hay fecha, usar hoy
    if not fecha_subida:
        fecha_subida = date.today()
        
    # Guardar en DB
    db_foto = crud_fotografia.create_fotografia(
        db=db, 
        id_vehiculo=id_vehiculo, 
        ruta_archivo=ruta_archivo, 
        angulo=angulo, 
        fecha_subida=fecha_subida
    )
    
    return db_foto

@router.get("/", response_model=List[schemas_fotografia.FotografiaResponse])
def listar_fotografias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_fotografia.get_fotografias(db=db, skip=skip, limit=limit)

@router.delete("/{id_fotografia}")
def borrar_fotografia(id_fotografia: int, db: Session = Depends(get_db)):
    db_foto = crud_fotografia.delete_fotografia(db=db, id_fotografia=id_fotografia)
    if not db_foto:
        raise HTTPException(status_code=404, detail="Fotografía no encontrada")
    return {"mensaje": "Fotografía eliminada"}
