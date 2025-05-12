# Importamos los schemas de los registros terceros
from .empresa import ClaseEmpresaBase, ClaseEmpresaCreate, ClaseEmpresaUpdate
from .persona_natural import ClasePersonaNaturalBase, ClasePersonaNaturalCreate, ClasePersonaNaturalUpdate
from .rut_empresa import ClaseRutEmpresaBase, ClaseRutEmpresaCreate, ClaseRutEmpresaUpdate
from .rut_persona import ClaseRutPersonaBase, ClaseRutPersonaCreate, ClaseRutPersonaUpdate

# Exportamos las clases para que puedan ser importadas desde el paquete
__all__ = [
    "ClaseEmpresaBase",
    "ClaseEmpresaCreate",
    "ClaseEmpresaUpdate",
    "ClasePersonaNaturalBase",
    "ClasePersonaNaturalCreate",
    "ClasePersonaNaturalUpdate",
    "ClaseRutEmpresaBase",
    "ClaseRutEmpresaCreate",
    "ClaseRutEmpresaUpdate",
    "ClaseRutPersonaBase",
    "ClaseRutPersonaCreate",
    "ClaseRutPersonaUpdate"
]