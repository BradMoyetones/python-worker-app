from PySide6.QtWidgets import ( QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QAbstractItemView, QListWidget )
from PySide6.QtCore import Qt

class HomeView(QWidget):
    """Vista de bienvenida. Es un contenedor simple (div)."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40) # Padding generoso

        self.title = QLabel("🏠 Página de Inicio")
        # Estilos rápidos para no llenar el main CSS de IDs únicos
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e293b;")
        
        self.welcome_label = QLabel("Bienvenido al sistema de automatización.\nSelecciona una opción en el menú para comenzar.")
        self.welcome_label.setWordWrap(True) # Para que el texto salte de línea si es largo
        self.welcome_label.setStyleSheet("font-size: 16px; color: #64748b; line-height: 150%;")

        layout.addWidget(self.title)
        layout.addWidget(self.welcome_label)
        layout.addStretch() # Empuja todo hacia arriba (como justify-start)

class FilesView(QWidget):
    """Vista para armar y ejecutar workflows de archivos."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
        
        self.title = QLabel("🛠️ Constructor de Workflow")
        self.title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1e293b;")
        
        # --- SECCIÓN DE ENTRADA ---
        input_layout = QHBoxLayout()
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Nombre del paso / carpeta...")
        self.folder_input.setMinimumHeight(40)
        
        self.btn_add_step = QPushButton("➕ Añadir Paso")
        self.btn_add_step.setCursor(Qt.PointingHandCursor)
        self.btn_add_step.setStyleSheet("""
            QPushButton { 
                background-color: #10b981; color: white; 
                padding: 10px; border-radius: 6px; font-weight: bold; 
            }
            QPushButton:hover { background-color: #059669; }
        """)
        
        input_layout.addWidget(self.folder_input)
        input_layout.addWidget(self.btn_add_step)

        # --- LISTA DE PASOS (Visual) ---
        self.label_lista = QLabel("Pasos a ejecutar:")
        self.steps_list = QListWidget() # Como un <ul id="task-list">
        self.steps_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.steps_list.setStyleSheet("""
            QListWidget { 
                border: 2px solid #e2e8f0; border-radius: 8px; 
                background: white; padding: 5px; color: #1e293b;
            }
        """)

        # --- ACCIONES ---
        self.btn_create = QPushButton("🚀 Ejecutar Workflow Completo")
        self.btn_create.setObjectName("primary_button")
        
        self.btn_clear = QPushButton("🗑️ Limpiar Todo")
        self.btn_clear.setCursor(Qt.PointingHandCursor)

        self.status_label = QLabel("Estado: Listo")
        self.status_label.setObjectName("status")
        
        # Agregamos todo al layout
        layout.addWidget(self.title)
        layout.addLayout(input_layout)
        layout.addWidget(self.label_lista)
        layout.addWidget(self.steps_list)
        layout.addWidget(self.btn_create)
        layout.addWidget(self.btn_clear)
        layout.addWidget(self.status_label)
        layout.addStretch()

        # Conectamos lógica interna de la UI
        self.btn_add_step.clicked.connect(self.agregar_a_la_lista)
        self.btn_clear.clicked.connect(self.steps_list.clear)

    def agregar_a_la_lista(self):
        texto = self.folder_input.text().strip()
        if texto:
            self.steps_list.addItem(texto) # Añade el texto a la lista visual
            self.folder_input.clear()
            self.folder_input.setFocus()