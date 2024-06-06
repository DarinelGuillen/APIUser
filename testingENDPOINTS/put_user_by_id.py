# Endpoint: PUT /users/{id}
# Description: Updates a specific user by ID.
# Body: {"name": "Updated Name"}

from flask import Blueprint, jsonify, current_app, request

put_user_by_id_route = Blueprint('update_user_by_id_route', __name__)

@put_user_by_id_route.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    user_data = request.get_json()
    if not user_data or not user_data.get('name'):
        return jsonify({"error": "Datos incompletos o no proporcionados"}), 400

    cursor = conn.cursor()
    update_query = f"UPDATE {current_app.config['TABLE']} SET name = %s WHERE id = %s"
    cursor.execute(update_query, (user_data['name'], id))
    conn.commit()
    updated_rows = cursor.rowcount

    cursor.close()

    if updated_rows:
        return jsonify({"success": "Usuario actualizado correctamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
