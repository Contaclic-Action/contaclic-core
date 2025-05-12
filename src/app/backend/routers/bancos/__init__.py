# Importamos las librerías necesarias
from .endpoints_bancolombia import router as bancolombia_router

# Listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "bancolombia_router",
]