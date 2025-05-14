# Agrupamos submodulos de registro

from .generales import modelo_registro as generales_modelo_registro
from .geograficos import modelo_registro as geograficos_modelo_registro
from .metodo_pago import modelo_registro as metodo_pago_modelo_registro
from .terceros import modelo_registro as terceros_modelo_registro

# Exponemos los submodulos
__all__ = [
    "generales_modelo_registro",
    "geograficos_modelo_registro",
    "metodo_pago_modelo_registro",
    "terceros_modelo_registro"
]