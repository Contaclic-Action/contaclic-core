---
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

## 🔗 Conexión de proyecto local a GitHub

### ✅ Crea un archivo .gitignore en la raíz del proyecto.

Incluye rutas comunes para ignorar archivos innecesarios:

- ⚙️.gitignore

- ┣ 📁 .venv/
- ┣ 📁 node_modules/
- ┣ 🛠️ __pycache__/
- ┣ 📁.env
- ┣ 🛠️* .log
- ┣ 🛠️* .sqlite3
- ┣ 📁.next/
- ┣ 🛠️ dist/
- ┣ 🛠️ .vscode/
- ┗ 🛠️ .idea/

---

1. ✅ Inicializar el repositorio local - Si tu proyecto aún no está conectado a Git: 
 ▶ `git init`
2. ✅ Agrega el repositorio remoto - Esto vincula tu proyecto local al repositorio de GitHub:
 ▶ `git remote add origin https://github.com/tu_usuario/tu_repositorio.git`
3. ✅ Crea y muévete a la rama principal main.
 ▶ `git checkout -b main`
4. ✅ Añade los archivos y haz tu primer commit - Preparar archivos para subir
 ▶ `git add .`
 ▶ `git commit -m "Primer commit "`
5. ✅ Sube tu código a GitHub -  Si tu rama local se llama main, haz:
 ▶ `git push -u origin main`

- ⚠️ Si da error porque el repositorio remoto ya contiene archivos:
▶ `git push -u origin main --force`

---

 ## ✅ Actualizar el README.md en GitHub.

1. Añadir los cambios del archivo README.md.
▶ `git add README.md`
2. Hacer el commit con un mensaje claro.
▶ `git commit -m "Actualizar contenido del README.md"`
3. Subir los cambios al repositorio remoto. 
▶ `git push origin main`


## ✅ Subir o actualizar los cambios del proyecto en GitHub.

1. Verifica qué archivos han cambiado.
▶ `git status`
2. Añade todos los archivos modificados 
▶ `git add .`
3. Haz un commit con un mensaje descriptivo 
▶ `git commit -m "Actualizar estructura y archivos del proyecto"`
4. Sube los cambios al repositorio remoto 
▶ `git push origin main`

---

## 🖥️ Confirmar en GitHub.

- ✅ README.md se muestra como descripción principal del repositorio.
- ⚙️ .gitignore, requirements.txt y demás archivos son visibles.
- ✅ La rama principal aparece como main.

---

## 🛠️ Configuración local

### ✅  Clona el repositorio: 

▶ `https://github.com/Contaclic-Action/contaclic-core.git` 

### ✅  Entorno virtual 

    python -m venv .venv
    source .venv/bin/activate  - Linux/macOS

    .venv\Scripts\activate     - Windows

### ✅ Instalar dependencias.

▶ `pip install -r requirements.txt`

### ✅ Levantar entorno con Docker.

▶ `docker-compose up --build`

### 🧪 Correr pruebas.

▶ `pytest src/tests`

✅ Usa pytest-cov para cobertura:

▶ `pytest --cov=src/app src/tests` - Para cobertura


📌 Las pruebas están organizadas en 🗂️ src/tests/. 

Se utiliza pytest para cobertura y ejecución.

---

## 🔀 Flujo de trabajo (Git)

 Usa `main` solo para código listo para producción.

 Trabajo en ramas separadas:

- `feat/ → nueva funcionalidad.`
- `fix/ → corrección de bug.`
- `refactor/ → cambios internos sin alterar funcionalidad.`
- `test/ → pruebas.`
- `docs/ → documentación.`
- `chore/ → tareas de mantenimiento.`

---

### 💬 Estilo de Commit

Usamos Conventional Commits:

- `feat: nombre de funcionalidad.`
- `fix: corrección de error.`
- `docs: cambios de documentación.`
- `test: pruebas nuevas o corregidas.`

---

### 📚 Documentación

Documentación general está en docs/

Endpoints autodocumentados con FastAPI Swagger:

▶  `http://localhost:8000/docs`

---

## 🧩 ¿Cómo reportar un error o sugerir una mejora?

Usa la pestaña `Issues` en GitHub para reportar errores, sugerencias o mejoras.

