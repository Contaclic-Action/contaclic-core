# Guía para Contribuir

Gracias por tu interés en contribuir. Este documento establece un flujo de trabajo claro y estandarizado para mantener la calidad del código en **Contaclic Action**.

---

## 🧠  Tecnologías

- Python 3.11+
- FastAPI
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions
- Pytest
- Pydantic V2 – validación robusta de datos
- Redis – cache y mensajería

---

##                🔗  Conexión de proyecto local a GitHub

### ✅ 1. Crea un archivo .gitignore en la raíz del proyecto.

Incluye rutas comunes para ignorar archivos innecesarios:

- ┣  ⚙️.gitignore
- ┣ 📁 .venv/
- ┣ 📁 node_modules/
- ┣ 🛠️ __pycache__/
- ┣ 📁.env
- ┣ 🛠️* .log
- ┣ 🛠️* .sqlite3
- ┣ 📁.next/
- ┣ 🛠️ dist/
- ┣ 🛠️ .vscode/
- ┣ 🛠️ .idea/

2. Inicializar el repositorio local - Si tu proyecto aún no está conectado a Git:
-  `git init`
3. Agrega el repositorio remoto - Esto vincula tu proyecto local al repositorio de GitHub:
-  `git remote add origin https://github.com/tu_usuario/tu_repositorio.git`
4. Crea y muévete a la rama principal main.
-  `git checkout -b main`
5. Añade los archivos y haz tu primer commit - Preparar archivos para subir
-  `git add .`
-  `git commit -m "Primer commit "`
6. Sube tu código a GitHub -  Si tu rama local se llama main, haz:
-  `git push -u origin main`

### ⚠️ Si da error porque el repositorio remoto ya contiene archivos:
-  `git push -u origin main --force`

---

# 📄 Subir o actualizar el archivo README.md

1. Verifica que el archivo está presente.
-  `git status`
2. Agrega el archivo README.md al staging.
-  `git add README.md`
3. Realiza un commit con un mensaje descriptivo.
-  `git commit -m "Agregar o actualizar README.md"`
4. Sube los cambios al repositorio en GitHub.
-  `git push origin main`


## 💻 Confirmar en GitHub.


- ✅ README.md se muestra como descripción principal del repositorio.
- ⚙️ .gitignore, requirements.txt y demás archivos son visibles.
- ✅ La rama principal aparece como main.

---

## 🛠️ Configuración local

1.  Clona el repositorio: https://github.com/Contaclic-Action/contaclic-core.git 

2.  Entorno virtual 

    `python -m venv .venv`
    `source .venv/bin/activate`  - Linux/macOS
    `.venv\Scripts\activate`     - Windows

3. Instalar dependencias

 `pip install -r requirements.txt`

4. Levantar entorno con Docker

 `docker-compose up --build`


### 🧪 Correr pruebas

 `pytest src/tests`

✅ Usa pytest-cov para cobertura:

 `pytest --cov=src/app src/tests` - Para cobertura


📌 Las pruebas están organizadas en src/tests/. Se utiliza pytest para cobertura y ejecución.

---

## 🔀 Flujo de trabajo (Git)

- Usa `main` solo para código listo para producción.

- Trabaja en ramas separadas:

🔹feat/ → nueva funcionalidad
🔹fix/ → corrección de bug
🔹refactor/ → cambios internos sin alterar funcionalidad
🔹test/ → pruebas
🔹docs/ → documentación
🔹chore/ → tareas de mantenimiento

### 💬 Estilo de Commit

Usamos Conventional Commits:

- `feat: nombre de funcionalidad`
- `fix: corrección de error`
- `docs: cambios de documentación`
- `test: pruebas nuevas o corregidas`

---

### 📚 Documentación

Documentación general está en docs/

Endpoints autodocumentados con FastAPI Swagger:

  `http://localhost:8000/docs`

---

## 🧩 ¿Cómo reportar un error o sugerir una mejora?

Usa la pestaña `Issues` en GitHub para reportar errores, sugerencias o mejoras.

Si vas a enviar un `Pull Request`:
- Crea una rama (`feat/nueva-funcionalidad`)
- Asegúrate de que todos los tests pasen
- Describe claramente qué hace el cambio


## 🔎 Revisión de código

Antes de subir tu código:

- Ejecuta los tests: `pytest src/tests`.
- Verifica que todo compile sin errores.
- Usa nombres claros en variables y funciones.

---

### 🤝 Código de conducta

Este proyecto tiene un [Código de Conducta](./CODE_OF_CONDUCT.md). Por favor, sé respetuoso y constructivo con otros colaboradores.

###  ⚙️ `Cómo iniciar/`

