# 🛠️ Python Worker App

Este es un proyecto estilo **Worker** para automatizar tareas de archivos (crear, copiar, mover, etc.), estructurado de forma modular similar a una arquitectura de Node.js.

## 🚀 Inicio Rápido

### 1. Preparar el entorno (Solo la primera vez)

En Python, siempre usamos un entorno virtual para no ensuciar el sistema:

```bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno
# En Windows:
.venv\Scripts\activate
# En Mac/Linux:
source .venv/bin/activate

```

### 2. Instalar dependencias

Una vez activado el entorno (verás un `(.venv)` en la terminal):

```bash
pip install -r requirements.txt

```

### 3. Ejecutar la aplicación

Para lanzar la interfaz gráfica:

```bash
python main.py

```

---

## 📦 Gestión de Dependencias (El "Cheat Sheet")

Como en Node.js usamos `package.json`, aquí usamos el `requirements.txt`. Estos son los comandos equivalentes:

* **Instalar un nuevo paquete:**
`pip install nombre-paquete`
* **Guardar cambios en el "package.json" (congelar):**
`pip freeze > requirements.txt`
*Nota: Haz esto siempre después de instalar algo nuevo.*
* **Ver qué hay instalado actualmente:**
`pip list`

---

## 🛠️ Comandos de Desarrollo Útiles

### Auto-reload (Tipo Vite/Nodemon)

Si quieres que la app se reinicie sola al guardar cambios (`Ctrl + S`), instala `watchdog` y corre:

```bash
# Instalar herramienta
pip install watchdog

# Correr con auto-restart
watchmedo auto-restart --patterns="*.py" --recursive -- python main.py

```

### Estructura del Proyecto

* `app/ui/`: Definición de ventanas y widgets (PySide6).
* `app/actions/`: Lógica de cada tarea (clases que heredan de `BaseAction`).
* `app/core/`: El motor que ejecuta las acciones y maneja los hilos.
* `main.py`: Punto de entrada y orquestador principal.