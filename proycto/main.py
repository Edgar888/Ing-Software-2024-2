from funciones import *

def mostrar_menu():
    print("Menú:")
    print("1. Ver registros de una tabla")
    print("2. Filtrar registros de una tabla por ID")
    print("3. Actualizar columna nombre de un registro")
    print("4. Eliminar un registro por ID o todos los registros")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tabla = input("Ingrese el nombre de la tabla: ")
            mostrar_registros(tabla)
        elif opcion == '2':
            tabla = input("Ingrese el nombre de la tabla: ")
            id = int(input("Ingrese el ID a filtrar: "))
            filtrar_registros_por_id(tabla, id)
        elif opcion == '3':
            tabla = input("Ingrese el nombre de la tabla: ")
            id = int(input("Ingrese el ID del registro a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_nombre(tabla, id, nuevo_nombre)
        elif opcion == '4':
            tabla = input("Ingrese el nombre de la tabla: ")
            opcion_eliminar = input("¿Desea eliminar un registro por ID o todos los registros? (ID/Todos): ")
            if opcion_eliminar.lower() == 'id':
                id = int(input("Ingrese el ID del registro a eliminar: "))
                eliminar_registro_por_id(tabla, id)
            elif opcion_eliminar.lower() == 'todos':
                eliminar_todos_registros(tabla)
            else:
                print("Opción inválida.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

