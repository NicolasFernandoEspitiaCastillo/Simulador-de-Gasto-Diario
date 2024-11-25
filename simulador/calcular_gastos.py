
from collections import defaultdict
import archivo_datos

# Calcular los gastos totales y por categoría
def calcular_gastos_totales():
    gastos = archivo_datos.cargar_datos()
    
    # Calcular el total general
    total_general = sum(gasto['cantidad'] for gasto in gastos)
    print(f"Gasto Total: {total_general}")

    # Calcular los gastos por categoría
    gastos_por_categoria = defaultdict(float)
    for gasto in gastos:
        gastos_por_categoria[gasto['categoria']] += gasto['cantidad']
    
    print("Gasto por categoría:")
    for categoria, total in gastos_por_categoria.items():
        print(f"{categoria}: {total}")
