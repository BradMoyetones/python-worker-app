from PySide6.QtCore import QThread, Signal

class ActionRunner(QThread):
    """
    Este es nuestro 'Worker Thread'. 
    Hereda de QThread para poder correr en un hilo separado de la UI.
    """
    # Definimos señales (como eventos personalizados en Node)
    # Signal(tipo_de_dato)
    finished = Signal(str)  # Se emite al terminar, envía el mensaje de resultado
    error = Signal(str)     # Se emite si algo sale mal

    def __init__(self, action_object):
        super().__init__()
        self.action = action_object

    def run(self):
        """
        Todo lo que pongas aquí adentro se ejecutará en el 
        hilo secundario, SIN congelar la ventana.
        """
        try:
            # Ejecutamos la acción (la que pasamos por constructor)
            result = self.action.run()
            
            # 'Emitimos' el resultado para que la UI lo reciba
            self.finished.emit(result)
        except Exception as e:
            # Si hay un crash, enviamos el error
            self.error.emit(str(e))