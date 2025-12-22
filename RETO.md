# 🧠🔥 RETO (SIN AI): **Desktop Workflow Automator**

Una **app de escritorio** que te permita **crear, ejecutar y monitorear flujos de acciones locales**, todo definido por el usuario desde la UI.

Nada de lenguaje natural.
Nada de magia negra.
**Todo explícito, controlado y lógico.**

---

## 🎯 IDEA CENTRAL

La app permite al usuario construir **workflows** paso a paso, por ejemplo:

1. Crear carpeta
2. Copiar archivos
3. Renombrar
4. Comprimir
5. Ejecutar un comando
6. Borrar con confirmación

Y luego:

* Guardarlos
* Ejecutarlos
* Ver logs
* Manejar errores

---

## 🖥️ UI (simple pero real)

Ventana con 3 zonas:

### 1️⃣ Panel de pasos

* Lista ordenada de acciones
* Botones: ↑ ↓ ✏️ ❌

### 2️⃣ Editor de paso

* Tipo de acción (select)
* Inputs dinámicos según la acción

### 3️⃣ Consola

* Logs en tiempo real
* Estado (idle / running / error / done)

---

## 🧠 ACCIONES SOPORTADAS (v1)

* `CreateFolder(path)`
* `CopyFile(src, dest)`
* `MoveFile(src, dest)`
* `Rename(path, new_name)`
* `Delete(path)` ⚠️ confirmación
* `Zip(path, output)`
* `RunCommand(cmd)`

---

## 🔥 REGLAS DEL RETO (NO negociables)

❌ No ifs gigantes
❌ No lógica en la UI
❌ No try/except globales

✅ Cada acción es una **clase**
✅ Todas heredan de `BaseAction`
✅ Cada acción implementa `execute()`
✅ Logs centralizados
✅ Validación antes de ejecutar

---

## 🧩 ESTRUCTURA OBLIGATORIA

```txt
app/
 ├─ ui/
 │   └─ main_window.py
 ├─ actions/
 │   ├─ base.py
 │   ├─ create_folder.py
 │   ├─ copy_file.py
 │   └─ ...
 ├─ core/
 │   ├─ workflow.py
 │   ├─ runner.py
 │   └─ logger.py
 └─ main.py
```

---

## 🧠 LO QUE APRENDES DE VERDAD

* Python orientado a objetos (bien hecho)
* Polimorfismo
* Manejo fino de errores
* Arquitectura limpia
* Separación UI / lógica
* Estados y ejecución secuencial

Esto **no es Python de scripts**, es **Python de aplicaciones reales**.

---

## 🧪 NIVELES DE DIFICULTAD

### 🟢 Nivel 1

* Ejecutar acciones secuenciales
* Logs básicos

### 🟡 Nivel 2

* Cancelar ejecución
* Validaciones previas
* Guardar workflows en JSON

### 🔴 Nivel 3 (tryhard)

* Rollback parcial
* Reintentos
* Ejecución condicional
* Variables entre pasos

---

## 🧨 BONUS OPCIONAL

* Threads para no congelar la UI
* Exportar .exe
* Tema dark
* Historial de ejecuciones

---

## 🧠 POR QUÉ ESTE RETO SÍ TE CALZA

* Nada de AI
* Nada de frameworks monstruo
* Todo es lógica
* UI real
* Escalable
* Te obliga a pensar como ingeniero, no como scripter

---

Si quieres, elige el **framework de UI** (Tkinter o PySide)