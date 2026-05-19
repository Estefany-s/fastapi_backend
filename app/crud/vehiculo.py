from sqlalchemy.orm import Session
from app.models.vehiculo import Vehiculo
from app.schemas.vehiculo import VehiculoCreate, VehiculoUpdate

# 1. Obtener todos los vehículos (Para el inventario y catálogo)
def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehiculo).offset(skip).limit(limit).all()

# 2. Obtener un vehículo específico por su ID
def get_vehiculo_por_id(db: Session, id_vehiculo: int):
    return db.query(Vehiculo).filter(Vehiculo.ID_Vehiculo == id_vehiculo).first()

# 3. Obtener vehículos filtrados por Marca (Útil para el Ítem 15 de la rúbrica)
def get_vehiculos_por_marca(db: Session, id_marca: int):
    return db.query(Vehiculo).filter(Vehiculo.ID_Marca == id_marca).all()

# 4. Crear un nuevo vehículo (Mapea automáticamente el campo Precio)
def create_vehiculo(db: Session, vehiculo: VehiculoCreate):
    db_vehiculo = Vehiculo(
        Modelo=vehiculo.Modelo,
        Anio=vehiculo.Anio,
        Color=vehiculo.Color,
        Precio=vehiculo.Precio,  # <-- Mapeo del campo Precio
        ID_Marca=vehiculo.ID_Marca
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

# 5. Actualizar un vehículo existente (Fácil y dinámico)
def update_vehiculo(db: Session, id_vehiculo: int, vehiculo_data: VehiculoUpdate):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.ID_Vehiculo == id_vehiculo).first()
    if not db_vehiculo:
        return None
    
    # Convertimos los datos entrantes en un diccionario excluyendo lo que venga vacío (None)
    update_data = vehiculo_data.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_vehiculo, key, value)
        
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

# 6. Eliminar un vehículo (Físico o cascada automática según tu modelo)
def delete_vehiculo(db: Session, id_vehiculo: int):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.ID_Vehiculo == id_vehiculo).first()
    if not db_vehiculo:
        return None
    
    db.delete(db_vehiculo)
    db.commit()
    return db_vehiculo