import mysql.connector
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

DB_NAME = os.getenv('DB')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
USER = 'root'

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT, database=DB_NAME)
cursor = cnx.cursor()

file_path = 'C:\\Users\\darin\\Documents\\8B\\LAB Reto\\APIUser\\data\\index.html'

if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no existe.")

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

current_docs = []
for doc in soup.find_all('li'):
    parts = doc.text.split(' - ')
    if len(parts) == 2:
        endpoint = parts[0]
        description_body = parts[1]
        description, body = (description_body.split(' Body: ') + [None])[:2]
        current_docs.append((endpoint, description, body))

cursor.execute("SELECT endpoint FROM documentation")
stored_docs = cursor.fetchall()

stored_endpoints = set(doc[0] for doc in stored_docs)

add_doc = ("INSERT INTO documentation (endpoint, description, body) VALUES (%s, %s, %s)")
check_doc = ("SELECT * FROM documentation WHERE endpoint = %s")

for doc in current_docs:
    cursor.execute(check_doc, (doc[0],))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE documentation SET description = %s, body = %s WHERE endpoint = %s", (doc[1], doc[2], doc[0]))
    else:
        cursor.execute(add_doc, doc)
    stored_endpoints.discard(doc[0])

delete_doc = ("DELETE FROM documentation WHERE endpoint = %s")
for endpoint in stored_endpoints:
    cursor.execute(delete_doc, (endpoint,))
    print(f"El endpoint {endpoint} ha sido eliminado de la base de datos.")

cnx.commit()

cursor.close()
cnx.close()
print("Documentación sincronizada con la base de datos.")
