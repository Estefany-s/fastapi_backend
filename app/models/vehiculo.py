from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Vehiculo(Base):
    __tablename__ = "Vehiculos"

    ID_Vehiculo = Column(Integer, primary_key=True, index=True)
    Modelo = Column(String(100), nullable=False)
    Anio = Column(Integer)
    Precio = Column(Numeric(10, 2), nullable=False, default=0.00)
    Color = Column(String(30))

    ID_Marca = Column(
        Integer,
        ForeignKey("Marcas.ID_Marca")
    )

    marca = relationship(
        "Marca",
        back_populates="vehiculos"
    )

    fotografias = relationship(
        "Fotografia",
        back_populates="vehiculo",
        cascade="all, delete"
    )