from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Fotografia(Base):
    __tablename__ = "Fotografias"

    ID_Fotografia = Column(Integer, primary_key=True, index=True)

    Ruta_Archivo = Column(String(255), nullable=False)

    Angulo = Column(String(50))

    Fecha_Subida = Column(Date)

    ID_Vehiculo = Column(
        Integer,
        ForeignKey("Vehiculos.ID_Vehiculo")
    )

    vehiculo = relationship(
        "Vehiculo",
        back_populates="fotografias"
    )