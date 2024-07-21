# Endpoint: POST /users
# Description: Creates a new user.
# Body: {"name": "John Doe", "email": "john.doe@example.com"}


from flask import Blueprint, request, jsonify, current_app

create_user_route = Blueprint('create_user_route', __name__)

@create_user_route.route('/users', methods=['POST'])
def create_user():
    conn = current_app.config['GET_DB_CONNECTION']()
    if conn is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    new_user = request.json
    if not new_user or not new_user.get('name'):
        return jsonify({"error": "Nombre de usuario no proporcionado"}), 400

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {current_app.config['TABLE']} (name) VALUES (%s)", (new_user['name'],))
    conn.commit()

    new_user_id = cursor.lastrowid
    cursor.close()

    return jsonify({"id": new_user_id, "name": new_user['name']}), 201
