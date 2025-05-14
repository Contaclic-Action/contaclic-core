## 🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.


Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---

# 🗂️ Estructura general

## ├── 📦 backend/   Backend con FastAPI (API REST, lógica de negocio, base de datos, automatizaciones)

## 🏛️ Contaclic Core

**contaclic_core** es el backend central de la plataforma de automatización contable. Está construido con FastAPI, Docker, pruebas automatizadas, y una estructura escalable y profesional.


## └── 💻 frontend/  Frontend moderno en Next.js (interfaz de usuario para clientes y administrativos)

---

## 📥 Configuración local


1. Clonación del proyecto

Puedes clonar este repositorio con:

`https://github.com/Contaclic-Action/contaclic-core.git`

 ---

2. 🧹 Gestión del Entorno Virtual y Dependencias.

- ✅ Eliminar el Entorno Virtual Antiguo (Limpieza).
 
    ▶ `Remove-Item -Path .venv -Recurse -Force`   

- ✅ Crear un Nuevo Entorno Virtual.

  ▶ `python -m venv .venv`                       

- ✅ Activar el Nuevo Entorno Virtual. 

  ▶ `.\.venv\Scripts\activate`                   

-  ✅ Verificar listado en la raiz del proyecto. 

  ▶ `pip install -r requirements.txt`           

-  ✅ Para verificar todas las librerías instaladas específicamente en ese entorno.

  ▶ `pip freeze`

---

3. Levantar entorno con Docker.

 `docker-compose up --build`

---

4. 🧪 Correr pruebas.

 `pytest src/tests`
                               
---

🚧 Estado del proyecto

- [x] Backend funcional
- [ ] Servicios de validación de terceros
- [ ] Procesamiento de archivos (XML, PDF)
- [ ] Frontend visual con Next.js
- [ ] Integraciones

 ## 💪🏼 CONTRIBUTING.md 

 Guía para quienes quieran colaborar en el desarrollo. Ver el archivo [CONTRIBUTING](CONTRIBUTING) para más información.

 ## 👨‍💼 Autor
 Yecid Cordoba – GitHub | <admin@contaclick.pro> 

 ## ⚖️ Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más información.
