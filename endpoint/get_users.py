# Endpoint: GET /users
# Description: Retrieves a list of users.

from flask import Blueprint, jsonify, current_app

get_users_route = Blueprint('get_users_route', __name__)

@get_users_route.route('/users', methods=['GET'])
def get_users():
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {current_app.config['TABLE']}")
    users = cursor.fetchall()

    cursor.close()

    return jsonify(users)
