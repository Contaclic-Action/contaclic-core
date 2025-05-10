# backend/models/registro/terceros/__init__.py
# Modelo principal para gestionar terceros.

from .empresa import Empresa
from .persona_natural import PersonaNatural 
from .rut_empresa import RutEmpresa
from .rut_persona import Rutpersona

# Exponemos las clases que queremos que sean accesibles.
__all__ = [
    "Empresa",
    "PersonaNatural",
    "RutEmpresa",
    "Rutpersona",
]