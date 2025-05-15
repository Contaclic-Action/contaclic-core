🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.


Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---



## 📥 Configuración local


1. 🧹 **Gestión del Entorno Virtual y Dependencias**
    
   
-  Eliminar el Entorno Virtual Antiguo (Limpieza).

      ▶ `Remove-Item -Path .venv -Recurse -Force`  

- Crear       ▶  `python -m venv .venv`                       
- Activar     ▶  `.\.venv\Scripts\activate`
- Verificar   ▶  `pip install -r requirements.txt` 
                    
- Para verificar todas las librerías instaladas específicamente en ese entorno.
     
      ▶ pip freeze

---

2. **Levantar entorno con Docker**

`docker-compose up --build`
 
---

3. 🖱️ **Clonación del proyecto**

Puedes clonar este repositorio con:

git clone `https://github.com/Contaclic-Action/contaclic-core.git`
`cd contaclic_core`

 ---

4. 🧪 Correr pruebas.

- 📂 src/                     ▶️  Código fuente principal.
- ┃┣ 📂 tests/                ▶️  Pruebas automatizadas.

Ejecuta las pruebas unitarias y de integración con:

 `pytest src/tests`
                            
---


🚧 Estado del proyecto

- [x] Backend funcional
- [ ] Servicios de validación de terceros
- [ ] Procesamiento de archivos (XML, PDF)
- [ ] Frontend visual con Next.js
- [ ] Integraciones

---

# 📚 Documentación

Bienvenido a **Contaclic Core**, una plataforma modular para automatización contable y tributaria.

---

## 📁 Contaclic_Core

El backend está construido con **FastAPI**, **SQLAlchemy**, **Docker** y otras herramientas modernas.  
La documentación interna del proyecto se encuentra en:

[📁 ESTRUCTURA PROYECTO](./docs/README.md)

---

## 💪🏼 Contribuciones

¿Quieres colaborar con este proyecto?

Consulta nuestra guía de colaboración en:  
[🔧 CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 🧑🏽 Autor

**Yecid Córdoba P.**  

📧 <admin@contaclick.pro>  
🔍 Más información en: [YECIDCP.md](./YECIDCP.md)

---

## ⚖️ Licencia

Este proyecto está bajo la Licencia MIT.  

📄 Revisa los términos en: [LICENSE](./LICENSE)
