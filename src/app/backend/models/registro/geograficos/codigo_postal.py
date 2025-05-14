# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# export class CodigoPostal(Base):
class CodigoPostal(Base):
    __tablename__ = "codigo_postal"

    id = Column(Integer, primary_key=True, index=True)
    codigo_postal = Column(String, unique=True, nullable=False)
        
   # Datos de Ubicación
    departamento = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    zona_postal = Column(String, nullable=False)
    sector = Column(String, nullable=True)
    barrio = Column(String, nullable=True)
    vereda = Column(String, nullable=True)

    # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now()) 
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)



