import mysql.connector

# Conexión a la base de datos remota
remote_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7778742049",
    database="JAM"
)

# Cursor para ejecutar consultas
cursor = remote_db.cursor()

# Consulta para seleccionar los datos de la tabla
query = "SELECT * FROM JAM.'27_04_24'"
cursor.execute(query)

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Cerrar cursor y conexión remota
cursor.close()
remote_db.close()

# Guardar los datos en un archivo local
with open('copia_de_datos.csv', 'w') as f:
    for registro in resultados:
        f.write(','.join(map(str, registro)) + '\n')
