from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# export class Departamentos(Base):
class Departamentos(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)
    departamento = Column(String, unique=True, nullable=False)
    
    # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)