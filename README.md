## 🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.**


Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---
## 🚀 Tecnologías

| Tecnología               | Descripción                                        |
|--------------------------|----------------------------------------------------|
| **Python 3.11+**         | Backend moderno con FastAPI y SQLAlchemy ORM       |
| **PostgreSQL**           | Base de datos relacional principal                 |
| **React / Next.js 14+**  | Frontend SPA con SSR y rendimiento optimizado      |
| **Tailwind CSS**         | Utilidades para estilos rápidos y personalizables  |
| **React Query**          | Manejo eficiente de estados asincrónicos           |
| **Redis**                | Cache de alta velocidad y cola de tareas           |
| **Power BI**             | Visualización interactiva de datos empresariales   |
| **Pytest**               | Framework de testing para backend                  |
| **Docker & Compose**     | Contenedores y orquestación local/prod             |
| **Pydantic V2**          | Validación de datos y modelos en FastAPI           |

---

# 🗂️ Estructura general

### ├── 📦 backend/   Backend con FastAPI (API REST, lógica de negocio, base de datos, automatizaciones)
### └── 💻 frontend/  Frontend moderno en Next.js (interfaz de usuario para clientes y administrativos)

---

## 👋 Bienvenido al backend de Contaclic Action.

Este sistema ha sido desarrollado para automatizar y gestionar de forma eficiente, modular y escalable toda la información tributaria, contable y documental de tu empresa, tanto a nivel nacional como municipal.

Aquí encontrarás:

### 🧩 Todos los módulos funcionales del sistema (tributación, Compras, bancos, etc.).

### ⚙️ Detalles técnicos de su estructura, lógica de negocio y herramientas integradas.

### 🚀 Mejoras continuas orientadas a rendimiento, usabilidad y escalabilidad.


Este backend es el núcleo que conecta procesos clave de tu operación contable con automatizaciones inteligentes y una visión clara del estado financiero.

---

# 🏛️ Contaclic Core

**contaclic_core** es el backend central de la plataforma de automatización contable. Está construido con FastAPI, Docker, pruebas automatizadas, y una estructura escalable y profesional.
                    
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

### 📁 schemas/ 

Contiene las clases de Pydantic, utilizadas para:

- Validar los datos de entrada y salida de la API.
- Separar los modelos internos de la base de datos de las estructuras que se exponen al cliente.
- Esto mejora la seguridad y mantiene el codigo desacoplado.

### 📁 routers/  

Endpoints de la API agrupados por funcionalidad. Cada archivo corresponde a un recurso o entidad y contiene:

- Las rutas (@router.get, @router.post, etc.).
- La logica de interaccion entre los schemas y los modelos.

### ⚙️ __init__.py en cada carpeta/ 

Este archivo hace que la carpeta sea reconocida como un paquete de Python y permite importaciones limpias entre modulos. Ayuda a mantener una estructura modular y organizada.

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


🚧 Estado del proyecto

- [x] Backend funcional
- [ ] Servicios de validación de terceros
- [ ] Procesamiento de archivos (XML, PDF)
- [ ] Frontend visual con Next.js
- [ ] Integraciones

📌 Recursos útiles

✅ Repositorio en GitHub

✅ Tablero de tareas

✅ Estructura del backend

✅ Issues para empezar

 ## 👨‍💼 Autor
 Yecid Cordoba – GitHub | <admin@contaclick.pro> 

 ## ⚖️ Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más información.
