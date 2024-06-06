# Endpoint: GET /users/{id}
# Description: Retrieves a specific user by ID.

from flask import Blueprint, jsonify, current_app, request

get_user_by_id_route = Blueprint('get_user_by_id_route', __name__)

@get_user_by_id_route.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {current_app.config['TABLE']} WHERE id = %s", (id,))
    user = cursor.fetchone()

    cursor.close()

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
