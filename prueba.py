import json
from tabulate import tabulate
from colorama import Fore, Style
from colorama import just_fix_windows_console
import time
import os

just_fix_windows_console()

DB_PATH = "base_datos.json"
ENCABEZADOS = ["Index", "Nombre", "Edad"]
COMMANDS = ["Crear usuario", "Eliminar usuario", "Modificar usuario", "Salir"]

# Limpia la consola según el sistema operativo
def clear():
    os.system("cls" if os.name == "nt" else "clear")

import time

def pause_with_dots(seconds=2, message="Volviendo al menú"):
    states = [".", "..", "..."]
    iterations = int(seconds / 0.5)

    for i in range(iterations):
        dots = states[i % len(states)]
        print_colored(f"\r{message}{dots}", "yellow", end="")
        time.sleep(0.5)

    # Limpia la línea al final
    print_colored("\r" + " " * (len(message) + 5), "yellow", end="\r")

def print_colored(text, color="white", end="\n"):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    print(colors.get(color, Fore.WHITE) + text + Style.RESET_ALL, end=end, flush=True)

def print_title():
    print_colored(r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║    ██████╗██╗     ██╗    ██╗   ██╗███████╗██████╗    ║
║   ██╔════╝██║     ██║    ██║   ██║██╔════╝██╔══██╗   ║
║   ██║     ██║     ██║    ██║   ██║█████╗  ██████╔╝   ║
║   ██║     ██║     ██║    ██║   ██║██╔══╝  ██╔══██╗   ║
║   ╚██████╗███████╗██║    ╚██████╔╝███████╗██║  ██║   ║
║    ╚═════╝╚══════╝╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝   ║
║                                                      ║
║           USER MANAGER CLI · JSON DB v1.0            ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""", "cyan")
    print("\n ")

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
        print_colored("No hay usuarios registrados.\n", "yellow")
        return

    tabla = [
        [i, user["name"], user["age"]]
        for i, user in enumerate(usuarios)
    ]

    print_colored(tabulate(tabla, headers=ENCABEZADOS, tablefmt="grid"))
    print()

def mostrar_menu():
    print("Comandos disponibles:")
    for i, cmd in enumerate(COMMANDS):
        print_colored(f"[{i}] -> {cmd}", "green")

def crear_usuario(usuarios):
    name = input("Nombre: ").strip()
    age = input("Edad: ").strip()

    if not age.isdigit():
        print_colored("Edad no válida.\n", "red")
        pause_with_dots()
        return

    usuarios.append({
        "name": name,
        "age": int(age)
    })

    guardar_db(usuarios)
    print_colored("Usuario creado correctamente.\n", "green")
    pause_with_dots()

def eliminar_usuario(usuarios):
    index = input("Índice del usuario a eliminar: ")

    if not index.isdigit() or int(index) >= len(usuarios):
        print_colored("Índice no válido.\n", "red")
        pause_with_dots()
        return

    eliminado = usuarios.pop(int(index))
    guardar_db(usuarios)

    print_colored(f"Usuario '{eliminado['name']}' eliminado.\n", "red")
    pause_with_dots()

def modificar_usuario(usuarios):
    index = input("Índice del usuario a modificar: ")

    if not index.isdigit() or int(index) >= len(usuarios):
        print_colored("Índice no válido.\n", "red")
        return

    name = input("Nuevo nombre: ").strip()
    age = input("Nueva edad: ").strip()

    if not age.isdigit():
        print_colored("Edad no válida.\n", "red")
        pause_with_dots()
        return

    usuarios[int(index)]["name"] = name
    usuarios[int(index)]["age"] = int(age)

    guardar_db(usuarios)
    print_colored("Usuario modificado correctamente.\n", "green")
    pause_with_dots()

def main():
    print_title()
    usuarios = cargar_db()

    while True:
        clear()
        mostrar_usuarios(usuarios)
        mostrar_menu()

        opcion = input("\nSelecciona una opción: ")

        if not opcion.isdigit():
            print_colored("Opción no válida.\n", "red")
            pause_with_dots()
            continue

        opcion = int(opcion)

        if opcion == 0:
            crear_usuario(usuarios)
        elif opcion == 1:
            eliminar_usuario(usuarios)
        elif opcion == 2:
            modificar_usuario(usuarios)
        elif opcion == 3:
            print_colored("Saliendo de la aplicación 👋", "yellow")
            pause_with_dots(1, "Cerrando")
            break
        else:
            print_colored("Opción no válida.\n", "red")
            pause_with_dots()

main()