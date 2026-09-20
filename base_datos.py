import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puesto TEXT NOT NULL,
            salario REAL NOT NULL,
            antiguedad INTEGER NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

def insertar_empleado(nombre, puesto, salario, antiguedad):
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO empleados (nombre, puesto, salario, antiguedad)
        VALUES (?, ?, ?, ?)
    """, (nombre, puesto, salario, antiguedad))

    conexion.commit()
    conexion.close()

def obtener_empleados():
    conexion = sqlite3.connect("empleados.db")
    conexion.row_factory = sqlite3.Row

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM empleados")

    empleados = cursor.fetchall()

    conexion.close()

    return empleados

def buscar_empleados_por_nombre(nombre):
    conexion = sqlite3.connect("empleados.db")
    conexion.row_factory = sqlite3.Row

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM empleados
        WHERE nombre LIKE ?
    """, (f"%{nombre}%",))

    empleados = cursor.fetchall()

    conexion.close()

    return empleados

def obtener_empleado_por_id(id_empleado):
    conexion = sqlite3.connect("empleados.db")
    conexion.row_factory = sqlite3.Row

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM empleados
        WHERE id = ?
    """, (id_empleado,))

    empleado = cursor.fetchone()

    conexion.close()

    return empleado

def eliminar_empleado_db(id_empleado):
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM empleados
        WHERE id = ?
    """, (id_empleado,))

    conexion.commit()
    conexion.close()

def actualizar_empleado(
        id_empleado,
        nombre,
        puesto,
        salario,
        antiguedad
):
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
                   UPDATE empleados
                   set nombre = ?, puesto = ?, salario = ?, antiguedad = ?
                   WHERE id = ?
    """, (
        nombre,
        puesto,
        salario,
        antiguedad,
        id_empleado
    ))

    conexion.commit()
    conexion.close()