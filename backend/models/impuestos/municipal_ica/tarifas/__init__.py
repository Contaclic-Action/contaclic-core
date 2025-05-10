# backend/models/impuestos/municipal_ica/tarifas/__init__.py
# Acuerdo municipal.

from .ica_medellin import IcaMedellin

# Definimos los modelos que serán importados por otros módulos o archivos.
__all__ = [
    "IcaMedellin",
]