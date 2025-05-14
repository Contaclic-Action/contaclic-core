from sqlalchemy import Column, String

# export class IdentifiableMixin:
class IdentifiableMixin:
    """
    Mixin para añadir un campo de identificación a los modelos de SQLAlchemy.
    Incluye:
    - numero_identificacion: Número de identificación del registro
    - dv: Dígito de verificación del número de identificación
    """
    numero_identificacion = Column(String, unique=True, nullable=False, comment="Número de identificación")
    dv = Column(String, nullable=False, comment="Dígito de verificación")