## 🏛️ Backend

Este módulo es el núcleo de la plataforma **Contaclic Core**, encargado de integrar y automatizar los procesos contables, operativos y tributarios.  
Está construido con **FastAPI**, gestionado con **Docker**, y estructurado para escalar con facilidad, garantizando mantenibilidad y claridad.

---

## 📁 Estructura backend


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
### ⚙️ __init__.py en cada carpeta/ 

Este archivo hace que la carpeta sea reconocida como un paquete de Python y permite importaciones limpias entre modulos. Ayuda a mantener una estructura modular y organizada.

- ❌ Carpetas que no necesitan `__init__.py`

- 📁 Carpetas de uploads - solo para guardar archivos temporales.
- 📁 Carpetas de tests - si no planeas importar módulos desde fuera.
- 📁 Carpetas docs/, temp/ o cualquier carpeta de recursos.

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

### 📝 main.py/

Es el punto de entrada de la aplicacion FastAPI. Aqui se:

- Crea la instancia principal de la app (app = FastAPI()).
- Se agregan middlewares (como CORS).
- Se incluyen los routers definidos en routers/.
- Se levanta el servidor si se ejecuta directamente.
- Beneficios de esta Estructura.

---

## 🧱 Ventajas de esta Arquitectura.

### 🧠 Separación clara de responsabilidades.
Cada capa del proyecto (modelos, esquemas, routers, base de datos) tiene una función bien definida, lo que facilita el entendimiento del sistema y promueve buenas practicas de desarrollo.

### 📈 Escalabilidad
La estructura modular permite agregar nuevos recursos de forma sencilla. Solo necesitas crear el modelo, el esquema y el router correspondiente sin afectar otras partes de la aplicación.

### 🔧 Mantenibilidad
Las capas están desacopladas. Por lo tanto, hacer cambios en una (por ejemplo, en los modelos o esquemas) requiere pocas o ninguna modificacion en el resto del codigo.

### 🧪 Testabilidad
Cada componente (modelo, ruta, lógica) puede ser probado de forma aislada, lo que facilita la escritura de pruebas unitarias y mejora la calidad del codigo.

### 🧩 Consistencia
El uso de un patron uniforme en toda la aplicacion reduce errores, facilita la colaboracion en equipo y mejora la experiencia de desarrollo a largo plazo.

---

## 🏗️ Progreso

- [x] Estructura de carpetas creada
- [x] Documentación base iniciada
- [ ] Documentación completa de `registro/`
- [ ] Documentación de `schemas/`

---

## 📚 Documentación 


### 💼 backend/models/banco

- [📁 BANCOLOMBIA](./models/banco/bancolombia/)


### 💼 backend/models/dian

- [📁 EMITIDOS](./models/dian/emitidos/)
- [📁 RECIBIDOS](./models/dian/recibidos/)


### 💼 backend/models/impuestos

- [📁 MUNICIPAL](./models/impuestos/municipal_ica/)
- [📁 NACIONAL](./models/impuestos/nacional/)


### 💼 backend/models/registro

- [📁 GENERALES](./models/registro/generales.md)
- [📁 GEOGRAFICOS](./models/registro/geograficos.md)
- [📁 METODO PAGO](./models/registro/metodo_pago.md)
- [📁 TERCEROS](./models/registro/terceros.md)


### 💼 backend/models/usuarios

- [📁 USUARIOS](./models/usuarios/)

---

## ✉️ Contacto

Para soporte técnico o colaboración en la documentación, escribe a:
  
📧 **admin@contaclick.pro**

