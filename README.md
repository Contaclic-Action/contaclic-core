🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.

> Automatización contable y administrativa con propósito, visión y estructura.


## 🚀 Qué hace Contaclic Action

- Automatiza el ingreso y validación de facturas electrónicas (XML, PDF).
- Procesa archivos masivos desde ZIP, Excel, imagen, CSV.
- Se integra con servicios externos (correo, APIs, Power BI, Microsoft 365).
- Mantiene una estructura modular y documentada para crecer sin romperse.
- Soporta flujos internos contables (egresos, ingresos, compras, informes).
- Guarda toda la información con trazabilidad, control y posibilidad de auditoría.

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


🚧 Estado del proyecto (mayo 2025)

- [x] Estructura modular completa
- [ ] Procesamiento de XML y PDF
- [ ] Modelos y esquemas contables
- [ ] Integración con correo y Power Automate
- [ ] Documentación interna 100% revisada
- [ ] Primeras conexiones con software contable externo
- [ ] Ensayo con empresa real o propia

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
