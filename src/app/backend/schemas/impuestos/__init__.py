# importar las clases de los módulos correspondientes
from .municipal_ica import Clase1Basica, Clase2Basica, Clase3Basica, Clase4Basica
from .nacional import Clase1Nacional, Clase2Nacional, Clase3Nacional, Clase4Nacional

#exportamos las clases para que puedan ser importadas desde el paquete
__all__ = [
    "Clase1Basica",
    "Clase2Basica",
    "Clase3Basica",
    "Clase4Basica",
    "Clase1Nacional",
    "Clase2Nacional",
    "Clase3Nacional",
    "Clase4Nacional"
]