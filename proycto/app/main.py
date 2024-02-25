from funciones import *

def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Ver registros de una tabla")
    print("2. Filtrar registros por ID")
    print("3. Actualizar fecha de renta")
    print("4. Eliminar registro(s)")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tabla = input("Ingrese el nombre de la tabla: ")
            ver_registros(tabla)
        elif opcion == "2":
            tabla = input("Ingrese el nombre de la tabla: ")
            id = int(input("Ingrese el ID a filtrar: "))
            filtrar_registros(tabla, id)
        elif opcion == "3":
            actualizar_fecha_renta()
        elif opcion == "4":
            tabla = input("Ingrese el nombre de la tabla: ")
            id = int(input("Ingrese el ID a eliminar (ingrese 0 para eliminar todos los registros): "))
            eliminar_registro(tabla, id)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