Si vas a enviar un `Pull Request`:
- Crea una rama (`feat/nueva-funcionalidad`).
- Asegúrate de que todos los tests pasen.
- Describe claramente qué hace el cambio.

---

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

- Host: Es la URL o IP de la base de datos.(Ej: dpg-xxxxxxx.render.com) - PSQL Command.
- Port: generalmente 5432 (el puerto estándar de PostgreSQL).
- Maintenance Database: suele ser el nombre de la base de datos principal que creaste en Render.
- Username (Role): Es el nombre que configuraste o te asignó Render ( "DATABASE USER").
- Password: la contraseña del usuario de base de datos.
- Service: este campo no es obligatorio en pgAdmin. 

---

## 🧹 Gestión del Entorno Virtual y Dependencias

 1. ✅ Eliminar el Entorno Virtual Antiguo (Limpieza).
  ▶ `Remove-Item -Path .venv -Recurse -Force`   -  Si la carpeta se llama .venv

 2. ✅ Crear un Nuevo Entorno Virtual.
  ▶ `python -m venv .venv`                       -  Esto crea una nueva carpeta '.venv'

 3. ✅ Activar el Nuevo Entorno Virtual. 
  ▶ `.\.venv\Scripts\activate`                   -  Si la carpeta se llama .venv

 4. ✅ Verificar listado en la raiz del proyecto. 
  ▶ `pip install -r requirements.txt`            -  Instalar las Dependencias.

 5. ✅ Para verificar todas las librerías instaladas específicamente en ese entorno.
  ▶ `pip freeze`                                 -  Muestra el contenido de requirements.txt.

---

# 🏗️ RESUMEN ESTRUCTURA 

- ┣ 📂 .github/                 ▶️  Workflows de GitHub Actions (CI/CD).
       ┃┣ 📝 ci.yml             ▶️  CI principal (test/lint).
       ┃┣ 📝 workflows          ▶️  Pruebas o despliegue automático.
- ┣ 📂 .venv/                   ▶️  Entorno virtual local (no se sube a Git).
- ┣ 📂 docs/                    ▶️  Documentación general o técnica.
       ┃┣🐳 Dockerfile          ▶️  Build para producción.
       ┃┣ 🐳 docker-compose.yml ▶️  Servicios acoplados.
- ┣ 📂 infrastructure/          ▶️  Archivos para despliegue (Dockerfile, docker-compose).
- ┣ 📂 src/                     ▶️  Código fuente principal.
       ┃┣ 📂 tests/             ▶️  Pruebas automatizadas.
       ┃┣ 📂 app/               ▶️  Módulo principal.          
           ┃┣ 📂 backend/       ▶️  Backend FastAPI (rutas, modelos, servicios, etc.).
- ┣ ⚙️ .gitignore               ▶️  Para excluir archivos temporales.
- ┣ 📝 CHANGELOG.md             ▶️  Historial de cambios.
- ┣ 📝 CODE_OF_CONDUCT.md       ▶️  Reglas de comportamiento.
- ┣ 📄 CONTRIBUTING.md          ▶️  Guía para colaboradores.
- ┣ 📄 LICENSE                  ▶️  Tipo de licencia.
- ┣ 📄 README.md                ▶️  Descripción del proyecto.
- ┣ 📄 requirements.txt         ▶️  Dependencias de producción.
- ┗ 🔒 SECURITY.md              ▶️  Cómo reportar vulnerabilidades.

---

## 🏛️ BACKEND

