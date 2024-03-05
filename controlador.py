import mysql.connector

def dameDato():
    conexion = mysql.connector.connect(
        host='localhost',
        user='empresa',
        password='empresa',
        database='empresa'
        )
    cursor = conexion.cursor()
    peticion = 'SELECT productos.nombre FROM productos WHERE Identificador = 37'
    cursor.execute(peticion)
    fila = cursor.fetchone()
    return fila[0]
