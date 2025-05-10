# backend/models/dian/__init__.py
# Modelos relacionados con el modulo de la Dian.

from .emitidos import Emitidos
from .recibidos import Recibidos


# Definimos los modelos que serán importados por otros módulos o archivos.
__all__ = [
    "Emitidos",
    "Recibidos",
]