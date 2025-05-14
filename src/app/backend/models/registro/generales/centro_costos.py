from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# export class CentroCostos(Base):
class CentroCostos(Base):
    __tablename__ = "centro_costos"

# Primary Key
    # id = Column(Integer, primary_key=True, index=True)

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)
   
    # Descripción
    nombre_descripcion = Column(String, nullable=True)
    responsable = Column(String, nullable=True)
    area = Column(String, nullable=True)
    tipo_retencion = Column(String, nullable=True)
    tipo_iva = Column(String, nullable=True)
    oservaciones = Column(String, nullable=True)
    
     # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)
    
    # Timestamps
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())