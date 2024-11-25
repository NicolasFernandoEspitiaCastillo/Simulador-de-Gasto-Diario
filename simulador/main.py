
import registrar_gasto
import listar_gastos
import calcular_gastos
import generar_reporte

def iniciar_simulador():
    while True:
        print("\n--- Simulador de Gasto Diario ---")
        print("1. Registrar Gasto")
        print("2. Listar Gastos")
        print("3. Calcular Gastos Totales")
        print("4. Generar Reporte")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_gasto.registrar_gasto()
        elif opcion == '2':
            listar_gastos.listar_gastos()
        elif opcion == '3':
            calcular_gastos.calcular_gastos_totales()
        elif opcion == '4':
            generar_reporte.generar_reporte()
        elif opcion == '5':
            print("Saliendo del simulador...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función principal
if __name__ == "__main__":
    iniciar_simulador()
