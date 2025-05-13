from sqlalchemy import Column, Integer, String 
from backend.database.base_class import Base

class Municipios(Base):
    __tablename__ = "municipios"

    id = Column(Integer, primary_key=True, index=True)
    municipio = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    
    ############## Datos Geográficos ##############
    municipio = Column(String, nullable=False)
    codigo = Column(String, nullable=False)