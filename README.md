## 🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.


Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---

# 🗂️ Estructura general

### ├── 📦 backend/   Backend con FastAPI (API REST, lógica de negocio, base de datos, automatizaciones)
### └── 💻 frontend/  Frontend moderno en Next.js (interfaz de usuario para clientes y administrativos)

---

# 🏛️ Contaclic Core

**contaclic_core** es el backend central de la plataforma de automatización contable. Está construido con FastAPI, Docker, pruebas automatizadas, y una estructura escalable y profesional.
                    
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

## 📥 Configuración local


- ✅  Clona el repositorio: 

 `https://github.com/Contaclic-Action/contaclic-core.git` 


- ✅  Entorno virtual 

    python -m venv .venv
    source .venv/bin/activate  - Linux/macOS

    .venv\Scripts\activate     - Windows

- ✅ Instalar dependencias.

 `pip install -r requirements.txt`

- ✅ Levantar entorno con Docker.

 `docker-compose up --build`

### 🧪 Correr pruebas.

 `pytest src/tests`

- Usa pytest-cov para cobertura:

 `pytest --cov=src/app src/tests` 


### 📌 Las pruebas están organizadas en 🗂️ src/tests/. 

Se utiliza pytest para cobertura y ejecución.

---


## 🔗 Conexión de proyecto local a GitHub

### ✅ Crea un archivo .gitignore en la raíz del proyecto.

Incluye rutas comunes para ignorar archivos innecesarios:

1. ✅ Inicializar el repositorio local  ▶ `git init`
2. ✅ Agrega el repositorio remoto ▶ `git remote add origin https://github.com/Contaclic-Action/contaclic-core.git`
3. ✅ Crea y muévete a la rama principal main  ▶ `git checkout -b main`
4. ✅ Añade los archivos y haz tu primer commit ▶ `git add .`
 ▶ `git commit -m "Primer commit "`
5. ✅ Sube tu código a GitHub  ▶ `git push -u origin main`

- ⚠️ Si da error porque el repositorio remoto ya contiene archivos:

▶ `git push -u origin main --force`

---

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
