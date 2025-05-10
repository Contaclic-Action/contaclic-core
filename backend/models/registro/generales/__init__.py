# backend/models/registro/generales/__init__.py
# Modelos fiscales y tributarios compartidos entre modulo.

from .catalogo_terceros import CatalogoTerceros
from .centro_costos import CentroCostos
from .conceptos_dian import ConceptosDian
from .conceptos_rut import ConceptosRut  
from .plan_cuenta import PlanCuenta
from .subtipo_tercero import SubtipoTercero 
from .tipo_documento import TipoDocumento
from .tipo_sociedad import TipoSociedad
from .tipo_tercero import TipoTercero

# Exponemos las clases que queremos que sean accesibles.
__all__ = [
    "CatalogoTerceros",
    "CentroCostos",
    "ConceptosDian",
    "ConceptosRut",
    "PlanCuenta",
    "SubtipoTercero",
    "TipoDocumento",
    "TipoSociedad",
    "TipoTercero",
]