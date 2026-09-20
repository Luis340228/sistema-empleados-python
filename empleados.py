def mostrar_empleado(empleado):
    bono, salario_con_bono = calcular_bono(
        empleado["salario"],
        empleado["antiguedad"]
    )

    print(f"ID: {empleado['id']}")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Puesto: {empleado['puesto']}")
    print(f"Salario: ${empleado['salario']:.2f}")
    print(f"Antiguedad: {empleado['antiguedad']}")
    print(f"Bono: ${bono:.2f}")
    print(f"Salario + bono: ${salario_con_bono:.2f}")

def mostrar_empleados(lista_empleados):
    print("\n--- LISTA DE EMPLEADOS ---")

    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    for empleado in lista_empleados:
        mostrar_empleado(empleado)
        print("-" * 30)

def solicitar_nombre_busqueda():
    print("\n--- BUSCAR EMPLEADO ---")

    nombre_buscar = input(
        "Nombre del empleado a buscar: "
    ).strip()

    return nombre_buscar

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

def registrar_empleado():
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

    return nombre, puesto, salario, antiguedad

def editar_empleado(empleado):
    print("\n--- EDITAR EMPLEADO---")

    print("\nDeja vacío el dato que no quieras modificar.")

    nuevo_nombre = input(
        f"Nombre [{empleado['nombre']}]: "
    ).strip()

    if nuevo_nombre == "":
        nuevo_nombre = empleado["nombre"]

    nuevo_puesto = input(
        f"Puesto [{empleado['puesto']}]: "
    ).strip()

    if nuevo_puesto == "":
        nuevo_puesto = empleado["puesto"]

    while True:
        nuevo_salario = input(
            f"Salario [{empleado['salario']}]: "
        ).strip()

        if nuevo_salario == "":
            nuevo_salario = empleado["salario"]
            break

        try:
            nuevo_salario = float(nuevo_salario)

            if nuevo_salario <= 0:
                print("El salario debe ser mayor a 0.")
                continue

            break

        except ValueError:
            print("Debes escribir un salario válido.")

    while True:
        nueva_antiguedad = input(
            f"Antiguedad [{empleado['antiguedad']}]: "
        ).strip()

        if nueva_antiguedad == "":
            nueva_antiguedad = empleado["antiguedad"]
            break

        try:
            nueva_antiguedad = int(nueva_antiguedad)

            if nueva_antiguedad < 0:
                print("La antiguedad debe ser mayor a 0.")
                continue

            break

        except ValueError:
            print("Debes escribir una antiguedad válida.")

    return (
        nuevo_nombre,
        nuevo_puesto,
        nuevo_salario,
        nueva_antiguedad,
    )

def solicitar_id_eliminar():
    print("\n--- ELIMINAR EMPLEADO---")

    while True:
        try:
            id_empleado = int(
                input("ID del empleado a eliminar: ")
            )
            return id_empleado

        except ValueError:
            print("Debes escribir un ID valido")