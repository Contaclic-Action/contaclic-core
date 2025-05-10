             
#                     💻 **Contaclic Action – Plataforma Contable y Tributaria** 🚀.
 

Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---

## 🧠 * Tecnologías *

| Tecnología              | Descripción                                |
| --------------------    |-------------------------------------       |
| Python 3.10+            | Backend con FastAPI + SQLAlchemy           |
| PostgreSQL              | Base de datos                              |
| React / Next.js 14+     | Frontend visual                            |
| Tailwind CSS            | Estilos rápidos y modernos                 |
| React Query             | Manejo de peticiones y estado              |
| Redis                   | Mensajería y almacenamiento en caché       |
| Power BI                | Visualización datos y paneles interactivos |
| Pydantic V2             | Validación robusta (backend)               |


---

# 🗂️ Estructura general


📁 `contaclic_core/`

### ├── 📦 backend/   Backend con FastAPI (API REST, lógica de negocio, base de datos, automatizaciones)
### └── 💻 frontend/  Frontend moderno en Next.js (interfaz de usuario para clientes y administrativos)

---

### 📁 `backend/`


# 👋 Bienvenido al backend de Contaclic Action

Este sistema ha sido desarrollado para automatizar y gestionar de forma eficiente, modular y escalable toda la información tributaria, contable y documental de tu empresa, tanto a nivel nacional como municipal.

Aquí encontrarás:

### 🧩 Todos los módulos funcionales del sistema (tributación, facturación, bancos, etc.).

### ⚙️ Detalles técnicos de su estructura, lógica de negocio y herramientas integradas.

### 🚀 Mejoras continuas orientadas a rendimiento, usabilidad y escalabilidad.


Este backend es el núcleo que conecta procesos clave de tu operación contable con automatizaciones inteligentes y una visión clara del estado financiero.

---

###  ⚙️ `Cómo iniciar/`


 ## 📌 CONEXION PgAdmin 4 y Render.

1. 💾 Host: Es la URL o IP de la base de datos.(Ej: dpg-xxxxxxx.render.com) - PSQL Command.
2. 💾 Port: generalmente 5432 (el puerto estándar de PostgreSQL).
3. 💾 Maintenance Database: suele ser el nombre de la base de datos principal que creaste en Render.
4. 💾 Username (Role): Es el nombre que configuraste o te asignó Render ( "DATABASE USER").
5. 💾 Password: la contraseña del usuario de base de datos.
6. 💾 Service: este campo no es obligatorio en pgAdmin. 

## 🧹 Gestión del Entorno Virtual y Dependencias

1. ▶️ Eliminar el Entorno Virtual Antiguo (Limpieza):
### 📥 Remove-Item -Path .venv -Recurse -Force   ➡️ Si la carpeta se llama .venv
2. ▶️ Crear un Nuevo Entorno Virtual:
### 📥 python -m venv .venv                      ➡️  Esto crea una nueva carpeta '.venv'
3. ▶️ Activar el Nuevo Entorno Virtual:         
### 📥 .\.venv\Scripts\activate                  ➡️  Si la carpeta se llama .venv
4. ▶️ Verificar listado en la raiz del proyecto. Instalar las Dependencias:
### 📥 pip install -r requirements.txt
5. ▶️ Para verificar todas las librerías instaladas específicamente en ese entorno.
### 📥 pip freeze                                ➡️  Muestra el contenido de requirements.txt.

---

                    
#                     🏗️ RESUMEN ESTRUCTURA - BACKEND


### 💼 backend/	                       -   Contiene la app principal, routers registrados, CORS.
└──📝 backend/main.py	               -   Archivo principal que levanta la API

### 💼backend/bot/	                   -   Bot de Telegram con Python. "usuario automático".
└── 🗂️ backend/bot/main.py	            -   Punto de entrada principal.
── 🗂️ backend/bot/handlers/	        -   Manejadores de comandos.
── 🗂️ backend/bot/middlewares/         -   Hacer logs por usuario, o limitar por roles, etc.
── 🗂️ backend/bot/services/	        -   Conexión con backend.

### 💼 backend/clientes/	           -   Libreto de operaciones.
└── 🗂️ backend/cliente/bancos/         -   Operaciones bancarias.
── 🗂️ backend/cliente/recibidos/       -   Modulo recibido Dian. Todo sobre compras.
── 🗂️ backend/cliente/terceros/	    -   Manejo de usuarios y terceros.

### 💼 backend/contabilidad/	        -   Lógica de negocio central
└── 🗂️ backend/contabilidad/models/	 -   Modelos de datos
── 🗂️ backend/contabilidad/routers/     -   Endpoints (listar, crear, actualizar, etc.)
── 🗂️ backend/contabilidad/schemas/     -   Esquemas expuestos en API

### 💼 backend/core/	                -   Configuraciones de la app
└── 📝 /core/config.py	                -   Gestiona la configuración externa.

### 💼 backend/database/	            -   Configuracion de la base de datos.  
└── 📝 /database/connection.py	        -   Logica de conexion a PostgreSQL usando SQLAlchemy.

### 💼 backend/integrations/            -   Módulo unificado para integraciones
└── 🗂️ backend/integrations/auth/       -   Autenticación y tokens

### 💼 backend/models/	                -   Modelos SQLAlchemy para representar las tablas. 
└── 🗂️ backend/models/registro/	     -   Modelos geograficos para crear terceros.
── 🗂️ backend/models/dian/	             -   Conciliacion modulo Dian.
── 🗂️ backend/models/bancos/	         -   Conciciliacion de extractos bancarios.

### 💼 backend/routers/	                -   Carpeta general de endpoints FastAPI organizados por dominio.
└── 🗂️ backend/routers/registro/   
── 🗂️ backend/routers/dian/
── 🗂️ backend/routers/bancos/

### 💼 backend/schemas/	                -  Aqui defines los esquemas de entrada/salida (Pydantic) 
└── 🗂️ backend/schemas/bancos/	         -  Conciciliacion de extractos bancarios.
── 🗂️ backend/schemas/registro/	     -  Esquema geograficos para crear terceros.  
── 🗂️ backend/schemas/dian/	         -  Conciliacion modulo Dian.   

### 💼 backend/services/                -  Divide lógica de negocio de forma clara y coherente.
└── 🗂️ backend/services/bancos/	     -  Operaciones bancarias
── 🗂️ backend/services/registro/        -  Encapsula toda la lógica, terceros, geográficos, etc.
── 🗂️ backend/services/dian/	         -  Interacción con los datos regulados por la DIAN.

### 💼 backend/tests/	                -  Es la raíz de la pruebas automáticas
└── 🗂️ backend/tests/clientes/          -  Dependencias comunes de la API
── 🗂️ backend/tests/models/             -  Modelos de datos
── 🗂️ backend/tests/database/           -  Esquemas para validación/serialización API

### 💼 backend/uploads/	                -  Para guardar temporalmente los archivos (CSV, PDF, XML).
└── 🗂️ backend/uploads/	bancos/YYYY/
── 🗂️ backend/uploads/	terceros/YYYY/
── 🗂️ backend/uploads/	emitidos/YYYY/

### 💼 backend/utils/	                -  Funciones pequenas y sin conexion a la base de datos.
└── 🗂️ backend/utils/archivos/pdf/	     -  Funciones para leer PDFs.
── 🗂️ backend/utils/archivos/csv/	     -  Validaciones CSV regitros de empresas y personas naturales.
── 🗂️ backend/utils/archivos/xml/	     -  XML

---

##                   🛠️ Framework y Servidor


└── ✅ fastapi==0.115.8            - Framework web moderno para construir APIs
── ✅ uvicorn==0.34.0             - Servidor ASGI para ejecutar FastAPI

### 🗂️ ORM y Base de Datos (elige uno de los dos drivers para PostgreSQL)
└── ✅ SQLAlchemy==2.0.38          - ORM para bases de datos relacionales
── ✅ asyncpg==0.30.0             - Driver asíncrono para PostgreSQL (recomendado)
── ✅ psycopg2-binary==2.9.10     - Alternativa sincrónica (no necesaria si usas asyncpg)

### 🛡️ Validación y Configuración
└── ✅ pydantic==2.10.6            - Validación de datos con anotaciones de tipo
── ✅ python-dotenv==1.1.0        - Carga de variables desde .env

