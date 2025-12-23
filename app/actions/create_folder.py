import os
from pathlib import Path

class CreateFolderAction:
    """Acción encargada de la creación física de directorios."""
    def __init__(self, folder_name="nueva_carpeta"):
        self.folder_name = folder_name

    def run(self):
        # Usamos Path (pathlib) porque es más moderno y seguro que os.path
        path = Path(self.folder_name)
        
        try:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                return f"✅ Carpeta '{self.folder_name}' creada con éxito."
            return f"⚠️ La carpeta '{self.folder_name}' ya existe."
        except Exception as e:
            # Capturamos errores de permisos o caracteres inválidos
            return f"❌ Error: {str(e)}"