- ┣ 💼 **backend/**	                ▶️   Contiene la app principal, routers registrados, CORS.
 ┃┣  📄 main.py	                    ▶️   Archivo principal que levanta la API.
- ┣ 💼 **backend/bot/**	            ▶️   Bot de Telegram con Python. "usuario automático".
 ┃┣ 🗂️ main.py	                     ▶️   Punto de entrada principal.
┃┣🗂️ handlers/	                     ▶️   Manejadores de comandos.
┃┣ 🗂️ middlewares/                  ▶️   Hacer logs por usuario, o limitar por roles, etc.
┃┣ 🗂️ services/	                 ▶️   Conexión con backend.
- ┣ 💼 **backend/clientes/**	    ▶️   Libreto de operaciones.
 ┃┣ 🗂️ bancos/                      ▶️   Operaciones bancarias.
 ┃┣ 🗂️ recibidos/                   ▶️   Modulo recibido Dian. Todo sobre compras.
 ┃┣ 🗂️ terceros/	                 ▶️   Manejo de usuarios y terceros.
- ┣ 💼 **backend/contabilidad/**	▶️   Lógica de negocio central.
 ┃┣ 🗂️ models/	                     ▶️   Modelos de datos.
 ┃┣ 🗂️ routers/                     ▶️   Endpoints (listar, crear, actualizar, etc.).
 ┃┣ 🗂️ schemas/                     ▶️   Esquemas expuestos en API.
- ┣ 💼 **backend/core/**	        ▶️   Configuraciones de la app.
 ┃┣ 📄 config.py	                ▶️   Gestiona la configuración externa.
- ┣ 💼 **backend/database/**	    ▶️   Configuracion de la base de datos.  
 ┃┣ 📄 connection.py	            ▶️   Logica de conexion a PostgreSQL usando SQLAlchemy.
- ┣ 💼 **backend/integrations/**    ▶️   Módulo unificado para integraciones.
 ┃┣ 🗂️ auth/                        ▶️   Autenticación y tokens.
- ┣ 💼 **backend/models/**	        ▶️   Modelos SQLAlchemy para representar las tablas. 
 ┃┣ 🗂️ registro/	                 ▶️   Modelos geograficos para crear terceros.
 ┃┣ 🗂️ dian/	                     ▶️   Conciliacion modulo Dian.
 ┃┣ 🗂️ bancos/	                     ▶️   Conciciliacion de extractos bancarios.
- ┣ 💼 **backend/routers/**	        ▶️   Carpeta general de endpoints FastAPI organizados por dominio.
 ┃┣ 🗂️ registro/   
 ┃┣ 🗂️ dian/
 ┃┣ 🗂️ bancos/
- ┣ 💼 **backend/schemas/**	        ▶️  Aqui defines los esquemas de entrada/salida (Pydantic).
 ┃┣ 🗂️ bancos/	                     ▶️  Conciciliacion de extractos bancarios.
 ┃┣ 🗂️ registro/	                 ▶️  Esquema geograficos para crear terceros.  
 ┃┣ 🗂️ dian/	                     ▶️  Conciliacion modulo Dian.   
- ┣ 💼 **backend/services/**        ▶️  Divide lógica de negocio de forma clara y coherente.
 ┃┣ 🗂️ bancos/	                     ▶️  Operaciones bancarias.
 ┃┣ 🗂️ registro/                    ▶️  Encapsula toda la lógica, terceros, geográficos, etc.
 ┃┣ 🗂️ dian/	                     ▶️  Interacción con los datos regulados por la DIAN.
- ┣ 💼 **backend/tests/**	        ▶️  Es la raíz de la pruebas automáticas.
 ┃┣ 🗂️ clientes/                    ▶️  Dependencias comunes de la API.
 ┃┣ 🗂️ models/                      ▶️  Modelos de datos.
 ┃┣ 🗂️ database/                    ▶️  Esquemas para validación/serialización API.
- ┣ 💼 **backend/uploads/**	        ▶️  Para guardar temporalmente los archivos (CSV, PDF, XML).
 ┃┣ 🗂️ uploads/bancos/YYYY/
 ┃┣ 🗂️ uploads/terceros/YYYY/
 ┃┣ 🗂️ uploads/emitidos/YYYY/
- ┗ 💼 **backend/utils/**	         ▶️  Funciones pequenas y sin conexion a la base de datos.
 ┃┣ 🗂️ archivos/pdf/	              ▶️  Funciones para leer PDFs.
 ┃┣ 🗂️ archivos/csv/	              ▶️  Validaciones CSV regitros de empresas y personas naturales.
 ┃┣ 🗂️ archivos/xml/	              ▶️  XML.

---

##                🧠 **Estructura de archivos `__init__.py`**

### 🗂️ DATABASE / `__init__.py`

`from .connection import engine, SessionLocal, get_db`
`from .base_class import Base`

---

### 📁 Carpetas de modelos (models/)  

- 🎯 Importamos las clases de los modelos que queremos exponer.

`from .archivo_1 import Clase1`
`from .archivo_2 import Clase2`

-  Controlamos qué se puede importar desde fuera.

`__all__ = ["Clase1", "Clase2"]`

---

###  📁 Carpetas de routers (routers/)

-  🎯 Importamos los routers definidos en otros archivos.

`from .recurso_1 import router as recurso_1_router`
`from .recurso_2 import router as recurso_2_router`

-  Listamos los routers para facilitar su uso desde main.py o routers principales.

` __all__ = ["recurso_1_router", "recurso_2_router"]`

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

---

### ❌ Carpetas que no necesitan `__init__.py`

- 📁 Carpetas de uploads - solo para guardar archivos temporales.
- 📁 Carpetas de tests - si no planeas importar sus módulos desde fuera.
- 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.
           
---

## 📋 PROCESO CREACION DE TABLAS

### 🗂️ .env

- DATABASE_URL=postgresql://usuario:contrasena@host:puerto/basededatos

---

### 🗂️ database/connection.py

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

---

### 🗂️ DATABASE / base_class.py

`from sqlalchemy.ext.declarative import declarative_base`
`Base = declarative_base()`

### 🗂️ DATABASE / create_tables.py

`from backend.database.connection import engine`
`from backend.database.base_class import Base`   
`from backend.models import *`  

`def create_all_tables():`                 
     `Base.metadata.create_all(bind=engine)`  

`if __name__ == "__main__":`                   
`print("✅ Tablas creadas exitosamente.")`
`create_all_tables()`

### 🗂️ DATABASE / mixins

1. TimestampMixin.py 🧱

`from sqlalchemy import Column, DateTime, func`

`class TimestampMixin:`

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())

2. UserTrackingMixin.py 👤

`from sqlalchemy import Column, String`

`class UserTrackingMixin:`

    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)

3. ActiveStateMixin.py ✅

`from sqlalchemy import Column, Boolean, DateTime, func`

# Export class ActiveStateMixin:

`class ActiveStateMixin:`

    estado = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)


4. LocationMixin.py 🌍

`from sqlalchemy import Column, String`

`class LocationMixin:`

    pais = Column(String, nullable=True)
    departamento = Column(String, nullable=True)
    ciudad = Column(String, nullable=True)

5. IdentifiableMixin.py 🔑

`from sqlalchemy import Column, Integer, String`

`class IdentifiableMixin:`

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)

6. Combinación de mixins 🧩

`from backend.database.base_class import Base`
`from backend.database.mixins import AuditMixin, LocationMixin`

`class Nombre(Base, AuditMixin, LocationMixin):`

    __tablename__ = "Nombres"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    identificacion = Column(String, unique=True, nullable=False)


---

### 🗂️ MODELOS - models


- 🗂️ `registro`


`from sqlalchemy import Column, Integer, String`

`from backend.database.base_class import Base`

`from backend.database.audit_mixin import AuditMixin`


    class nombre(Base, AuditMixin):
    __tablename__ = "tercero"

     id = Column(Integer, primary_key=True, index=True)
     numero_identificacion = Column(String, index=True)

  `Trazabilidad`

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    estado = Column(Boolean, default=True)

---

### 🗂️ ESQUEMAS - schemas


`from pydantic import BaseModel` 

`from typing import Optional`

`from datetime import datetime`

`class nombre(BaseModel):`
    

`class TerceroCreate(TerceroBase):`
    pass  # Aquí no necesitas campos adicionales, porque se llenan automáticamente

class Nombre(NombreBase):
    id: int
    fecha_creacion: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_creacion: Optional[str]
    usuario_actualizacion: Optional[str]
    activo: Optional[bool] = True

    class Config:
        from_attributes = True  # Necesario para que funcione con ORM


---

### 🗂️ ROUTERS - routers 

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

---

### 🗂️ MAIN.PY - Integracion de los Endpoints  

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

---

### 🗂️ Incluye tus routers con prefijo /api

`app.include_router(terceros.router, prefix="/api")`

---

### 🗂️ "Crear tablas:" 

`python -m backend.db.create_tables`

---

