## 👋 Bienvenido al backend de Contaclic Action.

Este sistema ha sido desarrollado para automatizar y gestionar de forma eficiente, modular y escalable toda la información tributaria, contable y documental de tu empresa, tanto a nivel nacional como municipal.

Aquí encontrarás:

### 🧩 Todos los módulos funcionales del sistema (tributación, Compras, bancos, etc.).

### ⚙️ Detalles técnicos de su estructura, lógica de negocio y herramientas integradas.

### 🚀 Mejoras continuas orientadas a rendimiento, usabilidad y escalabilidad.


Este backend es el núcleo que conecta procesos clave de tu operación contable con automatizaciones inteligentes y una visión clara del estado financiero.

---

# 🏗️ RESUMEN ESTRUCTURA 

- ┣ 📂 .github/                 ▶️  Workflows de GitHub Actions (CI/CD).
- ┣ 📂 .venv/                   ▶️  Entorno virtual local (no se sube a Git).
- ┣ 📂 docs/                    ▶️  Documentación general o técnica.
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

## 🏛️ CONTACLIC_CORE

- ┣ 💼 **backend/**	              ▶️  Contiene la app principal, routers registrados, CORS.
 ┃┣  📄 main.py	                  ▶️  Archivo principal que levanta la API.
 ┃┣  📄 .env	                  ▶️  Almacenar variables de entorno.
- ┣ 💼 **backend/bot/**	          ▶️  Bot de Telegram con Python. "usuario automático".
- ┣ 💼 **backend/clientes/**	  ▶️  Libreto de operaciones.
- ┣ 💼 **backend/contabilidad/**  ▶️  Lógica de negocio central.
- ┣ 💼 **backend/core/**	      ▶️  Configuraciones de la app.
- ┣ 💼 **backend/database/**	  ▶️  Configuracion de la base de datos.  
- ┣ 💼 **backend/integrations/**  ▶️  Módulo unificado para integraciones.
- ┣ 💼 **backend/models/**	      ▶️  Modelos SQLAlchemy para representar las tablas. 
- ┣ 💼 **backend/routers/**	      ▶️  Endpoints FastAPI organizados por dominio.
- ┣ 💼 **backend/schemas/**	      ▶️  Esquemas de entrada/salida (Pydantic).
- ┣ 💼 **backend/services/**      ▶️  Divide lógica de negocio de forma clara y coherente.
- ┣ 💼 **backend/tests/**	      ▶️  Es la raíz de la pruebas automáticas.
- ┣ 💼 **backend/uploads/**	      ▶️  Guardar temporalmente los archivos (CSV, PDF, XML).
- ┗ 💼 **backend/utils/**	      ▶️  Funciones pequenas y sin conexion a la base de datos.

---

## 📌 Explicación de la organización:

### 📁 database/ 

Conexion a la base de datos. Aqui generalmente se encuentra:

- El motor de conexion (engine).
- La sesion (SessionLocal).
- El archivo create_tables.py para inicializar las tablas a partir de los modelos.

---

### 📁 models/ 

Define las clases de SQLAlchemy que representan tus tablas en la base de datos. Cada clase equivale a una tabla y define sus campos, relaciones y restricciones.

---

### 📁 schemas/ 

Contiene las clases de Pydantic, utilizadas para:

- Validar los datos de entrada y salida de la API.
- Separar los modelos internos de la base de datos de las estructuras que se exponen al cliente.
- Esto mejora la seguridad y mantiene el codigo desacoplado.

---

### 📁 routers/  

Endpoints de la API agrupados por funcionalidad. Cada archivo corresponde a un recurso o entidad y contiene:

- Las rutas (@router.get, @router.post, etc.).
- La logica de interaccion entre los schemas y los modelos.

---

### ⚙️ __init__.py en cada carpeta/ 

Este archivo hace que la carpeta sea reconocida como un paquete de Python y permite importaciones limpias entre modulos. Ayuda a mantener una estructura modular y organizada.

- ❌ Carpetas que no necesitan `__init__.py`

- 📁 Carpetas de uploads - solo para guardar archivos temporales.
- 📁 Carpetas de tests - si no planeas importar sus módulos desde fuera.
- 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.

### 📝 main.py/

Es el punto de entrada de la aplicacion FastAPI. Aqui se:

- Crea la instancia principal de la app (app = FastAPI()).
- Se agregan middlewares (como CORS).
- Se incluyen los routers definidos en routers/.
- Se levanta el servidor si se ejecuta directamente.
- Beneficios de esta Estructura.

---