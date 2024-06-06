import os

# Ejecutar update_index.py para actualizar el archivo de documentación
os.system('python scripts/update_index.py')

# Ejecutar store_docs.py para actualizar la base de datos
os.system('python scripts/store_docs.py')

# Ejecutar generate_code.py para generar el código de ejemplo actualizado
os.system('python scripts/generate_code.py')

# Ejecutar monitor_docs.py para mostrar los endpoints actuales
os.system('python scripts/generate_reports.py')
