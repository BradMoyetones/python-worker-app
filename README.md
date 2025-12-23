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

## 🏗️ Generar Ejecutables (Build)

Se ha configurado un archivo `WorkerAppPro.spec` para empaquetar la aplicación junto con sus `assets` de forma automática.

### Para Windows (.exe) o macOS (.app)

1. Instala PyInstaller: `pip install pyinstaller`
2. Ejecuta el build:
```bash
pyinstaller WorkerAppPro.spec

```


3. Encontrarás el resultado en la carpeta `dist/`.

*Nota: Para generar el ejecutable de Windows debes estar en Windows, y para el de Mac debes estar en macOS.*

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

* `app/ui/`: Definición de ventanas y widgets (PySide6) y vistas dinámicas.
* `app/actions/`: Lógica de cada tarea (clases de acción pura).
* `app/core/`: El motor (Runner) que maneja hilos y el sistema de Workflows.
* `assets/`: Iconos SVG y recursos visuales.
* `main.py`: Punto de entrada y orquestador principal.