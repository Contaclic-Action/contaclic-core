# Importamos lo enrutadores desde los módulos correspondientes
from .endpoints_catalogo_terceros import router as catalogo_terceros_router
from .endpoints_empresas import router as empresas_router
from .endpoints_generales import router as generales_router
from .endpoints_geograficos import router as geograficos_router
from .endpoints_personas import router as personas_router
from .endpoints_rut_empresas import router as rut_empresas_router
from .endpoints_rut_personas import router as rut_personas_router

# listamos los enrutadores en __all__ para facilitar su importación
__all__ = [
    "catalogo_terceros_router",
    "empresas_router",
    "generales_router",
    "geograficos_router",
    "personas_router",
    "rut_empresas_router",
    "rut_personas_router",
]