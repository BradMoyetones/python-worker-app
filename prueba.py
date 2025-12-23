import json
from tabulate import tabulate

datos_leidos = []
usuarios = []
encabezados = ["index", "Nombre", "Edad"]

with open('base_datos.json', 'r', encoding='utf-8') as archivo_json:
    datos_leidos = json.load(archivo_json)

usuarios = datos_leidos['usuarios']
print("Lista de usuarios:")
# Usar tabulate de forma correcta porque pasando usuarios directamente da error
# print(tabulate(usuarios, headers=encabezados, tablefmt="grid"))
print(tabulate([[i, user['name'], user['age']] for i, user in enumerate(usuarios)], headers=encabezados, tablefmt="grid"))

commands = ["crear usuario", "eliminar usuario", "modificar usuario"]

for command in commands:
    # La persona debe ingresar el indice del comando
    print(f"Comando disponible: {command} -> digita {commands.index(command)} para seleccionarlo")

commands_input = input("Escribe un comando: ")

if commands_input.isdigit() and int(commands_input) < len(commands):
    comando_seleccionado = commands[int(commands_input)]
    print(f"Has seleccionado el comando: {comando_seleccionado}")
else:
    print("Comando no válido.")
    exit()

command_index = commands.index(comando_seleccionado)
if command_index == 0:
    print("Creando usuario...")
    name = input("Ingresa el nombre del nuevo usuario: ")
    age = input("Ingresa la edad del nuevo usuario: ")
    print(f"Usuario {name} de {age} años creado.")
    usuarios.append({"name": name, "age": age})
    with open('base_datos.json', 'w', encoding='utf-8') as archivo_json:
        json.dump({"usuarios": usuarios}, archivo_json, ensure_ascii=False, indent=4)
    print("Usuario guardado en la base de datos.")
elif command_index == 1:
    print("Eliminando usuario..")
    index = input("Ingresa el índice del usuario a eliminar: ")
    if index.isdigit() and int(index) < len(usuarios):
        usuario_eliminado = usuarios.pop(int(index))
        print(f"Usuario {usuario_eliminado['name']} eliminado.")
        with open('base_datos.json', 'w', encoding='utf-8') as archivo_json:
            json.dump({"usuarios": usuarios}, archivo_json, ensure_ascii=False, indent=4)
        print("Usuario eliminado de la base de datos.")
    else:
        print("Índice no válido.")
        exit()
elif command_index == 2:
    print("Modificando usuario...")
    index = input("Ingresa el índice del usuario a modificar: ")
    if index.isdigit() and int(index) < len(usuarios):
        nuevo_nombre = input("Ingresa el nuevo nombre: ")
        nueva_edad = input("Ingresa la nueva edad: ")
        usuarios[int(index)]['name'] = nuevo_nombre
        usuarios[int(index)]['age'] = nueva_edad
        print(f"Usuario modificado a {nuevo_nombre}, {nueva_edad} años.")
        with open('base_datos.json', 'w', encoding='utf-8') as archivo_json:
            json.dump({"usuarios": usuarios}, archivo_json, ensure_ascii=False, indent=4)
        print("Usuario modificado en la base de datos.")
    else:
        print("Índice no válido.")
        exit()



