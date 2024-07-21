import requests

# Aquí tienes un ejemplo de código en Python utilizando la biblioteca requests para el endpoint de API especificado:

```python
import requests

def create_new_user():
    url = "http://api.example.com/users"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("User created successfully.")
    else:
        print("Failed to create user. Status code:", response.status_code)

# Ejemplo de uso de la función
create_new_user()
```

En este código, la función `create_new_user` hace una solicitud HTTP POST al endpoint `/users` con los datos de usuario proporcionados en el cuerpo. Luego, se imprime un mensaje indicando si el usuario se creó exitosamente o si hubo un error en la solicitud. La ejecución de la función se realiza mediante el ejemplo de uso al final del código. Puedes adaptar este código a tu entorno y requisitos específicos.

Aquí tienes un ejemplo de código en Python utilizando la biblioteca `requests` para realizar una solicitud GET al endpoint `/users` de una API que recupera una lista de usuarios:

```python
import requests

def get_users_list():
    url = "https://api.example.com/users"  # Reemplazar con la URL correcta de la API

    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f"Failed to retrieve users. Status code: {response.status_code}")
        return None

# Ejemplo de uso de la función
users_list = get_users_list()

if users_list:
    print("Lista de usuarios obtenida:")
    for user in users_list:
        print(user)
```

En este ejemplo, la función `get_users_list` realiza una solicitud GET al endpoint `/users` de la API especificada. Si la solicitud es exitosa (código de estado 200), se devuelve la lista de usuarios en formato JSON. En caso de que la solicitud falle, se mostrará un mensaje de error.

En el ejemplo de uso, se llama a la función `get_users_list` y se imprime la lista de usuarios obtenida si la solicitud fue exitosa. Recuerda reemplazar la URL por la correcta de la API que estés utilizando.

Claro, aquí te dejo un ejemplo de código en Python utilizando la biblioteca `requests` para consumir el endpoint /users/{id} de una API:

```python
import requests

def get_user_by_id(user_id):
    url = f"https://api.example.com/users/{user_id}"

    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        return None

# Ejemplo de uso de la función
user_id = 123
user_info = get_user_by_id(user_id)

if user_info:
    print("User found:")
    print(user_info)
else:
    print(f"User with ID {user_id} not found.")
```

En este ejemplo, la función `get_user_by_id` toma como parámetro el `user_id`, construye la URL del endpoint con ese ID, realiza la solicitud GET, verifica el estado de la respuesta y devuelve los datos del usuario si el código de estado es 200 (éxito) o `None` en caso contrario.

Finalmente, se muestra un ejemplo de uso de la función donde se busca un usuario por su ID y se imprime la información o un mensaje de usuario no encontrado.

