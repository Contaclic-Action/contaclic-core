🖼️ Logo

<p align="center">
  <img src="./assets/logo.png" alt="Contaclic Logo" width="200"/>
</p>

# 🧠  Plataforma Contable y Tributaria.


Automatización contable y tributaria inteligente para empresas. Incluye módulos de carga masiva, validación de datos, creación de terceros, lectura de RUT en PDF, conciliación de compras y más.

---

## 📚 Documentación

Ver el archivo [backend](./docs/README.md) para más información.

---

## 📥 Configuración local


1. 🧹 **Gestión del Entorno Virtual y Dependencias**
    
   
- ✅ Eliminar el Entorno Virtual Antiguo (Limpieza).

     ▶ `Remove-Item -Path .venv -Recurse -Force`  

- ✅ Crear       ▶  `python -m venv .venv`                       
- ✅ Activar     ▶  `.\.venv\Scripts\activate`
- ✅ Verificar   ▶  `pip install -r requirements.txt` 
                    
- ✅ Para verificar todas las librerías instaladas específicamente en ese entorno.
     
 ▶ `pip freeze`

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

 ## 💪🏼 CONTRIBUTING.md 

 Guía para quienes quieran colaborar en el desarrollo. Ver el archivo [CONTRIBUTING.md](./CONTRIBUTING.md) para más información.


 ## 👨‍💼 Autor
 Yecid Cordoba – GitHub | <admin@contaclick.pro> 
 Ver el archivo [YECIDCP.md](./YECIDCP.md) para más información.

 ## ⚖️ Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](./LICENSE) para más información.
