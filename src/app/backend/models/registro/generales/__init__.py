# backend/models/registro/generales/__init__.py
# Modelos fiscales y tributarios compartidos entre modulo.

from .catalogo_terceros import CatalogoTerceros
from .centro_costos import CentroCostos
from .conceptos_rut import ConceptosRut  
from .plan_cuenta import PlanCuenta
from .clientes import Clientes
from .proveedores import Proveedores
from .tipo_documento import TipoDocumento
from .tipo_sociedad import TipoSociedad
from .tipo_tercero import TipoTercero

# Exportar las clases
__all__ = [
    "CatalogoTerceros",
    "CentroCostos",
    "ConceptosRut",
    "PlanCuenta",
    "Clientes",
    "Proveedores",
    "TipoDocumento",
    "TipoSociedad",
    "TipoTercero"
]