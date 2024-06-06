# Configurafcion de Entorno
``` bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
# Error Fix
``` bash
deactivate
Remove-Item -Recurse -Force .\venv
```


## Scripts

- `analyze_docs.py`: Analiza y clasifica la documentación.
- `monitor_docs.py`: Monitorea y actualiza la documentación.
- `generate_reports.py`: Genera reportes de actualizaciones.
- `generate_code.py`: Genera código automáticamente usando plantillas.

## Ejecución

```bash
python scripts/analyze_docs.py
python scripts/monitor_docs.py
python scripts/generate_reports.py
python scripts/generate_code.py
