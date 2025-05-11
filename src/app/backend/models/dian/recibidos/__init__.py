# backend/models/dian/recibidos/__init__.py
# Modelos relacionados con el modulo documentos recibidos de la Dian.

from .factura_compra_xml import FacturaCompraXml
from .factura_compra import FacturaCompra
from .informe_recibidos import InformeRecibidos
from .nota_credito_xml import NotaCreditoXml
from .nota_credito import NotaCredito

# Definimos los modelos que serán importados por otros módulos o archivos.
__all__ = [
    "FacturaCompraXml",
    "FacturaCompra",
    "InformeRecibidos",
    "NotaCreditoXml",
    "NotaCredito"
]