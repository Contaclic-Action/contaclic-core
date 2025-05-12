# Importamos los schemas de los registros de métodos de pago
from .bancos_virtuales import ClaseBancosVirtualesBase, ClaseBancosVirtualesCreate, ClaseBancosVirtualesUpdate
from .bancos import ClaseBancosBase, ClaseBancosCreate, ClaseBancosUpdate
from .tipo_banco import ClaseTipoBancoBase, ClaseTipoBancoCreate, ClaseTipoBancoUpdate

# Exportamos las clases para que puedan ser importadas desde el paquete
__all__ = [
    "ClaseBancosVirtualesBase",
    "ClaseBancosVirtualesCreate",
    "ClaseBancosVirtualesUpdate",
    "ClaseBancosBase",
    "ClaseBancosCreate",
    "ClaseBancosUpdate",
    "ClaseTipoBancoBase",
    "ClaseTipoBancoCreate",
    "ClaseTipoBancoUpdate"
]