---

 ## 📌 CONEXION PgAdmin 4 y Render.

1. Host: Es la URL o IP de la base de datos.(Ej: dpg-xxxxxxx.render.com) - PSQL Command.
2. Port: generalmente 5432 (el puerto estándar de PostgreSQL).
3. Maintenance Database: suele ser el nombre de la base de datos principal que creaste en Render.
4. Username (Role): Es el nombre que configuraste o te asignó Render ( "DATABASE USER").
5. Password: la contraseña del usuario de base de datos.
6. Service: este campo no es obligatorio en pgAdmin. 

## 🧹 Gestión del Entorno Virtual y Dependencias

▶️ Eliminar el Entorno Virtual Antiguo (Limpieza):
📥 `Remove-Item -Path .venv -Recurse -Force`   ➡️ Si la carpeta se llama .venv
▶️ Crear un Nuevo Entorno Virtual:
📥 `python -m venv .venv`                      ➡️  Esto crea una nueva carpeta '.venv'
▶️ Activar el Nuevo Entorno Virtual:         
📥 `.\.venv\Scripts\activate`                  ➡️  Si la carpeta se llama .venv
▶️ Verificar listado en la raiz del proyecto. Instalar las Dependencias:
📥 `pip install -r requirements.txt`
▶️ Para verificar todas las librerías instaladas específicamente en ese entorno.
📥 `pip freeze`                                ➡️  Muestra el contenido de requirements.txt.

---

#                     🏗️ RESUMEN ESTRUCTURA 

### ├── 📂 .github/                 - Workflows de GitHub Actions (CI/CD).
-       ├── 📝 ci.yml               - CI principal (test/lint).
-       └── 📝 workflows            - Pruebas o despliegue automático.
### ├── 📂 .venv/                   - Entorno virtual local (no se sube a Git).
### ├── 📂 docs/                    - Documentación general o técnica.
-       ├── 🐳 Dockerfile           - Build para producción.
-       └── 🐳 docker-compose.yml   - Servicios acoplados.
### ├── 📂 infrastructure/          - Archivos para despliegue (Dockerfile, docker-compose).
### ├── 📂 src/                     - Código fuente principal.
-       ├── 📂 tests/               - Pruebas automatizadas.
-       └── 📂 app/                 - Módulo principal.          
-           └── 📂 backend/         - Backend FastAPI (rutas, modelos, servicios, etc.).
### ├── ⚙️ .gitignore               - Para excluir archivos temporales.
### ├── 📝 CHANGELOG.md             - Historial de cambios.
### ├── 📝 CODE_OF_CONDUCT.md       - Reglas de comportamiento.
### ├── 📄 CONTRIBUTING.md          - Guía para colaboradores.
### ├── 📄 LICENSE                  - Tipo de licencia.
### ├── 📄 README.md                - Descripción del proyecto.
### ├── 📄 requirements.txt         - Dependencias de producción.
### └── 🔒 SECURITY.md              - Cómo reportar vulnerabilidades.

# 🏛️ BACKEND

