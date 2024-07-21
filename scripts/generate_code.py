import openai
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
DB_NAME = os.getenv('DB')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
USER = 'root'

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOSTNAME, port=PORT, database=DB_NAME)
cursor = cnx.cursor()

query = "SELECT endpoint, description, body FROM documentation"
cursor.execute(query)
docs = cursor.fetchall()

def generate_code_example(endpoint_info):
    prompt = f"""
    Genera un ejemplo de código para el siguiente endpoint de API:

    Método: {endpoint_info['method']}
    Ruta: {endpoint_info['path']}
    Descripción: {endpoint_info['description']}
    Cuerpo: {endpoint_info['body']}

    El ejemplo de código debe ser en Python, utilizando la biblioteca requests, e incluir:
    1. La definición de la función.
    2. La construcción de la solicitud HTTP.
    3. La ejecución de la solicitud y el manejo de la respuesta.
    4. Un ejemplo de uso de la función.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )
    return response.choices[0].message['content'].strip()

output_dir = 'C:\\Users\\darin\\Documents\\8B\\LAB Reto\\APIUser\\data'
os.makedirs(output_dir, exist_ok=True)
current_time = datetime.now().strftime("%d-%B-%Y_%H-horas")

file_name = f"Code_Examples_{current_time}.py"
file_path = os.path.join(output_dir, file_name)
with open(file_path, 'w', encoding='utf-8') as f:
    f.write("import requests\n\n")

    for doc in docs:
        endpoint_info = {
            'method': doc[0].split(' ')[0],
            'path': doc[0].split(' ')[1],
            'description': doc[1],
            'body': doc[2]
        }
        code_example = generate_code_example(endpoint_info)
        f.write(code_example + '\n\n')

print(f"Código generado y guardado en {file_path}")

cursor.close()
cnx.close()
