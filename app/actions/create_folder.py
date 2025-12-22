import os

class CreateFolderAction:
    def __init__(self, folder_name="nueva_carpeta"):
        self.folder_name = folder_name

    def run(self):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            return f"Carpeta '{self.folder_name}' creada con éxito."
        return "La carpeta ya existe."