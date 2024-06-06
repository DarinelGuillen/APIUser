from jinja2 import Template
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

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
query = "SELECT endpoint, description, body FROM documentation"
cursor.execute(query)
docs = cursor.fetchall()

# Plantilla de Jinja2
template_str = """
import requests

def {{ method_name }}({{ params }}{{ body_param }}):
    url = f'http://127.0.0.1:5000{{ endpoint_path }}'
    {{ body_data }}
    response = requests.{{ http_method }}(url{{ body_pass }})
    return response.json()

# Ejemplo de uso
print({{ method_name }}({{ example_params }}{{ example_body }}))
"""

template = Template(template_str)

# Directorio para guardar el código generado
output_dir = 'C:\\Users\\darin\\Documents\\LAB Reto\\APIUser\\data'

# Crear el directorio si no existe
os.makedirs(output_dir, exist_ok=True)

# Obtener la fecha y hora actual en un formato más legible
current_time = datetime.now().strftime("%d-%B-%Y_%H-horas")

# Generar y guardar código para cada endpoint en un archivo único
file_name = f"Code_Examples_{current_time}.py"
file_path = os.path.join(output_dir, file_name)
with open(file_path, 'w', encoding='utf-8') as f:
    for doc in docs:
        endpoint, description, body = doc
        endpoint_path = endpoint.split(' ')[1].replace('{id}', '{id}')
        method_name = endpoint_path.split('/')[1] + '_users'
        params = 'id' if '{id}' in endpoint else ''
        body_param = 'data=None' if body else ''
        http_method = endpoint.split(' ')[0].lower()
        body_data = f'data = {body}' if body else ''
        body_pass = ', json=data' if body else ''
        example_body = 'data={"name": "John Doe"}' if body else ''
        example_params = 'id=1' if params else ''

        code = template.render(
            method_name=method_name,
            params=params,
            endpoint_path=endpoint_path,
            http_method=http_method,
            body_param=(', ' + body_param) if params and body_param else body_param,
            body_data=body_data,
            body_pass=body_pass,
            example_body=(', ' + example_body) if example_params and example_body else example_body,
            example_params=example_params
        )
        f.write(code + '\n\n')

print(f"Código generado y guardado en {file_path}")

cursor.close()
cnx.close()
