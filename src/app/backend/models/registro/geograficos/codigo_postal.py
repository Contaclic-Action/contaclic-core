# coding: utf-8
from sqlalchemy import Column, Integer, String
from backend.database.base_class import Base

class CodigoPostal(Base):
    __tablename__ = "codigo_postal"

    id = Column(Integer, primary_key=True, index=True)
    codigo_postal = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    
    ############## Datos Geográficos ##############
    departamento = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    zona_postal = Column(String, nullable=False)
    sector = Column(String, nullable=True)
    barrio = Column(String, nullable=True)
    vereda = Column(String, nullable=True)