-   💼 backend/	                        -   Contiene la app principal, routers registrados, CORS.
└── 📄 backend/main.py	                -   Archivo principal que levanta la API
-   💼backend/bot/	                    -   Bot de Telegram con Python. "usuario automático".
└── 🗂️ backend/bot/main.py	             -   Punto de entrada principal.
─── 🗂️ backend/bot/handlers/	         -   Manejadores de comandos.
─── 🗂️ backend/bot/middlewares/         -   Hacer logs por usuario, o limitar por roles, etc.
──│ 🗂️ backend/bot/services/	         -   Conexión con backend.
-   💼 backend/clientes/	            -   Libreto de operaciones.
└── 🗂️ backend/cliente/bancos/          -   Operaciones bancarias.
─── 🗂️ backend/cliente/recibidos/       -   Modulo recibido Dian. Todo sobre compras.
──│ 🗂️ backend/cliente/terceros/	     -   Manejo de usuarios y terceros.
-   💼 backend/contabilidad/	        -   Lógica de negocio central
└── 🗂️ backend/contabilidad/models/	 -   Modelos de datos
─── 🗂️ backend/contabilidad/routers/    -   Endpoints (listar, crear, actualizar, etc.)
──│ 🗂️ backend/contabilidad/schemas/    -   Esquemas expuestos en API
-   💼 backend/core/	                -   Configuraciones de la app
└── 📄 /core/config.py	                -   Gestiona la configuración externa.
-   💼 backend/database/	            -   Configuracion de la base de datos.  
└── 📄 /database/connection.py	        -   Logica de conexion a PostgreSQL usando SQLAlchemy.
-   💼 backend/integrations/            -   Módulo unificado para integraciones
└── 🗂️ backend/integrations/auth/       -   Autenticación y tokens
-   💼 backend/models/	                -   Modelos SQLAlchemy para representar las tablas. 
└── 🗂️ backend/models/registro/	     -   Modelos geograficos para crear terceros.
─── 🗂️ backend/models/dian/	             -   Conciliacion modulo Dian.
──│ 🗂️ backend/models/bancos/	         -   Conciciliacion de extractos bancarios.
-   💼 backend/routers/	                -   Carpeta general de endpoints FastAPI organizados por dominio.
└── 🗂️ backend/routers/registro/   
─── 🗂️ backend/routers/dian/
──│ 🗂️ backend/routers/bancos/
-   💼 backend/schemas/	                -  Aqui defines los esquemas de entrada/salida (Pydantic) 
└── 🗂️ backend/schemas/bancos/	         -  Conciciliacion de extractos bancarios.
─── 🗂️ backend/schemas/registro/	     -  Esquema geograficos para crear terceros.  
──│ 🗂️ backend/schemas/dian/	         -  Conciliacion modulo Dian.   
-   💼 backend/services/                -  Divide lógica de negocio de forma clara y coherente.
└── 🗂️ backend/services/bancos/	     -  Operaciones bancarias
─── 🗂️ backend/services/registro/       -  Encapsula toda la lógica, terceros, geográficos, etc.
──│ 🗂️ backend/services/dian/	         -  Interacción con los datos regulados por la DIAN.
-   💼 backend/tests/	                -  Es la raíz de la pruebas automáticas
└── 🗂️ backend/tests/clientes/          -  Dependencias comunes de la API
─── 🗂️ backend/tests/models/            -  Modelos de datos
──│ 🗂️ backend/tests/database/          -  Esquemas para validación/serialización API
-   💼 backend/uploads/	                -  Para guardar temporalmente los archivos (CSV, PDF, XML).
└── 🗂️ backend/uploads/	bancos/YYYY/
─── 🗂️ backend/uploads/	terceros/YYYY/
──│ 🗂️ backend/uploads/	emitidos/YYYY/
-   💼 backend/utils/	                -  Funciones pequenas y sin conexion a la base de datos.
└── 🗂️ backend/utils/archivos/pdf/	     -  Funciones para leer PDFs.
─── 🗂️ backend/utils/archivos/csv/	     -  Validaciones CSV regitros de empresas y personas naturales.
──│ 🗂️ backend/utils/archivos/xml/	     -  XML

---

##                       📋 PROCESO CREACION DE TABLAS

### ✅ .env

DATABASE_URL=postgresql://usuario:contrasena@host:puerto/basededatos

### ✅ database/connection.py

- 🔄 Usa python-dotenv para cargar la variable del .env:

`from sqlalchemy import create_engine`
`from sqlalchemy.orm import sessionmaker`
`from backend.database.base_class import Base`
`from dotenv import load_dotenv`
`import os`
   `load_dotenv()` 

   `DATABASE_URL = os.getenv("DATABASE_URL")`

   `engine = create_engine(DATABASE_URL)`
   `SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)`

 `def get_db():`
     `db = SessionLocal()`
    `try:`
        `yield db`
    `finally:`
         `db.close()`

### ✅ DATABASE / base_class.py

`from sqlalchemy.ext.declarative import declarative_base`
`Base = declarative_base()`

### ✅ DATABASE / __init__.py

`from .connection import engine, SessionLocal, get_db`
`from .base_class import Base`

### DATABASE / create_tables.py

`from backend.database.connection import engine`
`from backend.database.base_class import Base`   
`from backend.models import *`  

`def create_all_tables():`                 
     `Base.metadata.create_all(bind=engine)`  

`if __name__ == "__main__":`                   
`print("✅ Tablas creadas exitosamente.")`
`create_all_tables()`

### ✅ MODELOS - models

`from sqlalchemy import Column, Integer, String`
`from backend.database.base_class import Base`

`class Tercero(Base):`
`__tablename__ = "terceros"`

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    identificacion = Column(String, unique=True, index=True)
    direccion = Column(String)

### ✅ MODELS /__init__.py

`from .terceros import Tercero`
`__all__ = [`
`"Tercero",`
` ]`

### ✅ ESQUEMAS - schemas

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

### ✅ ESQUEMAS / __init__.py

`from .terceros import Tercero, TerceroCreate, TerceroBase`

### ✅ ROUTERS - routers 

