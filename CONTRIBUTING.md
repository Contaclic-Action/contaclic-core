---
# Guía para Contribuir

Gracias por tu interés en contribuir. Este documento establece un flujo de trabajo claro y estandarizado para mantener la calidad del código en **Contaclic Action**.

---
## ✅ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

[tecnologias](TECNOLOGIAS)

---

## 🔁 Flujo de trabajo para contribuciones

1. **Haz un fork del repositorio.**
2. Clonar fork:
`https://github.com/Contaclic-Action/contaclic-core.git`

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

🧹 Estilo de código

Sigue las guías de estilo PEP8.

Usa black, flake8 o ruff para formatear y verificar tu código.

Nombra tus funciones y variables de forma clara y coherente.

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

---


          

