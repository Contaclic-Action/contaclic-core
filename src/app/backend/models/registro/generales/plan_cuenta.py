from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# exportar class PlanCuenta(Base):
class PlanCuenta(Base):
    __tablename__ = "plan_cuenta"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    cuenta = Column(String, unique=True, nullable=False)
    nombre_cuenta = Column(String, nullable=False)
    naturaleza = Column(String, nullable=False)
    
    # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)