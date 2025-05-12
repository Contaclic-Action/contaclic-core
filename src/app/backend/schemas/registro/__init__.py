# imporamos los schemas de los registros 
from .generales import ClaseGeneralesBase, ClaseGeneralesCreate, ClaseGeneralesUpdate
from .geograficos import ClaseGeograficosBase, ClaseGeograficosCreate, ClaseGeograficosUpdate
from .metodo_pago import ClaseMetodoPagoBase, ClaseMetodoPagoCreate, ClaseMetodoPagoUpdate
from .terceros import ClaseTercerosBase, ClaseTercerosCreate, ClaseTercerosUpdate

# exportamos las clases para que puedan ser importadas desde el paquete
__all__ = [
    "ClaseGeneralesBase",
    "ClaseGeneralesCreate",
    "ClaseGeneralesUpdate",
    "ClaseGeograficosBase",
    "ClaseGeograficosCreate",
    "ClaseGeograficosUpdate",
    "ClaseMetodoPagoBase",
    "ClaseMetodoPagoCreate",
    "ClaseMetodoPagoUpdate",
    "ClaseTercerosBase",
    "ClaseTercerosCreate",
    "ClaseTercerosUpdate"
]