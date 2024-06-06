import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que tienes los datos en una lista de diccionarios
data = [{"endpoint": "GET /users", "status": "updated", "date": "2023-01-01"}, ...]

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Generar un reporte simple
df.groupby('status').count().plot(kind='bar')
plt.show()