###  💼 Herramientas de desarrollo
└── ✅ black==25.1.0               - Formateador automático de código
── ✅ colorama==0.4.6             - Colores en terminal (útil para logs en Windows)

###  🧩 Tareas asíncronas (solo si usas Celery)
└── ✅ celery==5.5.2               - Cola de tareas para trabajos en segundo plano
── ✅ redis==5.2.1                - Broker de mensajes para Celery

###  🛠️ OCR e imágenes
└──✅ easyocr==1.7.2              - Reconocimiento de texto en imágenes

###  🛠️ PDFs y texto
└── ✅ pdfplumber==0.11.6          - Extrae texto y tablas de PDFs
── ✅ PyMuPDF==1.25.4             - Lectura y edición de PDFs

###  📊 Procesamiento de datos
└── ✅ pandas==2.2.3               - Análisis y manipulación de datos tabulares
── ✅ numpy==2.2.5                - Cálculo numérico (requerido por pandas)
── ✅ openpyxl==3.1.5             - Lectura y escritura de archivos Excel

### 📄 XML
└── ✅ xmlschema==3.2.1            - Validación y lectura de archivos XML con XSD

---

 ##                🔗  Conexión de proyecto local a GitHub

### ✅ 1. Crea un archivo .gitignore en la raíz del proyecto.

Incluye rutas comunes para ignorar archivos innecesarios:

### ⚙️.gitignore
└──📁 .venv/
──📁 node_modules/
──🛠️ __pycache__/
──📁.env
──🛠️* .log
──🛠️* .sqlite3
──📁.next/
──🛠️ dist/
──🛠️ .vscode/
──🛠️ .idea/

### ✅ 2. Inicializar el repositorio local - Si tu proyecto aún no está conectado a Git:
└── 🐍 git init
### ✅ 3. Agrega el repositorio remoto - Esto vincula tu proyecto local al repositorio de GitHub:
└── 🐍 git remote add origin https://github.com/tu_usuario/tu_repositorio.git
### ✅ 4. Crea y muévete a la rama principal main.
└── 🐍 git checkout -b main
### ✅ 5. Añade los archivos y haz tu primer commit - Preparar archivos para subir
└── 🐍 git add .
──  🐍 git commit -m "Primer commit "
### ✅ 6. Sube tu código a GitHub -  Si tu rama local se llama main, haz:
└── 🐍 git push -u origin main

### ⚠️ Si da error porque el repositorio remoto ya contiene archivos:
└── 🐍git push -u origin main --force

---

# 📄 Subir o actualizar el archivo README.md

### ✅ 1. Verifica que el archivo está presente.
└── 🐍 git status
### ✅ 2. Agrega el archivo README.md al staging.
└── 🐍 git add README.md
### ✅ 3. Realiza un commit con un mensaje descriptivo.
└── 🐍 git commit -m "Agregar o actualizar README.md"
### ✅ 4. Sube los cambios al repositorio en GitHub.
└── 🐍 git push origin main


# 💻 Confirmar en GitHub

### └── ✅ README.md se muestra como descripción principal del repositorio.
### ── ⚙️ .gitignore, requirements.txt y demás archivos son visibles.
### ── ✅ La rama principal aparece como main.

---

#                🧠 **Estructura de archivos __init__.py**

## 📁 Carpetas de modelos (models/)  

### 🎯 Importamos las clases de los modelos que queremos exponer
`from .archivo_1 import Clase1`
`from .archivo_2 import Clase2`

###  🔹Controlamos qué se puede importar desde fuera
`__all__ = ["Clase1", "Clase2"]`


##  📁 Carpetas de routers (routers/)

###  🎯 Importamos los routers definidos en otros archivos
`from .recurso_1 import router as recurso_1_router`
`from .recurso_2 import router as recurso_2_router`

###  🔹Listamos los routers para facilitar su uso desde main.py o routers principales

` __all__ = ["recurso_1_router", "recurso_2_router"]`

##  📁 Carpetas de esquemas (schemas/)

###  🎯 Importamos los esquemas base, create, update, etc.
`from .archivo_1 import Clase1Base, Clase1Create`
`from .archivo_2 import Clase2Base, Clase2Create`

###  🔹Indicamos explícitamente qué exportamos

`__all__ = ["Clase1Base", "Clase1Create", "Clase2Base", "Clase2Create"]`


