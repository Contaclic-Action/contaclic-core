### ⚙️ ```__init__.py```

Este archivo permite que una carpeta sea reconocida como un paquete de Python, facilitando las importaciones limpias entre módulos del proyecto.
Es clave para mantener una estructura modular y organizada, especialmente en proyectos grandes como este.


## 🧠 **Estructura de archivos `__init__.py`**

### 🗂️ DATABASE / `__init__.py`

 ```from .connection import engine, SessionLocal, get_db```
 ```from .base_class import Base```

- **engine**: Conexión principal a PostgreSQL.
- **SessionLocal**: Sesión de base de datos para operaciones CRUD.
- **get_db**: Dependencia para inyección de sesión en FastAPI.
- **Base**: Clase base para heredar en todos los modelos.


### 📁 MODELS / `__init__.py` 

- 🎯 Importamos las clases de los modelos que queremos exponer.

- ```from .archivo_1 import Clase1```
- ```from .archivo_2 import Clase2```

-  Controlamos qué se puede importar desde fuera.

- ```__all__ = ["Clase1", "Clase2"]```

---

###  📁 Carpetas de routers (routers/)

-  🎯 Importamos los routers definidos en otros archivos.

- ```from .recurso_1 import router as recurso_1_router```
- ```from .recurso_2 import router as recurso_2_router```

-  Listamos los routers para facilitar su uso desde main.py o routers principales.

- ``` __all__ = ["recurso_1_router", "recurso_2_router"]```

---

###  📁 Carpetas de esquemas (schemas/)

-  🎯 Importamos los esquemas base, create, update, etc.

`from .archivo_1 import Clase1Base, Clase1Create, Clase1Update`
`from .archivo_2 import Clase2Base, Clase2Create, Clase1Update`

-  Indicamos explícitamente qué exportamos.

`__all__ = ["Clase1Base", "Clase1Create", "Clase1Update" "Clase2Base", "Clase2Create" "Clase2Update"]`

---

### 📁 Carpetas de servicios (services/)

-  🎯 Importamos funciones o clases que contienen la lógica del negocio.

`from .recurso_1 import funcion_1`
`from .recurso_2 import clase_servicio`

-  Exportamos solo lo necesario.

`__all__ = ["funcion_1", "clase_servicio"]`

---

### 📁 Carpetas de utilidades (utils/)

-  🎯 Importamos funciones específicas de procesamiento PDF.

`from .lector_pdf import extraer_texto`
`from .validador_pdf import validar_formato`

-  Dejamos claro qué funciones queremos que estén disponibles.

`__all__ = ["extraer_texto", "validar_formato"]`




- ❌ Carpetas que no necesitan `__init__.py`

- 📁 Carpetas de uploads - solo para guardar archivos temporales.
- 📁 Carpetas de tests - si no planeas importar módulos desde fuera.
- 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.