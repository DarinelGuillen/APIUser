import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

# Cargar las variables de entorno
DB_NAME = os.getenv('DB')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
USER = 'root'  # Cambia esto si usas otro usuario

# Conectar a MySQL
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT)
cursor = cnx.cursor()

# Crear la base de datos si no existe
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

create_database(cursor)

# Seleccionar la base de datos
cursor.execute("USE {}".format(DB_NAME))

# Crear la tabla de documentación
TABLES = {}
TABLES['documentation'] = (
    "CREATE TABLE `documentation` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `endpoint` varchar(255) NOT NULL,"
    "  `description` varchar(255) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

def create_table(cursor, table_name):
    try:
        cursor.execute(TABLES[table_name])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)

create_table(cursor, 'documentation')

cursor.close()
cnx.close()
print("Table created successfully.")
