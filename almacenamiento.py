import json

def guardar_empleados(lista_empleados):
    with open("empleados.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_empleados, archivo, indent=4, ensure_ascii=False)

def cargar_empleados():
    try:
        with open("empleados.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: el archivo de empleados esta dañado.")
        return []
