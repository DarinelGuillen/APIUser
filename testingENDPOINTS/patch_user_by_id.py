# Endpoint: PATCH /users/{id}
# Description: Updates the name of a specific user by ID.
# Body: {"name": "Updated Name"}

from flask import Blueprint, jsonify, current_app, request

patch_user_by_id_route = Blueprint('patch_user_by_id_route', __name__)

@patch_user_by_id_route.route('/users/<int:id>', methods=['PATCH'])
def patch_user_by_id(id):
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    cursor = conn.cursor()
    name = request.json.get('name')
    if not name:
        return jsonify({"error": "Nombre no proporcionado"}), 400

    cursor.execute(f"UPDATE {current_app.config['TABLE']} SET name = %s WHERE id = %s", (name, id))
    conn.commit()
    updated_rows = cursor.rowcount

    cursor.close()

    if updated_rows:
        return jsonify({"success": "Nombre actualizado correctamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
