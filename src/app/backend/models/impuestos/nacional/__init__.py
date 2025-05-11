# backend/models/impuestos/nacional/__init__.py
# Modelo tributarios nacional compartidos entre modulo.

from .rendimientos_financieros import RendimientosFinancieros
from .responsabilidad_dian import ResponsabilidadDian
from .retencion_2025 import Retencion2025
from .autorretenedores_renta import AutorretenedoresRenta
from .grandes_contribuyentes import GrandesContribuyentes

# Definimos los modelos que serán importados por otros módulos o archivos.
__all__ = [
    "RendimientosFinancieros",
    "ResponsabilidadDian",
    "Retencion2025",
    "AutorretenedoresRenta",
    "GrandesContribuyentes",
]