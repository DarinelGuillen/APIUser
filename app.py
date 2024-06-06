import os
from flask import Flask, g
from dotenv import load_dotenv
import mysql.connector
from endpoint.get_users import get_users_route
from endpoint.create_user import create_user_route
from endpoint.get_user_by_id import get_user_by_id_route
# from endpoint.put_user_by_id import put_user_by_id_route
# from endpoint.delete_user_by_id import delete_user_by_id_route
# from endpoint.patch_user_by_id import patch_user_by_id_route

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['DB_CONFIG'] = {
    'user': 'root',
    'password': os.getenv('PASSWORD', ''),
    'host': os.getenv('HOSTNAME', '127.0.0.1'),
    'database': os.getenv('DB', 'test'),
    'port': int(os.getenv('PORT', 3306)),
}
app.config['TABLE'] = os.getenv('TABLE', 'user')

def get_db_connection():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(**app.config['DB_CONFIG'])
            print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            g.db = None
    return g.db

@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app.config['GET_DB_CONNECTION'] = get_db_connection

# Registrar las rutas
app.register_blueprint(get_users_route)
app.register_blueprint(create_user_route)
app.register_blueprint(get_user_by_id_route)
# app.register_blueprint(put_user_by_id_route)
# app.register_blueprint(delete_user_by_id_route)
# app.register_blueprint(patch_user_by_id_route)

if __name__ == '__main__':
    app.run(debug=True)
