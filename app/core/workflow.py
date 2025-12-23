class Workflow:
    """
    El Workflow es como una 'lista de reproducción' de acciones.
    Toma varias tareas y las ejecuta en orden secuencial.
    """
    def __init__(self, name="Proceso Secuencial"):
        self.name = name
        self.steps = [] # Aquí guardaremos los objetos de acción (CreateFolderAction, etc.)

    def add_step(self, action_object):
        """Añade una nueva tarea a la cola del workflow."""
        self.steps.append(action_object)
        return self # Esto permite 'encadenar' como en JS: workflow.add().add()

    def run(self):
        """
        Ejecuta todos los pasos uno tras otro.
        Si uno falla, devuelve el error. Si todos terminan, avisa.
        """
        resultados = []
        for i, step in enumerate(self.steps):
            # Ejecutamos cada acción (todas deben tener un método .run())
            try:
                res = step.run()
                resultados.append(f"Paso {i+1}: {res}")
            except Exception as e:
                return f"❌ Falló en el paso {i+1}: {str(e)}"
        
        # Unimos todos los mensajes de éxito
        return "\n".join(resultados)