from PySide6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, 
    QWidget, QFrame, QStackedWidget
)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer

# Importamos nuestras vistas (pestañas)
from app.ui.views import HomeView, FilesView

import os
import sys

def resource_path(relative_path):
    """ Obtiene la ruta absoluta para recursos, funciona para dev y PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Worker App Pro")
        self.resize(900, 650) # Un poco más grande para comodidad

        # --- ESTADO INTERNO ---
        self.is_expanded = True
        self.sidebar_buttons = [] # Lista para iterar los botones fácilmente

        # --- 1. CONTENEDOR RAIZ ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal horizontal: [ Sidebar | Stack de Páginas ]
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- 2. SIDEBAR (Panel Lateral) ---
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(200) # Ancho inicial (w-52 aprox)
        
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(8)

        # 2.1 Botón Toggle (Hamburguesa)
        self.btn_toggle = QPushButton("  Ocultar")
        self.btn_toggle.setObjectName("toggle_btn")
        icon_menu = self.get_colored_icon(resource_path("assets/menu.svg"), "#cbd5e1")
        self.btn_toggle.setIcon(icon_menu)
        self.btn_toggle.setCursor(Qt.PointingHandCursor)
        self.btn_toggle.clicked.connect(self.toggle_sidebar)

        sidebar_layout.addWidget(self.btn_toggle)

        # 2.2 Botones de Navegación
        self.add_sidebar_button(sidebar_layout, "Inicio", "assets/home.svg")
        self.add_sidebar_button(sidebar_layout, "Archivos", "assets/file.svg")
        self.add_sidebar_button(sidebar_layout, "Configuración", "assets/settings.svg")

        sidebar_layout.addStretch() # Empuja botones hacia arriba

        # --- 3. ÁREA DE CONTENIDO (Router) ---
        self.pages = QStackedWidget()
        self.pages.setObjectName("content")

        # Instanciamos las páginas
        self.home_page = HomeView()
        self.files_page = FilesView()

        # Las añadimos al Stack (Se manejan por índice: 0, 1, 2...)
        self.pages.addWidget(self.home_page) # Índice 0
        self.pages.addWidget(self.files_page) # Índice 1

        # Ensamblamos todo en el layout principal
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages)

        # --- 4. CONEXIÓN DE NAVEGACIÓN ---
        # Al hacer clic en los botones, cambiamos el índice del StackedWidget
        self.sidebar_buttons[0].clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.sidebar_buttons[1].clicked.connect(lambda: self.pages.setCurrentIndex(1))

        # --- 5. SISTEMA DE ANIMACIÓN ---
        # Animamos la propiedad minimumWidth para que el colapso sea suave
        self.anim = QPropertyAnimation(self.sidebar, b"minimumWidth")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.apply_styles()
    
    def add_sidebar_button(self, layout, text, icon_path):
        """Helper para estandarizar la creación de botones en el menú."""
        btn = QPushButton(f"  {text}")
        icon = self.get_colored_icon(resource_path(icon_path), "#cbd5e1")
        btn.setIcon(icon) 
        btn.setIconSize(QSize(18, 18))
        btn.setProperty("original_text", f"  {text}") 
        btn.setCursor(Qt.PointingHandCursor)
        
        layout.addWidget(btn)
        self.sidebar_buttons.append(btn)

    def toggle_sidebar(self):
        """Lógica para encoger/expandir la barra lateral con animación."""
        width_start = self.sidebar.width()
        
        if self.is_expanded:
            width_end = 65
            self.btn_toggle.setText("")
            for btn in self.sidebar_buttons:
                btn.setToolTip(btn.property("original_text").strip())
                btn.setText("")
        else:
            width_end = 200
            self.btn_toggle.setText("  Ocultar")
            for btn in self.sidebar_buttons:
                btn.setToolTip("")
                btn.setText(btn.property("original_text"))

        # Disparamos la transición
        self.anim.setStartValue(width_start)
        self.anim.setEndValue(width_end)
        self.anim.start()
        
        self.sidebar.setMaximumWidth(width_end) # Asegura que no sobrepase el límite
        self.is_expanded = not self.is_expanded
    
    def get_colored_icon(self, svg_path, color_hex):
        """Pinta un SVG dinámicamente. Evita tener que editar archivos .svg manualmente."""
        renderer = QSvgRenderer(svg_path)
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor(color_hex))
        painter.end()
        return QIcon(pixmap)

    def apply_styles(self):
        """El CSS global de la aplicación (QSS)."""
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', Tahoma, sans-serif;
                font-size: 14px;
            }
            #sidebar {
                background-color: #0f172a; /* Slate 950 */
                border-right: 1px solid #1e293b;
            }
            #sidebar QPushButton {
                background-color: transparent;
                color: #94a3b8;
                text-align: left;
                padding: 12px;
                border: none;
                border-radius: 6px;
                font-weight: 500;
            }
            #sidebar QPushButton:hover {
                background-color: #1e293b;
                color: #f8fafc;
            }
            #content {
                background-color: #f8fafc; /* Slate 50 */
            }
            #primary_button {
                background-color: #3b82f6; /* Blue 500 */
                color: white;
                padding: 10px 15px;
                border-radius: 6px;
                font-weight: bold;
                border: none;
            }
            #primary_button:hover { background-color: #2563eb; }
            #primary_button:pressed { background-color: #1d4ed8; }
            
            #status {
                color: #64748b;
                font-style: italic;
                padding: 5px;
            }
        """)