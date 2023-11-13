import pyodbc

# Establecer la cadena de conexión
server = 'localhost'
database = 'ClinicaVeterinaria'
username = 'sa'
password = '123456789'
port = '1433'

# La cadena de conexión sigue el formato:
# 'Driver={SQL Server};Server=server;Database=database;UID=username;PWD=password;Port=port;'
connection_string = f'Driver={{SQL Server}};Server={server},{port};Database={database};UID={username};PWD={password};'

# Conectarse a la base de datos
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM consulta where IdMascota=1")
    row = cursor.fetchall()

    print(row)

    # Cerrar la conexión
    conn.close()

except pyodbc.Error as e:
    print(f"Error de conexión a la base de datos: {e}")
