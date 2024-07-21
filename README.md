# Proyecto de Automatización de Documentación y Generación de Código

Este proyecto automatiza el proceso de análisis, almacenamiento y generación de código de ejemplo para la documentación de APIs. Utiliza MySQL para almacenar la documentación y Jinja2 para generar los ejemplos de código.

## Tabla de Contenidos
- [Configuración del Entorno](#configuración-del-entorno)
- [Solución de Errores Comunes](#solución-de-errores-comunes)
- [Scripts](#scripts)
  - [analyze_docs.py](#analyze_docspy)
  - [monitor_docs.py](#monitor_docspy)
  - [generate_reports.py](#generate_reportspy)
  - [store_docs.py](#store_docspy)
  - [generate_code.py](#generate_codepy)
- [Ejecución](#ejecución)
- [Automatización](#automatización)
  - [Automatización en Linux/Mac usando Cron Jobs](#automatización-en-linuxmac-usando-cron-jobs)
  - [Automatización en Windows usando Tareas Programadas](#automatización-en-windows-usando-tareas-programadas)
- [Contacto](#contacto)

## Configuración del Entorno

Para configurar el entorno virtual y las dependencias necesarias, sigue estos pasos:

```bash
python -m venv venv
.\venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac
pip install -r requirements.txt
python app.py
```

## Solución de Errores Comunes

Si necesitas desactivar y eliminar el entorno virtual, usa los siguientes comandos:
```bash
deactivate
Remove-Item -Recurse -Force .\venv
```
## Agregar Nuevos Endpoints
  - Crea un archivo en el directorio endpoint con el formato adecuado.
  - Asegúrate de que los comentarios sigan el formato:
```bash
  # Endpoint: {METHOD} /path
  # Description: Description of the endpoint.
  # Body: {"key": "value"}  # Si aplica
```


## Scripts

### analyze_docs.py

- **Función**: Analiza y clasifica la documentación de la API para identificar y organizar los endpoints y sus descripciones.
    
- **Uso**: Ejecuta este script para procesar nuevos documentos de API y clasificarlos adecuadamente.
    
- **Ejemplo de Ejecución**:
    
    
```
python scripts/analyze_docs.py

```

### monitor_docs.py

- **Función**: Monitorea la documentación de la API para detectar cambios o actualizaciones y mantiene la base de datos sincronizada.
    
- **Uso**: Ejecuta este script regularmente para asegurarte de que la base de datos siempre refleje la documentación actualizada.
    
- **Ejemplo de Ejecución**:
```
python scripts/monitor_docs.py

```
### generate_reports.py

- **Función**: Genera reportes sobre las actualizaciones y cambios en la documentación de la API, proporcionando una visión general de las modificaciones recientes.
    
- **Uso**: Ejecuta este script para obtener un informe detallado de las actualizaciones de la documentación.
    
- **Ejemplo de Ejecución**:
```
python scripts/generate_reports.py

```
### store_docs.py

- **Función**: Almacena la documentación de la API en una base de datos MySQL, incluyendo descripciones y cuerpos de solicitudes.
    
- **Uso**: Ejecuta este script para cargar y actualizar la documentación en la base de datos.
    
- **Ejemplo de Ejecución**:

```
python scripts/store_docs.py

```
### generate_code.py

- **Función**: Genera automáticamente ejemplos de código para interactuar con los endpoints de la API, usando plantillas Jinja2.
    
- **Uso**: Ejecuta este script para generar ejemplos de código actualizados basados en la documentación almacenada en la base de datos.
    
- **Ejemplo de Ejecución**:

```
python scripts/generate_code.py

```
## Ejecución

Para ejecutar todos los scripts en secuencia, puedes utilizar el siguiente comando:

```
python main.py
```
## Automatización

Para automatizar el proceso, puedes configurar un Cron Job (en Linux/Mac) o una Tarea Programada (en Windows) para ejecutar `main.py` a intervalos regulares.

### Automatización en Linux/Mac usando Cron Jobs

```
crontab -e
# Añadir la siguiente línea para ejecutar el script cada día a medianoche
0 0 * * * /path/to/venv/bin/python /path/to/your/project/main.py

```


## Integración con ChatGPT

Para mejorar la automatización de la documentación técnica, hemos integrado ChatGPT para generar descripciones detalladas de los endpoints de las APIs.

## Scripts

### generate_documentation.py

- **Función**: Utiliza ChatGPT para generar documentación técnica detallada de los endpoints de la API basándose en descripciones básicas.
    
- **Uso**: Ejecuta este script para generar documentación automáticamente.
    
- **Ejemplo de Ejecución**:


