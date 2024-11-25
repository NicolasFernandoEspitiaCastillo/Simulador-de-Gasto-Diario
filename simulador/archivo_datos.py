# archivo_datos.py
import json

# Cargar los datos desde el archivo JSON
def cargar_datos():
    try:
        with open('gastos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Guardar los datos en el archivo JSON
def guardar_datos(gastos):
    with open('gastos.json', 'w') as archivo:
        json.dump(gastos, archivo, indent=4)
