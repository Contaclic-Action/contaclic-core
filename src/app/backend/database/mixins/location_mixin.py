from sqlalchemy import Column, String

# export class LocationMixin:
class LocationMixin:
    """
    Mixin para añadir campos de ubicación a los modelos de SQLAlchemy.
    Incluye:
    - departamento: Nombre del departamento
    - municipio: Nombre del municipio
    - zona_postal: Zona postal
    - sector: Sector
    - barrio: Barrio
    - vereda: Vereda
    """
    departamento = Column(String, nullable=False, comment="Nombre del departamento")
    municipio = Column(String, nullable=False, comment="Nombre del municipio")
    zona_postal = Column(String, nullable=False, comment="Zona postal")
    sector = Column(String, nullable=True, comment="Sector")
    barrio = Column(String, nullable=True, comment="Barrio")
    vereda = Column(String, nullable=True, comment="Vereda")