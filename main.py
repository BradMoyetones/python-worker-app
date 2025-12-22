import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.actions.create_folder import CreateFolderAction

def main():
    # 1. Crear la instancia de la app (como el main process de Electron)
    app = QApplication(sys.argv)

    # 2. Instanciar la ventana
    window = MainWindow()

    # 3. Lógica simple para conectar el botón con la acción
    def al_hacer_clic():
        accion = CreateFolderAction("Carpeta_Desde_UI")
        resultado = accion.run()
        window.label.setText(resultado)

    window.btn_run.clicked.connect(al_hacer_clic)

    # 4. Mostrar y ejecutar
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()