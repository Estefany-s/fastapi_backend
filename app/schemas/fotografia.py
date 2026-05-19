from pydantic import BaseModel
from typing import Optional
from datetime import date

class FotografiaBase(BaseModel):
    Angulo: Optional[str] = None
    Fecha_Subida: Optional[date] = None
    ID_Vehiculo: int

class FotografiaCreate(FotografiaBase):
    # Ruta_Archivo is not provided by the user, it will be obtained from imgbb
    pass

class FotografiaUpdate(BaseModel):
    Angulo: Optional[str] = None
    Fecha_Subida: Optional[date] = None

class FotografiaResponse(FotografiaBase):
    ID_Fotografia: int
    Ruta_Archivo: str

    class Config:
        from_attributes = True
