# backend/models/registro/metodo_pago/
# Modelos de metodos de pagos.

from .bancos_virtuales import BancosVirtuales
from .bancos import Bancos    
from .tipo_banco import TipoBanco


# Exponemos las clases que queremos que sean accesibles.
__all__ = [
    "BancosVirtuales",
    "Bancos",
    "TipoBanco",
]