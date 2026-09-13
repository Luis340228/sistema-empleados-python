def mostrar_empleado(empleado):
    print(f"ID: {empleado['id']}")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Puesto: {empleado['puesto']}")
    print(f"Salario: ${empleado['salario']:.2f}")
    print(f"Antiguedad: {empleado['antiguedad']}")
    print(f"Bono: ${empleado['bono']:.2f}")
    print(f"Salario + bono: ${empleado['salario_con_bono']:.2f}")

def mostrar_empleados(lista_empleados):
    print("\n--- LISTA DE EMPLEADOS ---")

    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    for empleado in lista_empleados:
        mostrar_empleado(empleado)
        print("-" * 30)

def buscar_empleado(lista_empleados):
    print("\n--- BUSCAR EMPLEADO ---")

    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    nombre_buscar = input("Nombre del empleado a buscar: ").strip()

    encontrado = False

    for empleado in lista_empleados:
        if nombre_buscar.lower() in empleado["nombre"].lower():
            print("\nEmpleado encontrado:")
            mostrar_empleado(empleado)

            encontrado = True
            break

    if not encontrado:
        print("Empleado no encontrado.")

def calcular_bono(salario, antiguedad):
    if antiguedad < 2:
        porcentaje_bono = 0.05
    elif antiguedad <= 5:
        porcentaje_bono = 0.10
    else:
        porcentaje_bono = 0.15

    bono = salario * porcentaje_bono
    salario_con_bono = salario + bono

    return bono, salario_con_bono

def registrar_empleado(id_empleado):
    print("\n--- REGISTRAR EMPLEADO ---")

    while True:
        nombre = input("Nombre del empleado: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacio")
            continue

        break

    while True:
        puesto = input("Puesto: ").strip()
        if puesto == "":
            print("El puesto no puede estar vacío")
            continue

        break

    while True:
        try:
            salario = float(input("Salario: "))

            if salario <= 0:
                print("El salario debe ser mayor a 0")
                continue

            break
        except ValueError:
            print("Error: escribe un número válido.")

    while True:
        try:
            antiguedad = int(input("Años trabajando en la empresa: "))

            if antiguedad < 0:
                print("La antigüedad no puede ser negativa")
                continue

            break

        except ValueError:
            print("Error: escribe un número entero")

    bono, salario_con_bono = calcular_bono(salario, antiguedad)

    empleado = {
        "id" : id_empleado,
        "nombre": nombre,
        "puesto": puesto,
        "salario": salario,
        "antiguedad": antiguedad,
        "bono": bono,
        "salario_con_bono": salario_con_bono
    }

    return empleado

def editar_empleado(lista_empleados):
    print("\n--- EDITAR EMPLEADO---")

    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    while True:
        try:
            id_buscar = int(input("ID del empleado a editar: "))
            break
        except ValueError:
            print("Debes escribir un ID valido")

    for empleado in lista_empleados:
        if empleado["id"] == id_buscar:
            print("\nEmpleado encontrado:")
            mostrar_empleado(empleado)

            print("\nDeja vacío el dato que no quieras modificar.")

            nuevo_nombre = input(
                f"Nombre [{empleado['nombre']}]: "
            ).strip()

            if nuevo_nombre != "":
                empleado["nombre"] = nuevo_nombre

            nuevo_puesto = input(
                f"Puesto [{empleado['puesto']}]: "
            ).strip()

            if nuevo_puesto != "":
                empleado["puesto"] = nuevo_puesto

            nuevo_salario = input(
                f"Salario [{empleado['salario']}]: "
            ).strip()

            if nuevo_salario != "":
                try:
                    nuevo_salario = float(nuevo_salario)

                    if nuevo_salario > 0:
                        empleado["salario"] = nuevo_salario
                    else:
                        print("El salario debe ser mayor a 0.")

                except ValueError:
                    print("El salario no fue modificado porque no es válido.")

            nueva_antiguedad = input(
                f"Antiguedad [{empleado['antiguedad']}]: "
            ).strip()

            if nueva_antiguedad != "":
                try:
                    nueva_antiguedad = int(nueva_antiguedad)

                    if nueva_antiguedad >= 0:
                        empleado["antiguedad"] = nueva_antiguedad
                    else:
                        print("La antiguedad no puede ser negativa.")

                except ValueError:
                    print("La antiguedad no puede ser modificada porque no es valida.")

            bono, salario_con_bono = calcular_bono(
                empleado["salario"],
                empleado["antiguedad"]
            )

            empleado["bono"] = bono
            empleado["salario_con_bono"] = salario_con_bono

            print("\nEmpleado actualizado:")
            mostrar_empleado(empleado)

            return

    print("No existe un empleado con ese ID.")

def eliminar_empleado(lista_empleados):
    print("\n--- ELIMINAR EMPLEADO---")

    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    while True:
        try:
            id_buscar = int(input("ID del empleado a eliminar: "))
            break
        except ValueError:
            print("Debes escribir un ID valido.")

    for empleado in lista_empleados:
        if empleado["id"] == id_buscar:
            print("\nEmpleado encontrado:")
            mostrar_empleado(empleado)

            confirmar = input("¿Deseas eliminar este empleado? (s/n): ").strip().lower()

            if confirmar == "s":
                lista_empleados.remove(empleado)
                print("Empleado eliminado correctamente.")
            else:
                print("Operación cancelada.")

            return

    print("No existe un empleado con ese ID.")
