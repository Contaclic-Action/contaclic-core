# Importamos los enrutadores desde los módulos correspondientes
from .endpoints_municipio import router as municipio_router
from .endpoints_nacional import router as nacional_router
from .endpoints_tarifas import router as tarifas_router

# Listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "municipio_router",
    "nacional_router",
    "tarifas_router",
]

