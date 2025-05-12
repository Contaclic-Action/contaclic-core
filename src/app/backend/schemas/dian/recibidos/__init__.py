# importar las clases de los módulos correspondientes
import .factura_compra import (
    FacturaCompraBase,
    FacturaCompraCreate,
    FacturaCompraUpdate,
    FacturaCompraInDBBase,
    FacturaCompraInDB,
)   
from .factura_compra_xml import (
    FacturaCompraXMLBase,
    FacturaCompraXMLCreate,
    FacturaCompraXMLUpdate,
    FacturaCompraXMLInDBBase,
    FacturaCompraXMLInDB,
)
from .informe_recibidos import (
    InformeRecibidosBase,
    InformeRecibidosCreate,
    InformeRecibidosUpdate,
    InformeRecibidosInDBBase,
    InformeRecibidosInDB,
)   
from .nota_credito_xml import (
    NotaCreditoXMLBase,
    NotaCreditoXMLCreate,
    NotaCreditoXMLUpdate,
    NotaCreditoXMLInDBBase,
    NotaCreditoXMLInDB,
)
from .nota_credito import (
    NotaCreditoBase,
    NotaCreditoCreate,
    NotaCreditoUpdate,
    NotaCreditoInDBBase,
    NotaCreditoInDB,
)

# exportar las clases para que puedan ser importadas desde el módulo padre
__all__ = [
    "FacturaCompraBase",
    "FacturaCompraCreate",
    "FacturaCompraUpdate",
    "FacturaCompraInDBBase",
    "FacturaCompraInDB",
    "FacturaCompraXMLBase",
    "FacturaCompraXMLCreate",
    "FacturaCompraXMLUpdate",
    "FacturaCompraXMLInDBBase",
    "FacturaCompraXMLInDB",
    "InformeRecibidosBase",
    "InformeRecibidosCreate",
    "InformeRecibidosUpdate",
    "InformeRecibidosInDBBase",
    "InformeRecibidosInDB",
    "NotaCreditoXMLBase",
    "NotaCreditoXMLCreate",
    "NotaCreditoXMLUpdate",
    "NotaCreditoXMLInDBBase",
    "NotaCreditoXMLInDB",
    "NotaCreditoBase",
    "NotaCreditoCreate",
    "NotaCreditoUpdate",
    "NotaCreditoInDBBase",
    "NotaCreditoInDB"
]   