## 📁 Carpetas de servicios (services/)

###  🎯 Importamos funciones o clases que contienen la lógica del negocio
`from .recurso_1 import funcion_1`
`from .recurso_2 import clase_servicio`

###  🔹Exportamos solo lo necesario

`__all__ = ["funcion_1", "clase_servicio"]`


## 📁 Carpetas de utilidades (utils/)

###  🎯 Importamos funciones específicas de procesamiento PDF
`from .lector_pdf import extraer_texto`
`from .validador_pdf import validar_formato`

###  🔹Dejamos claro qué funciones queremos que estén disponibles

`__all__ = ["extraer_texto", "validar_formato"]`


## ❌ Carpetas que no necesitan __init__.py

└── 📁 Carpetas de uploads - solo para guardar archivos temporales.
── 📁 Carpetas de tests - si no planeas importar sus módulos desde fuera.
── 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.
           
---

#                       📋 PROCESO CREACION DE TABLAS

## ✅ .env

DATABASE_URL=postgresql://usuario:contrasena@host:puerto/basededatos

## ✅ database/connection.py

🔄 Usa python-dotenv para cargar la variable del .env:

### `from sqlalchemy import create_engine`
### `from sqlalchemy.orm import sessionmaker`
### `from backend.database.base_class import Base`
### `from dotenv import load_dotenv`
### `import os`

###   `load_dotenv()` - Cargar variables del .env

###   `DATABASE_URL = os.getenv("DATABASE_URL")`

###   `engine = create_engine(DATABASE_URL)`
###   `SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)`

### `def get_db():`
###     `db = SessionLocal()`
###    `try:`
###        `yield db`
###     `finally:`
###         `db.close()`

## ✅ DATABASE / base_class.py

`from sqlalchemy.ext.declarative import declarative_base`
`Base = declarative_base()`

## ✅ DATABASE / __init__.py

`from .connection import engine, SessionLocal, get_db`
`from .base_class import Base`

## DATABASE / create_tables.py

`from backend.database.connection import engine`
`from backend.database.base_class import Base`   
`from backend.models import *`  

`def create_all_tables():`                 
     `Base.metadata.create_all(bind=engine)`  

`if __name__ == "__main__":`                   
`print("✅ Tablas creadas exitosamente.")`
`create_all_tables()`

## ✅ MODELOS - models

`from sqlalchemy import Column, Integer, String`
`from backend.database.base_class import Base`

`class Tercero(Base):`
`__tablename__ = "terceros"`

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    identificacion = Column(String, unique=True, index=True)
    direccion = Column(String)

## ✅ MODELS /__init__.py

`from .terceros import Tercero`
`__all__ = [`
`"Tercero",`
` ]`

## ✅ ESQUEMAS - schemas

`from pydantic import BaseModel`
`class TerceroBase(BaseModel):`
`nombre: str`
`identificacion: str`
`direccion: str`
`class TerceroCreate(TerceroBase):`
` pass`
`class Tercero(TerceroBase):`
`id: int`
`class Config:`
`from_attributes = True`

## ✅ ESQUEMAS / __init__.py

`from .terceros import Tercero, TerceroCreate, TerceroBase`

## ✅ ROUTERS - routers 

`from fastapi import APIRouter, HTTPException, Depends`
`from sqlalchemy.orm import Session`
`from backend.schemas.tercero import TerceroCreate, Tercero`
`from backend.models.tercero import Tercero as DBTercero`
`from backend.database import get_db`

### router = APIRouter()

`@router.post("/terceros", response_model=Tercero)`
`def crear_tercero(tercero: TerceroCreate, db: Session = Depends(get_db)):`
   `existente = db.query(DBTercero).filter(DBTercero.identificacion == tercero.identificacion).first()`
     `if existente:`
         `raise HTTPException(status_code=400, detail="⚠️ El tercero ya esta registrado.")`

    nuevo_tercero = DBTercero(**tercero.dict())
    db.add(nuevo_tercero)
    db.commit()
    db.refresh(nuevo_tercero)
    return nuevo_tercero

 `@router.get("/terceros/{tercero_id}", response_model=Tercero)`
 `def get_tercero(tercero_id: int, db: Session = Depends(get_db)):`
     `db_tercero = db.query(DBTercero).filter(DBTercero.id == tercero_id).first()`
     `if db_tercero is None:`
         `raise HTTPException(status_code=404, detail="Tercero not found")`
     `return db_tercero`

