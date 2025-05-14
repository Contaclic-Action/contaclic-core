from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

# export class CatalogoTerceros(Base):
class CatalogoTerceros(Base):
    __tablename__ = "catalogo_terceros"

    # Primary Key
    # id = Column(Integer, primary_key=True, index=True)

    id = Column(Integer, primary_key=True, index=True)
    numero_identificacion = Column(String, unique=True, nullable=False)
    dv = Column(String, nullable=False)

    # Datos del Tercero

    tipo_documento = Column(String, nullable=False)
    tipo_contribuyente = Column(String, nullable=False)

    # Datos de Ubicación
    pais = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    ciudad_municipio = Column(String, nullable=False)

    # Datos del Tercero
    primer_apellido = Column(String, nullable=True)
    segundo_apellido = Column(String, nullable=True)
    primer_nombre = Column(String, nullable=True)
    otros_nombres = Column(String, nullable=True)
    razon_social = Column(String, nullable=True)
    nombre_comercial = Column(String, nullable=True)

    # Datos de Contacto
    direccion_principal = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False)
    codigo_postal = Column(String, nullable=True)
    telefono_1 = Column(String, nullable=True)
    telefono_2 = Column(String, nullable=True)

    # Clasificacion DIAN
    codigo_actividad_economica = Column(String, nullable=True)
    actividad_secundaria = Column(String, nullable=True)
    otras_actividades = Column(String, nullable=True)

    # Responsabilidades
    codigo_responsabilidad_dian = Column(String, nullable=True)

    # Datos de la Empresa
    tipo_tercero = Column(String, nullable=False)
    tipo_sociedad = Column(String, nullable=True)
    
    # Trazabilidad
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)
    
    # Timestamps
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())