# listar_gastos.py
import archivo_datos

# Función para listar todos los gastos
def listar_gastos():
    gastos = archivo_datos.cargar_datos()
    categoria = input("Ingrese una categoría para filtrar (deje vacío para ver todos): ")
    fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD) para filtrar o deje vacío: ")
    fecha_fin = input("Ingrese fecha de fin (YYYY-MM-DD) para filtrar o deje vacío: ")

    for gasto in gastos:
        if (categoria and categoria != gasto['categoria']) or \
           (fecha_inicio and gasto['fecha'] < fecha_inicio) or \
           (fecha_fin and gasto['fecha'] > fecha_fin):
            continue
        print(f"{gasto['fecha']} - {gasto['categoria']} - {gasto['cantidad']} - {gasto['descripcion']}")
