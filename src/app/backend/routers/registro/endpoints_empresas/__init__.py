# Importamos los enrutadores desde los módulos correspondientes
from .consultas import router as consultas_router
from .acciones import router as acciones_router
from .import_export import router as import_export_router
from .comunicacion import router as comunicacion_router

# Listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "consultas_router",
    "acciones_router",
    "import_export_router",
    "comunicacion_router",
]