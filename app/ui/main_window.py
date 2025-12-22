from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Worker App")
        self.resize(400, 300)

        # Layout simple
        layout = QVBoxLayout()
        
        self.label = QLabel("Listo para ejecutar acciones")
        self.btn_run = QPushButton("Ejecutar Crear Carpeta")
        
        layout.addWidget(self.label)
        layout.addWidget(self.btn_run)

        # Contenedor principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)