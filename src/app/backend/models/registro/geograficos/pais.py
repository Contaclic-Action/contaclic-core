from sqlalchemy import Column, Integer, String
from backend.database.base_class import Base

class Pais(Base):
    __tablename__ = "pais"

    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    
    ############## Datos Geográficos ##############
    pais = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
