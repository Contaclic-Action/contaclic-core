---
# Guía para Contribuir

Gracias por tu interés en contribuir. Este documento establece un flujo de trabajo claro y estandarizado para mantener la calidad del código en **Contaclic Action**.

---

## ✅ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

Ver el archivo [Tecnologías_utilizadas](./docs/backend/TECNOLOGIAS.md) para más información.

---

## 🔁 Flujo de trabajo para contribuciones

1. **Haz un fork del repositorio.**
2. Clonar fork:
`https://github.com/Contaclic-Action/contaclic-core.git`

### ✅ Actualizar README.md en GitHub.

1. Añadir los cambios   ▶ `git add README.md`
2. Hacer el commit      ▶ `git commit -m "Actualizar contenido del README.md"`
3. Subir cambios        ▶ `git push origin main`


### ✅ Actualizar los cambios en GitHub.

1. Verifica archivos    ▶ `git status`
2. Añadir archivos      ▶ `git add .`
3. Commit con mensaje   ▶ `git commit -m "Actualizar estructura y archivos del proyecto"`
4. Subir cambios        ▶ `git push origin main`


- 🖥️ Confirmar en GitHub.

---

## 🔀 Flujo de trabajo (Git)

 Usa `main` solo para código listo para producción.

```bash
✅ Usa ramas para trabajar, por ejemplo:

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


## 🧹 Estilo de código

- Sigue la guía [PEP8](https://peps.python.org/pep-0008/).
- Usa herramientas como `black`, `flake8` o `ruff` para formatear el código.
- Nombrá tus funciones y variables de forma clara y coherente.

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

## 📚 Documentación

- [Tecnologías utilizadas](./docs/backend/TECNOLOGIAS.md)
- [Código de Conducta](./CODE_OF_CONDUCT.md)
- [README del proyecto](./README.md)

---


          

