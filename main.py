from empleados import (
    registrar_empleado,
    mostrar_empleados,
    editar_empleado,
    solicitar_id_eliminar,
    solicitar_nombre_busqueda,
)

from base_datos import (
    crear_base_datos,
    insertar_empleado,
    obtener_empleados,
    buscar_empleados_por_nombre,
    obtener_empleado_por_id,
    eliminar_empleado_db, actualizar_empleado,
)

from empleados import mostrar_empleado

def main():
    crear_base_datos()

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
            nombre, puesto, salario, antiguedad = registrar_empleado()

            insertar_empleado(
                nombre,
                puesto,
                salario,
                antiguedad
            )

            print("Empleado registrado correctamente.")

        elif opcion == "2":
            empleados = obtener_empleados()
            mostrar_empleados(empleados)

        elif opcion == "3":
            nombre_buscar = solicitar_nombre_busqueda()

            empleados_encontrados = buscar_empleados_por_nombre(
                nombre_buscar
            )

            if empleados_encontrados:
                mostrar_empleados(empleados_encontrados)
            else:
                print("Empleado no encontrado.")

        elif opcion == "4":
            while True:
                try:
                    id_empleado = int(
                        input("ID del empleado a editar: ")
                    )
                    break
                except ValueError:
                    print("Debes escribir un ID válido.")

            empleado = obtener_empleado_por_id(id_empleado)

            if empleado is None:
                print("No existe un empleado con ese ID.")
                continue

            print("\nEmpleado encontrado:")
            mostrar_empleado(empleado)

            nombre, puesto, salario, antiguedad = editar_empleado(
                empleado
            )

            actualizar_empleado(
                id_empleado,
                nombre,
                puesto,
                salario,
                antiguedad
            )

            print("\nEmpleado actualizado correctamente.")

            empleado_actualizado = obtener_empleado_por_id(id_empleado)
            mostrar_empleado(empleado_actualizado)

        elif opcion == "5":
            id_empleado = solicitar_id_eliminar()

            empleado = obtener_empleado_por_id(id_empleado)

            if empleado is None:
                print("No existe un empleado con ese ID.")
                continue

            print("\nEmpleado encontrado:")
            mostrar_empleado(empleado)

            confirmar = input(
                "¿Deseas eliminar este empleado? (s/n): "
            ).strip().lower()

            if confirmar == "s":
                eliminar_empleado_db(id_empleado)
                print("Empleado eliminado correctamente.")
            else:
                print("Operación cancelada.")

        elif opcion == "6":
            print("\n--- CERRANDO PROGRAMA ---")
            break

        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()