import json
from datetime import datetime

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

# Función para registrar un nuevo gasto
def registrar_gasto():
    cantidad = float(input("Ingrese la cantidad del gasto: "))
    categoria = input("Ingrese la categoría del gasto (ej. comida, transporte): ")
    descripcion = input("Ingrese una breve descripción (opcional): ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuevo_gasto = {
        "cantidad": cantidad,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": fecha
    }
    
    gastos = cargar_datos()
    gastos.append(nuevo_gasto)
    guardar_datos(gastos)
    print("Gasto registrado exitosamente.")

