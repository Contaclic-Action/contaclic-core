# Importamos los enrutadores desde los módulos correspondientes
from .bancos import banco_router
from .dian import dian_router
from .impuestos import impuestos_router
from .registro import registro_router
from .usuarios import usuarios_router

# Listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "banco_router",
    "dian_router",
    "impuestos_router",
    "registro_router",
    "usuarios_router",
]