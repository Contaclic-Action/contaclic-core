# backend/models/registro/geograficos/__init__.py
# Modelos geograficos compartidos entre modulo.

from .codigo_postal import CodigoPostal
from .departamentos import Departamentos    
from .municipios import Municipios
from .pais import Pais

# Exponemos las clases que queremos que sean accesibles.
__all__ = [
    "CodigoPostal",
    "Departamentos",
    "Municipios",
    "Pais",
]
