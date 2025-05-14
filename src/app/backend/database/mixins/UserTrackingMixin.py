from sqlalchemy import Column, String

# export class UserTrackingMixin:
class UserTrackingMixin:
    """
    Mixin para añadir campos de trazabilidad de usuario a los modelos de SQLAlchemy.
    Incluye:
    - usuario_creacion: Usuario que creó el registro
    - usuario_actualizacion: Usuario que actualizó el registro
    """
    usuario_creacion = Column(String, nullable=True, comment="Usuario que creó el registro")
    usuario_actualizacion = Column(String, nullable=True, comment="Usuario que actualizó el registro")