import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.actions.create_folder import CreateFolderAction
from app.core.runner import ActionRunner
from app.core.workflow import Workflow

def main():
    # Inicializamos la app (El motor de Qt). 
    # sys.argv permite que la app reciba argumentos por terminal si fuera necesario.
    app = QApplication(sys.argv)

    # Creamos la ventana principal
    window = MainWindow()

    # --- LÓGICA DE CONEXIÓN ---
    # Definimos qué pasa cuando se interactúa con la vista de archivos.
    # Es como un controlador en MVC.
    def ejecutar_creacion():
        nombre = window.files_page.folder_input.text()
        if not nombre:
            window.files_page.status_label.setText("⚠️ Escribe un nombre")
            return
            
        # 1. Preparamos la acción y el estado visual
        accion = CreateFolderAction(nombre)
        window.files_page.status_label.setText("⏳ Procesando...")
        window.files_page.btn_create.setEnabled(False) # Bloqueamos botón para evitar doble clic

        # 2. Creamos el Worker (Thread)
        # IMPORTANTE: Guardamos referencia en 'window' para que Python no lo borre de memoria (GC)
        window.worker = ActionRunner(accion)

        # 3. Conectamos las señales (Event Listeners)
        window.worker.finished.connect(al_terminar)
        window.worker.error.connect(al_error)

        # 4. ¡Fuego! (Esto arranca el hilo paralelo)
        window.worker.start()

    def ejecutar_workflow_dinamico():
        # 1. Validamos si hay pasos en la lista
        count = window.files_page.steps_list.count()
        if count == 0:
            window.files_page.status_label.setText("⚠️ Añade al menos un paso a la lista")
            return

        # 2. Creamos el objeto Workflow
        flujo_usuario = Workflow("Flujo Personalizado")

        # 3. LEEMOS LA UI: Convertimos cada item de la lista en una Acción
        for i in range(count):
            nombre_carpeta = window.files_page.steps_list.item(i).text()
            flujo_usuario.add_step(CreateFolderAction(nombre_carpeta))

        # 4. Preparamos la ejecución igual que antes
        window.files_page.status_label.setText("⏳ Ejecutando pasos...")
        window.files_page.btn_create.setEnabled(False)

        # Usamos el Runner para no bloquear la UI
        window.worker = ActionRunner(flujo_usuario)
        window.worker.finished.connect(al_terminar)
        window.worker.error.connect(al_error)
        window.worker.start()

    def al_terminar(resultado):
        window.files_page.status_label.setText("✅ ¡Todo creado!")
        window.files_page.btn_create.setEnabled(True)
        # Opcional: limpiar lista al terminar
        # window.files_page.steps_list.clear()

    def al_error(err):
        window.files_page.status_label.setText(f"❌ Error: {err}")
        window.files_page.btn_create.setEnabled(True)

    # "Escuchamos" el clic del botón que está dentro de la vista de archivos
    # window.files_page.btn_create.clicked.connect(ejecutar_creacion)
    window.files_page.btn_create.clicked.connect(ejecutar_workflow_dinamico)

    # Mostramos la ventana y ejecutamos el Loop infinito (Event Loop)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()