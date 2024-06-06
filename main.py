import os
# *Funcion la cual guarda en infomacion de la documentacion en DB y crea codigo de ejemplos para su uso

# Ejecutar store_docs.py para actualizar la base de datos
os.system('python scripts/store_docs.py')

# Ejecutar generate_code.py para generar el código de ejemplo actualizado
os.system('python scripts/generate_code.py')
