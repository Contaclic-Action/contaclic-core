# backend/models/registro/__init__.py
# Modelos geograficos para crear terceros.

from .generales import Generales
from .geograficos import Geograficos    
from .metodo_pago import MeotodoPago
from .terceros import Terceros

# Exponemos las clases que queremos que sean accesibles.
__all__ = [
    "Generales",
    "Geograficos",
    "MeotodoPago",
    "Terceros",
]