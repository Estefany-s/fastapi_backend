from pydantic import BaseModel
from typing import Optional, List

# --- ESQUEMAS DE MARCA ---
class MarcaBase(BaseModel):
    Nombre_Marca: str
    Pais_Origen: Optional[str] = None

class MarcaCreate(MarcaBase):
    pass

class MarcaResponse(MarcaBase):
    ID_Marca: int

    class Config:
        from_attributes = True

# --- ESQUEMAS DE VEHÍCULO ---
class VehiculoCreate(BaseModel):
    Modelo: str
    Anio: int
    Color: str
    ID_Marca: int

class VehiculoResponse(BaseModel):
    ID_Vehiculo: int
    Modelo: str
    Anio: int
    Color: str
    ID_Marca: int

    class Config:
        from_attributes = True

# Esquema para cuando listemos autos y queramos meter la info completa de su marca
class VehiculoConMarcaResponse(VehiculoResponse):
    marca: MarcaResponse