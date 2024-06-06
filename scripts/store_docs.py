import mysql.connector
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# Cargar las variables de entorno
DB_NAME = os.getenv('DB')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
USER = 'root'  # Cambia esto si usas otro usuario

# Conectar a MySQL
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT, database=DB_NAME)
cursor = cnx.cursor()

# Ruta local del archivo de documentación
file_path = 'C:\\Users\\darin\\Documents\\LAB Reto\\APIUser\\data\\index.html'

# Leer el contenido del archivo
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Procesar el contenido con BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Extraer los endpoints actuales del archivo HTML
current_docs = []
for doc in soup.find_all('li'):
    endpoint, description_body = doc.text.split(' - ')
    description, body = (description_body.split(' Body: ') + [None])[:2]
    current_docs.append((endpoint, description, body))

# Obtener los endpoints almacenados en la base de datos
cursor.execute("SELECT endpoint FROM documentation")
stored_docs = cursor.fetchall()

# Convertir la lista de endpoints almacenados a un conjunto para una búsqueda rápida
stored_endpoints = set(doc[0] for doc in stored_docs)

# Insertar o actualizar los endpoints actuales
add_doc = ("INSERT INTO documentation (endpoint, description, body) VALUES (%s, %s, %s)")
check_doc = ("SELECT * FROM documentation WHERE endpoint = %s")

for doc in current_docs:
    cursor.execute(check_doc, (doc[0],))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE documentation SET description = %s, body = %s WHERE endpoint = %s", (doc[1], doc[2], doc[0]))
    else:
        cursor.execute(add_doc, doc)
    stored_endpoints.discard(doc[0])  # Remove processed endpoints from the set

# Eliminar los endpoints que ya no existen en el archivo HTML
delete_doc = ("DELETE FROM documentation WHERE endpoint = %s")
for endpoint in stored_endpoints:
    cursor.execute(delete_doc, (endpoint,))
    print(f"El endpoint {endpoint} ha sido eliminado de la base de datos.")

cnx.commit()

cursor.close()
cnx.close()
print("Documentación sincronizada con la base de datos.")
