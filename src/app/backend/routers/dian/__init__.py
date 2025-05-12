# Importamos los enrutadores desde los módulos correspondientes
from .emitidos import router as emitidos_router
from .recibidos import router as recibidos_router

# Listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "emitidos_router",
    "recibidos_router",
]