from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# exportamos a clase Municipios(Base):
class Municipios(Base):
    __tablename__ = "municipios"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)
    municipio = Column(String, unique=True, nullable=False)
    
    # Datos de Ubicación
    departamento = Column(String, nullable=False)

    # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)

