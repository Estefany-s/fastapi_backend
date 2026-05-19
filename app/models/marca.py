from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Marca(Base):
    __tablename__ = "Marcas"

    ID_Marca = Column(Integer, primary_key=True, index=True)
    Nombre_Marca = Column(String(50), nullable=False)
    Pais_Origen = Column(String(50))

    vehiculos = relationship(
        "Vehiculo",
        back_populates="marca",
        cascade="all, delete"
    )