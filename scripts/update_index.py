import os
import re
from bs4 import BeautifulSoup

# Directorio de endpoints
endpoints_dir = 'C:\\Users\\darin\\Documents\\LAB Reto\\APIUser\\endpoint'

# Archivo de documentación
doc_file = 'C:\\Users\\darin\\Documents\\LAB Reto\\APIUser\\data\\index.html'

# Leer los archivos de endpoint
def read_endpoints(directory):
    endpoints = []
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extraer información del endpoint
                endpoint = extract_endpoint_info(content)
                if endpoint:
                    endpoints.append(endpoint)
    return endpoints

# Extraer información del endpoint
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

# Actualizar el archivo de documentación
def update_documentation(endpoints, doc_file):
    # Leer el contenido existente del archivo de documentación
    with open(doc_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Usar BeautifulSoup para manipular el archivo HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Limpiar la lista de endpoints existente
    ul = soup.find('ul')
    ul.clear()

    # Añadir los nuevos endpoints
    for endpoint in endpoints:
        li = soup.new_tag('li')
        body_text = f' Body: {endpoint["body"]}' if endpoint['body'] else ''
        li.string = f'{endpoint["method"]} {endpoint["path"]} - {endpoint["description"]}{body_text}'
        ul.append(li)

    # Guardar el archivo de documentación actualizado
    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Leer los endpoints y actualizar la documentación
endpoints = read_endpoints(endpoints_dir)
update_documentation(endpoints, doc_file)

print("Documentación actualizada con éxito.")
