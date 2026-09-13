from empleados import (
    registrar_empleado,
    mostrar_empleados,
    buscar_empleado,
    editar_empleado,
    eliminar_empleado,
)

from almacenamiento import (
    cargar_empleados,
    guardar_empleados,
)

def main():
    empleados = cargar_empleados()

    if empleados:
        siguiente_id = max(empleado["id"] for empleado in empleados) + 1
    else:
        siguiente_id = 1

    while True:
        print("\n" + "=" * 35)
        print("     SISTEMA DE EMPLEADOS")
        print("=" * 35)

        print("1. Registrar empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado")
        print("4. Editar empleado")
        print("5. Eliminar empleado")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_empleado = registrar_empleado(siguiente_id)
            empleados.append(nuevo_empleado)
            siguiente_id += 1

            guardar_empleados(empleados)

        elif opcion == "2":
            mostrar_empleados(empleados)

        elif opcion == "3":
            buscar_empleado(empleados)

        elif opcion == "4":
            editar_empleado(empleados)
            guardar_empleados(empleados)

        elif opcion == "5":
            eliminar_empleado(empleados)
            guardar_empleados(empleados)

        elif opcion == "6":
            print("\n--- CERRANDO PROGRAMA ---")
            break

        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()