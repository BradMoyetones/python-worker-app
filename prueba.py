import json
from tabulate import tabulate

DB_PATH = "base_datos.json"
ENCABEZADOS = ["Index", "Nombre", "Edad"]
COMMANDS = ["crear usuario", "eliminar usuario", "modificar usuario", "salir"]

def cargar_db():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("usuarios", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_db(usuarios):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump({"usuarios": usuarios}, f, ensure_ascii=False, indent=4)

def mostrar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return

    tabla = [
        [i, user["name"], user["age"]]
        for i, user in enumerate(usuarios)
    ]

    print(tabulate(tabla, headers=ENCABEZADOS, tablefmt="grid"))
    print()

def mostrar_menu():
    print("Comandos disponibles:")
    for i, cmd in enumerate(COMMANDS):
        print(f"[{i}] {cmd}")

def crear_usuario(usuarios):
    name = input("Nombre: ").strip()
    age = input("Edad: ").strip()

    if not age.isdigit():
        print("Edad no válida.\n")
        return

    usuarios.append({
        "name": name,
        "age": int(age)
    })

    guardar_db(usuarios)
    print("Usuario creado correctamente.\n")

def eliminar_usuario(usuarios):
    index = input("Índice del usuario a eliminar: ")

    if not index.isdigit() or int(index) >= len(usuarios):
        print("Índice no válido.\n")
        return

    eliminado = usuarios.pop(int(index))
    guardar_db(usuarios)

    print(f"Usuario '{eliminado['name']}' eliminado.\n")

def modificar_usuario(usuarios):
    index = input("Índice del usuario a modificar: ")

    if not index.isdigit() or int(index) >= len(usuarios):
        print("Índice no válido.\n")
        return

    name = input("Nuevo nombre: ").strip()
    age = input("Nueva edad: ").strip()

    if not age.isdigit():
        print("Edad no válida.\n")
        return

    usuarios[int(index)]["name"] = name
    usuarios[int(index)]["age"] = int(age)

    guardar_db(usuarios)
    print("Usuario modificado correctamente.\n")

def main():
    print("""
====================================
     USER MANAGER CLI v1.0
====================================
""")

    usuarios = cargar_db()

    while True:
        mostrar_usuarios(usuarios)
        mostrar_menu()

        opcion = input("\nSelecciona una opción: ")

        if not opcion.isdigit():
            print("Opción no válida.\n")
            continue

        opcion = int(opcion)

        if opcion == 0:
            crear_usuario(usuarios)
        elif opcion == 1:
            eliminar_usuario(usuarios)
        elif opcion == 2:
            modificar_usuario(usuarios)
        elif opcion == 3:
            print("Saliendo de la aplicación 👋")
            break
        else:
            print("Opción no válida.\n")

main()