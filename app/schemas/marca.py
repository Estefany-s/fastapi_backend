from pydantic import BaseModel

# Base
class MarcaBase(BaseModel):
    Nombre_Marca: str
    Pais_Origen: str | None = None


# Crear
class MarcaCreate(MarcaBase):
    pass


# Actualizar
class MarcaUpdate(MarcaBase):
    pass


# Respuesta
class MarcaResponse(MarcaBase):
    ID_Marca: int

    class Config:
        from_attributes = True