`from fastapi import APIRouter, HTTPException, Depends`
`from sqlalchemy.orm import Session`
`from backend.schemas.tercero import TerceroCreate, Tercero`
`from backend.models.tercero import Tercero as DBTercero`
`from backend.database import get_db`

- router = APIRouter()

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

### ✅ ROUTERS / __init__.py

`from .terceros import router as terceros_router`

### ✅ MAIN.PY - Integracion de los Endpoints  

`from fastapi import FastAPI`
`from fastapi.middleware.cors import CORSMiddleware`
`from backend.routers import terceros  # importa tu router`

`app = FastAPI()`

 `🔐 CORS middleware`
 `app.add_middleware(`
     `CORSMiddleware,`
     `allow_origins=["http://localhost:3000"]`
     `allow_credentials=True,`
     `allow_methods=["*"],`
     `allow_headers=["*"],`
 `)`

### ✅ Incluye tus routers con prefijo /api

`app.include_router(terceros.router, prefix="/api")`

### ✅ "Crear tablas:" 

`python -m backend.db.create_tables`


## 📁 Explicación de la organización:

### 📁 database/ - Conexion a la base de datos. Aqui generalmente se encuentra:
└──🔹El motor de conexion (engine).
───🔹La sesion (SessionLocal).
───🔹El archivo create_tables.py para inicializar las tablas a partir de los modelos.

### 📁 models/ - Define las clases de SQLAlchemy que representan tus tablas en la base de datos. Cada clase equivale a una tabla y define sus campos, relaciones y restricciones.

### 📁 schemas/ - Contiene las clases de Pydantic, utilizadas para:
└──🔹Validar los datos de entrada y salida de la API.
───🔹Separar los modelos internos de la base de datos de las estructuras que se exponen al cliente.
──│🔹Esto mejora la seguridad y mantiene el codigo desacoplado.

### 📁 routers/ - Endpoints de la API agrupados por funcionalidad. Cada archivo corresponde a un recurso o entidad y contiene:
└──🔹Las rutas (@router.get, @router.post, etc.).
──│🔹La logica de interaccion entre los schemas y los modelos.

### ⚙️ __init__.py en cada carpeta - Este archivo hace que la carpeta sea reconocida como un paquete de Python y permite importaciones limpias entre modulos. Ayuda a mantener una estructura modular y organizada.

### 📝 main.py - Es el punto de entrada de la aplicacion FastAPI. Aqui se:
└──🔹Crea la instancia principal de la app (app = FastAPI()).
───🔹Se agregan middlewares (como CORS).
───🔹Se incluyen los routers definidos en routers/.
───🔹Se levanta el servidor si se ejecuta directamente.
──│🔹Beneficios de esta Estructura.

---

##                🧠 **Estructura de archivos __init__.py**

### 📁 Carpetas de modelos (models/)  

- 🎯 Importamos las clases de los modelos que queremos exponer
`from .archivo_1 import Clase1`
`from .archivo_2 import Clase2`

-  🔹Controlamos qué se puede importar desde fuera
`__all__ = ["Clase1", "Clase2"]`


###  📁 Carpetas de routers (routers/)

-  🎯 Importamos los routers definidos en otros archivos
`from .recurso_1 import router as recurso_1_router`
`from .recurso_2 import router as recurso_2_router`

-  🔹Listamos los routers para facilitar su uso desde main.py o routers principales

` __all__ = ["recurso_1_router", "recurso_2_router"]`

###  📁 Carpetas de esquemas (schemas/)

-  🎯 Importamos los esquemas base, create, update, etc.
`from .archivo_1 import Clase1Base, Clase1Create`
`from .archivo_2 import Clase2Base, Clase2Create`

-  🔹Indicamos explícitamente qué exportamos

`__all__ = ["Clase1Base", "Clase1Create", "Clase2Base", "Clase2Create"]`


### 📁 Carpetas de servicios (services/)

-  🎯 Importamos funciones o clases que contienen la lógica del negocio
`from .recurso_1 import funcion_1`
`from .recurso_2 import clase_servicio`

-  🔹Exportamos solo lo necesario

`__all__ = ["funcion_1", "clase_servicio"]`


### 📁 Carpetas de utilidades (utils/)

-  🎯 Importamos funciones específicas de procesamiento PDF
`from .lector_pdf import extraer_texto`
`from .validador_pdf import validar_formato`

-  🔹Dejamos claro qué funciones queremos que estén disponibles

`__all__ = ["extraer_texto", "validar_formato"]`


### ❌ Carpetas que no necesitan __init__.py

└── 📁 Carpetas de uploads - solo para guardar archivos temporales.
─── 📁 Carpetas de tests - si no planeas importar sus módulos desde fuera.
──│ 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.
           
---