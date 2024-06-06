import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
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
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT, database=DB_NAME)
cursor = cnx.cursor()

# Recuperar datos de MySQL
query = "SELECT endpoint, description FROM documentation"
cursor.execute(query)
docs = cursor.fetchall()

# Crear un DataFrame
df = pd.DataFrame(docs, columns=['endpoint', 'description'])

# Generar un reporte simple
df.groupby('endpoint').count().plot(kind='bar', y='description', legend=False)
plt.title('API Endpoints Documentation')
plt.xlabel('Endpoint')
plt.ylabel('Number of Descriptions')
plt.show()

cursor.close()
cnx.close()
