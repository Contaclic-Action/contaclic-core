from sqlalchemy import Column, String, DateTime, func

class AuditMixin:
    """
    Mixin para añadir trazabilidad a los modelos de SQLAlchemy.
    Incluye:
    - fecha_creacion: Fecha en que se creó el registro
    - fecha_actualizacion: Fecha de la última modificación
    - usuario_creacion: Usuario que creó el registro
    - usuario_actualizacion: Usuario que actualizó el registro
    """
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), comment="Fecha de creación")
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now(), comment="Fecha de actualización")
    usuario_creacion = Column(String, nullable=True, comment="Usuario que creó el registro")
    usuario_actualizacion = Column(String, nullable=True, comment="Usuario que actualizó el registro")
