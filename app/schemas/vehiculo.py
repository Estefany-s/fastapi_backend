from pydantic import BaseModel, Field
from typing import Optional, List
from .marca import MarcaResponse  # Importamos el schema de marca para anidarlo
from .fotografia import FotografiaResponse

class VehiculoBase(BaseModel):
    Modelo: str = Field(..., max_length=100)
    
    # Validation: ge=1996 restringe que el año sea desde 1996 en adelante
    Anio: Optional[int] = Field(..., ge=1996, description="El año debe ser mayor o igual a 1996")
    
    Color: Optional[str] = Field(None, max_length=30)
    
    # Validation: ge=0.0 fuerza un valor monetario realista y descarta negativos
    Precio: float = Field(default=1000.00, ge=0.0, description="El precio mínimo es de $0.00")
    
    ID_Marca: int

# Schema para recibir datos al CREAR
class VehiculoCreate(VehiculoBase):
    pass

# Schema para recibir datos al ACTUALIZAR (Campos opcionales)
class VehiculoUpdate(BaseModel):
    Modelo: Optional[str] = Field(None, max_length=100)
    Anio: Optional[int] = None
    Color: Optional[str] = Field(None, max_length=30)
    Precio: Optional[float] = Field(None, ge=0.0)
    ID_Marca: Optional[int] = None

# Schema de RESPUESTA estándar (Individual/Simple)
class VehiculoResponse(VehiculoBase):
    ID_Vehiculo: int

    class Config:
        from_attributes = True

# Schema de RESPUESTA AVANZADA (Trae el objeto Marca anidado)
# Esto es vital para cumplir el Ítem 7 y 14 de la rúbrica
class VehiculoConMarcaResponse(VehiculoResponse):
    marca: Optional[MarcaResponse] = None
    fotografias: List[FotografiaResponse] = []

    class Config:
        from_attributes = True