## ✅ ROUTERS / __init__.py

`from .terceros import router as terceros_router`

## ✅ MAIN.PY - Integracion de los Endpoints  

`from fastapi import FastAPI`
`from fastapi.middleware.cors import CORSMiddleware`
`from backend.routers import terceros  # importa tu router`

`app = FastAPI()`

 `🔐 CORS middleware`
 `app.add_middleware(`
     `CORSMiddleware,`
     `allow_origins=["http://localhost:3000"],  # puedes poner "*" si estás en desarrollo`
     `allow_credentials=True,`
     `allow_methods=["*"],`
     `allow_headers=["*"],`
 `)`

## ✅ Incluye tus routers con prefijo /api

`app.include_router(terceros.router, prefix="/api")`

## ✅ "Crear tablas:" python -m backend.db.create_tables


### 📁 Explicación de la organización:

### 📁 database/ - Conexion a la base de datos. Aqui generalmente se encuentra:
└──🔹El motor de conexion (engine).
──🔹La sesion (SessionLocal).
──🔹El archivo create_tables.py para inicializar las tablas a partir de los modelos.

### 📁 models/ - Define las clases de SQLAlchemy que representan tus tablas en la base de datos. Cada clase equivale a una tabla y define sus campos, relaciones y restricciones.

### 📁 schemas/ - Contiene las clases de Pydantic, utilizadas para:
└──🔹Validar los datos de entrada y salida de la API.
──🔹Separar los modelos internos de la base de datos de las estructuras que se exponen al cliente.
──🔹Esto mejora la seguridad y mantiene el codigo desacoplado.

### 📁 routers/ - Endpoints de la API agrupados por funcionalidad. Cada archivo corresponde a un recurso o entidad y contiene:
└──🔹Las rutas (@router.get, @router.post, etc.).
──🔹La logica de interaccion entre los schemas y los modelos.

### ⚙️ __init__.py en cada carpeta - Este archivo hace que la carpeta sea reconocida como un paquete de Python y permite importaciones limpias entre modulos. Ayuda a mantener una estructura modular y organizada.

### 📝 main.py - Es el punto de entrada de la aplicacion FastAPI. Aqui se:
└──🔹Crea la instancia principal de la app (app = FastAPI()).
──🔹Se agregan middlewares (como CORS).
──🔹Se incluyen los routers definidos en routers/.
──🔹Se levanta el servidor si se ejecuta directamente.
──🔹Beneficios de esta Estructura.

---

#                    🧱 Ventajas de esta Arquitectura.

## 🧠 Separacion clara de responsabilidades.
Cada capa del proyecto (modelos, esquemas, routers, base de datos) tiene una funcion bien definida, lo que facilita el entendimiento del sistema y promueve buenas practicas de desarrollo.

## 📈 Escalabilidad
La estructura modular permite agregar nuevos recursos de forma sencilla. Solo necesitas crear el modelo, el esquema y el router correspondiente sin afectar otras partes de la aplicacion.

## 🔧 Mantenibilidad
Las capas estan desacopladas. Por lo tanto, hacer cambios en una (por ejemplo, en los modelos o esquemas) requiere pocas o ninguna modificacion en el resto del codigo.

## 🧪 Testabilidad
Cada componente (modelo, ruta, logica) puede ser probado de forma aislada, lo que facilita la escritura de pruebas unitarias y mejora la calidad del codigo.

## 🧩 Consistencia
El uso de un patron uniforme en toda la aplicacion reduce errores, facilita la colaboracion en equipo y mejora la experiencia de desarrollo a largo plazo.


## 🚧 Estado del proyecto

 ### ☑️ Backend funcional.
 ### ⬜ Servicios de validación de terceros
 ### ⬜ Procesamiento de archivos (XML, PDF).
 ### ⬜ Frontend visual con Next.js.
 ### ⬜ Integraciones.

 ## 👨‍💼 Autor
 Yecid – GitHub | Contaclic.com (contaclic.co)

 ## ⚖️ Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más información.
