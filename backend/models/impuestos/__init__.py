# backend/models/impuestos/__init__.py
# Modelo tributarios compartidos entre modulo.

from .municipal_ica import MunicipalIca
from .nacional import Nacional

# Definimos los modelos que serán importados por otros módulos o archivos.
__all__ = [
    "MunicipalIca",
    "Nacional",
]