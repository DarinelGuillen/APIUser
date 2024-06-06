# Endpoint: DELETE /users/{id}
# Description: Deletes a specific user by ID.

from flask import Blueprint, jsonify, current_app

delete_user_by_id_route = Blueprint('delete_user_by_id_route', __name__)

@delete_user_by_id_route.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {current_app.config['TABLE']} WHERE id = %s", (id,))
    conn.commit()
    deleted_rows = cursor.rowcount

    cursor.close()

    if deleted_rows:
        return jsonify({"success": "Usuario eliminado correctamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
