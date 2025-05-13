from sqlalchemy import Column, Integer, String
from backend.database.base_class import Base

class Departamentos(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, index=True)
    departamento = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    
    ############## Datos Geográficos ##############
    departamento = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    