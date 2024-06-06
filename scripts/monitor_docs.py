from bs4 import BeautifulSoup

# Ruta local del archivo de documentación
file_path = 'C:\\Users\\darin\\Documents\\LAB Reto\\APIUser\\data\\index.html'
# "C:\Users\darin\Documents\LAB Reto\APIUser\data\index.html"

# Leer el contenido del archivo
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Procesar el contenido con BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Encuentra y procesa la información relevante
for doc in soup.find_all('li'):
    print(doc.text)
