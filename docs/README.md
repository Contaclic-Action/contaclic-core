# 📘 Documentación Técnica - Contaclic Core

Este sistema ha sido desarrollado para automatizar y gestionar de forma eficiente, modular y escalable toda la información tributaria, contable y documental de tu empresa, tanto a nivel nacional como municipal.

---

## 📁 Estructura del Proyecto

📁 contaclic_core
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

Aquí encontrarás:

### 🧩 Todos los módulos funcionales del sistema.

### ⚙️ Detalles técnicos de su estructura, lógica de negocio y herramientas integradas.

### 🚀 Mejoras continuas orientadas a rendimiento, usabilidad y escalabilidad.


Es el núcleo que conecta procesos clave de la operación contable con automatizaciones inteligentes y una visión clara del estado financiero.

---

## 📌 Objetivo

El objetivo de esta documentación es centralizar y explicar con claridad:

- La función de cada módulo del backend.
- La ubicación de los modelos, esquemas, rutas y servicios.
- Los flujos internos de los procesos clave (como ingreso de facturas, terceros, etc.).
- Cómo se estructuran los mixins, middlewares, validadores y utilidades.

---

## 📚 Documentación Backend

Este espacio contiene la documentación técnica de los módulos desarrollados para el backend de **Contaclic Core**.  
La estructura de esta carpeta replica la arquitectura del proyecto para facilitar su exploración y mantenimiento.

- [🗂️ BACKEND](./backend/README.md)

---