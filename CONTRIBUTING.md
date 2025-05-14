---
# Guía para Contribuir

Gracias por tu interés en contribuir. Este documento establece un flujo de trabajo claro y estandarizado para mantener la calidad del código en **Contaclic Action**.

---
## ✅ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

[tecnologias](TECNOLOGIAS)

---


### ✅ Actualizar el README.md en GitHub.

1. Añadir los cambios del archivo README.md.
▶ `git add README.md`
2. Hacer el commit con un mensaje claro.
▶ `git commit -m "Actualizar contenido del README.md"`
3. Subir los cambios al repositorio remoto. 
▶ `git push origin main`


### ✅ Subir o actualizar los cambios del proyecto en GitHub.

1. Verifica qué archivos han cambiado.
▶ `git status`
2. Añade todos los archivos modificados 
▶ `git add .`
3. Haz un commit con un mensaje descriptivo 
▶ `git commit -m "Actualizar estructura y archivos del proyecto"`
4. Sube los cambios al repositorio remoto 
▶ `git push origin main`


- 🖥️ Confirmar en GitHub.

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

 Export class ActiveStateMixin:

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

