import openai
import os
import re
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_documentation(endpoint_info):
    prompt = f"""
    Genera la documentación técnica para el siguiente endpoint de API:

    Método: {endpoint_info['method']}
    Ruta: {endpoint_info['path']}
    Descripción: {endpoint_info['description']}
    Parámetros: {endpoint_info.get('parameters', 'N/A')}
    Cuerpo: {endpoint_info.get('body', 'N/A')}

    La documentación debe incluir:
    1. Descripción del endpoint.
    2. Ejemplos de solicitudes y respuestas.
    3. Descripción de los parámetros y sus tipos.
    4. Posibles códigos de error y sus significados.
    5. reportes de hallazgos: Informar sobre oportunidades, riesgos y limitaciones.
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

def read_endpoints(directory):
    endpoints = []
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                endpoint = extract_endpoint_info(content)
                if endpoint:
                    endpoints.append(endpoint)
    return endpoints

def extract_endpoint_info(content):
    endpoint_match = re.search(r'#\s*Endpoint:\s*(GET|POST|PATCH|DELETE)\s*(/\S+)', content)
    description_match = re.search(r'#\s*Description:\s*(.+)', content)
    body_match = re.search(r'#\s*Body:\s*(.+)', content)

    if endpoint_match and description_match:
        method = endpoint_match.group(1)
        path = endpoint_match.group(2)
        description = description_match.group(1)
        body = body_match.group(1) if body_match else None
        return {'method': method, 'path': path, 'description': description, 'body': body}
    return None

def update_documentation(endpoints, doc_file, txt_file):
    with open(doc_file, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    ul = soup.find('ul')
    ul.clear()

    documentation_text = ""

    for endpoint in endpoints:
        doc_detail = generate_documentation(endpoint)
        li = soup.new_tag('li')
        li.string = f"{endpoint['method']} {endpoint['path']} - {endpoint['description']} Body: {endpoint['body']}"
        ul.append(li)
        documentation_text += doc_detail + "\n\n"

    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(documentation_text)

def main():
    endpoints_dir = 'C:\\Users\\darin\\Documents\\8B\\LAB Reto\\APIUser\\endpoint'
    doc_file = 'C:\\Users\\darin\\Documents\\8B\\LAB Reto\\APIUser\\data\\index.html'
    txt_file = 'C:\\Users\\darin\\Documents\\8B\\LAB Reto\\APIUser\\data\\documentation.txt'

    endpoints = read_endpoints(endpoints_dir)
    update_documentation(endpoints, doc_file, txt_file)
    print("Documentación generada y actualizada con éxito.")

if __name__ == "__main__":
    main()
