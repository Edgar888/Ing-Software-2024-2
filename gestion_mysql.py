import pymysql

# Establecer conexión con la base de datos
def conectar():
    conexion = pymysql.connect(
        host='localhost',
        user='usuario',
        password='contraseña',
        database='nombre_base_datos'
    )
    return conexion

# Función para insertar registros en todas las tablas
def insertar_registros():
    conexion = conectar()
    cursor = conexion.cursor()

    # Insertar registros en tabla Usuario
    cursor.execute("INSERT INTO Usuario (nombre, apellido) VALUES ('Juan', 'Perez')")
    cursor.execute("INSERT INTO Usuario (nombre, apellido) VALUES ('Maria', 'Gonzalez')")

    # Insertar registros en tabla Pelicula
    cursor.execute("INSERT INTO Pelicula (nombre, genero) VALUES ('Titanic', 'Drama')")
    cursor.execute("INSERT INTO Pelicula (nombre, genero) VALUES ('Matrix', 'Ciencia Ficción')")

    # Insertar registros en tabla Rentar
    cursor.execute("INSERT INTO Rentar (idUsuario, idPelicula, fecha_renta) VALUES (1, 1, '2024-01-01')")
    cursor.execute("INSERT INTO Rentar (idUsuario, idPelicula, fecha_renta) VALUES (2, 2, '2024-01-02')")

    conexion.commit()
    conexion.close()

# Función para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(apellido):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM Usuario WHERE apellido LIKE '%{apellido}'")

    usuarios = cursor.fetchall()

    conexion.close()
    return usuarios

# Función para cambiar el género de una película
def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(f"UPDATE Pelicula SET genero = '{nuevo_genero}' WHERE nombre = '{nombre_pelicula}'")

    conexion.commit()
    conexion.close()

# Función para eliminar rentas anteriores a 3 días
def eliminar_rentas_antiguas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM Rentar WHERE fecha_renta <= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")

    conexion.commit()
    conexion.close()

# Ejemplo de uso
insertar_registros()

apellido_filtrar = input("Ingrese el apellido para filtrar usuarios: ")
usuarios_filtrados = filtrar_usuarios_por_apellido(apellido_filtrar)
print("Usuarios con apellido que termina en", apellido_filtrar, ":", usuarios_filtrados)

nombre_pelicula = input("Ingrese el nombre de la película a actualizar: ")
nuevo_genero = input("Ingrese el nuevo género para la película: ")
cambiar_genero_pelicula(nombre_pelicula, nuevo_genero)

eliminar_rentas_antiguas()
print("Rentas antiguas eliminadas.")

