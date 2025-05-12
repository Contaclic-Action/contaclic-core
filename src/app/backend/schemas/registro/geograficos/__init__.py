# importamos el schema de registros - geograficos
from .codigo_postal import ClaseCodigoPostalBase, ClaseCodigoPostalCreate, ClaseCodigoPostalUpdate
from .departamentos import ClaseDepartamentosBase, ClaseDepartamentosCreate, ClaseDepartamentosUpdate
from .municipios import ClaseMunicipiosBase, ClaseMunicipiosCreate, ClaseMunicipiosUpdate
from .pais import ClasePaisBase, ClasePaisCreate, ClasePaisUpdate

# exportamos las clases para que puedan ser importadas desde el paquete
__all__ = [
    "ClaseCodigoPostalBase",
    "ClaseCodigoPostalCreate",
    "ClaseCodigoPostalUpdate",
    "ClaseDepartamentosBase",
    "ClaseDepartamentosCreate",
    "ClaseDepartamentosUpdate",
    "ClaseMunicipiosBase",
    "ClaseMunicipiosCreate",
    "ClaseMunicipiosUpdate",
    "ClasePaisBase",
    "ClasePaisCreate",
    "ClasePaisUpdate"
]
