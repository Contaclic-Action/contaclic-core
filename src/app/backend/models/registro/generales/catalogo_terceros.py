from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.database.base_class import Base

class catalogo_terceros(Base):
    __tablename__ = "catalogo_terceros"

    numero_identificacion = Column(String, primary_key=True, index=True)
    tipo_documento = Column(String, nullable=False)
    tipo_contribuyente = Column(String, nullable=False)

    pais = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    ciudad_municipio = Column(String, nullable=False)

    primer_apellido = Column(String, nullable=True)
    segundo_apellido = Column(String, nullable=True)
    primer_nombre = Column(String, nullable=True)
    otros_nombres = Column(String, nullable=True)

    razon_social = Column(String, nullable=True)
    nombre_comercial = Column(String, nullable=True)

    direccion_principal = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False)
    codigo_postal = Column(String, nullable=True)
    telefono_1 = Column(String, nullable=True)
    telefono_2 = Column(String, nullable=True)

    codigo_actividad_economica = Column(String, nullable=True)
    actividad_secundaria = Column(String, nullable=True)
    otras_actividades = Column(String, nullable=True)

    codigo_responsabilidad_dian = Column(String, nullable=True)
    tipo_tercero = Column(String, nullable=False)
    subtipo_tercero = Column(String, nullable=True)
    tipo_sociedad = Column(String, nullable=True)

    tiene_configuracion = Column(Boolean, default=False)
    usuario_creacion = Column(String, nullable=True)
    estado_empresa = Column(String, nullable=True)
    representante_legal = Column(String, nullable=True)
    estado_rut = Column(String, nullable=True)
    
    # Timestamps
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())