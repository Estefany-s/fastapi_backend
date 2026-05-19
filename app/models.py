from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Marca(Base):
    __tablename__ = "Marcas"

    ID_Marca = Column(Integer, primary_key=True, autoincrement=True)
    Nombre_Marca = Column(String(50), nullable=False)
    Pais_Origen = Column(String(50))

    vehiculos = relationship("Vehiculo", back_populates="marca")

class Vehiculo(Base):
    __tablename__ = "Vehiculos"

    ID_Vehiculo = Column(Integer, primary_key=True, autoincrement=True)
    Modelo = Column(String(100), nullable=False)
    Anio = Column(Integer)
    Color = Column(String(30))
    ID_Marca = Column(Integer, ForeignKey("Marcas.ID_Marca"))

    marca = relationship("Marca", back_populates="vehiculos")
    fotografias = relationship("Fotografia", back_populates="vehiculo")

class Fotografia(Base):
    __tablename__ = "Fotografias"

    ID_Fotografia = Column(Integer, primary_key=True, autoincrement=True)
    Ruta_Archivo = Column(String(255), nullable=False)
    Angulo = Column(String(50))
    Fecha_Subida = Column(Date)
    ID_Vehiculo = Column(Integer, ForeignKey("Vehiculos.ID_Vehiculo"))

    vehiculo = relationship("Vehiculo", back_populates="fotografias")