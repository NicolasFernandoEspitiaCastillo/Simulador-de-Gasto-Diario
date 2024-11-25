# registrar_gasto.py
from datetime import datetime
import archivo_datos

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
    
    gastos = archivo_datos.cargar_datos()
    gastos.append(nuevo_gasto)
    archivo_datos.guardar_datos(gastos)
    print("Gasto registrado exitosamente.")
