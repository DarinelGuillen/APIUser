import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
USER = 'root'

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT, database=DB_NAME)
cursor = cnx.cursor()

query = "SELECT endpoint, description FROM documentation"
cursor.execute(query)
docs = cursor.fetchall()

if not docs:
    print("No hay datos disponibles para generar el reporte.")
else:
    df = pd.DataFrame(docs, columns=['endpoint', 'description'])

    df.groupby('endpoint').count().plot(kind='bar', y='description', legend=False)
    plt.title('API Endpoints Documentation')
    plt.xlabel('Endpoint')
    plt.ylabel('Number of Descriptions')
    plt.show()

cursor.close()
cnx.close()
