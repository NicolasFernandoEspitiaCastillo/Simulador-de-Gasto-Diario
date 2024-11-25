# generar_reporte.py
from collections import defaultdict
import archivo_datos

# Función para generar un reporte de los gastos
def generar_reporte():
    gastos = archivo_datos.cargar_datos()
    
    total_general = sum(gasto['cantidad'] for gasto in gastos)
    reporte = f"Reporte de Gastos\nTotal General: {total_general}\n\n"
    
    # Reporte por categorías
    gastos_por_categoria = defaultdict(float)
    for gasto in gastos:
        gastos_por_categoria[gasto['categoria']] += gasto['cantidad']
    
    reporte += "Gastos por Categoría:\n"
    for categoria, total in gastos_por_categoria.items():
        reporte += f"{categoria}: {total}\n"
    
    # Guardar reporte en archivo
    with open('reporte_gastos.txt', 'w') as archivo:
        archivo.write(reporte)
    
    print("Reporte generado y guardado en 'reporte_gastos.txt'.")
