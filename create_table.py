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
        print("Database created or already exists.")
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

create_database(cursor)

# Seleccionar la base de datos
cursor.execute("USE {}".format(DB_NAME))
print(f"Using database {DB_NAME}.")

# Eliminar la tabla si ya existe
def drop_table_if_exists(cursor, table_name):
    try:
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
        print(f"Table {table_name} dropped if it existed.")
    except mysql.connector.Error as err:
        print(f"Error dropping table {table_name}: {err}")

drop_table_if_exists(cursor, 'documentation')
drop_table_if_exists(cursor, 'user')

# Crear las tablas
TABLES = {}
TABLES['documentation'] = (
    "CREATE TABLE `documentation` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `endpoint` varchar(255) NOT NULL,"
    "  `description` varchar(255) NOT NULL,"
    "  `body` text,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['user'] = (
    "CREATE TABLE `user` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `email` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  UNIQUE KEY `email` (`email`)"
    ") ENGINE=InnoDB")

def create_table(cursor, table_name):
    try:
        print(f"Creating table {table_name}: ", end='')
        cursor.execute(TABLES[table_name])
        print("OK")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)

create_table(cursor, 'documentation')
create_table(cursor, 'user')

cursor.close()
cnx.close()
print("Tables created successfully.")
