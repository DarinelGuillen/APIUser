import requests

Aquí te dejo un ejemplo de código en Python utilizando la biblioteca requests para el endpoint de API dado:

```python
import requests

def create_new_user():
    url = "http://example.com/users"
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("User created successfully.")
    else:
        print("Failed to create user. Status code:", response.status_code)


# Ejemplo de uso de la función
create_new_user()
```

En este código, la función `create_new_user` define la construcción de la solicitud HTTP utilizando el método POST para enviar los datos del nuevo usuario al endpoint `/users`. Luego, la solicitud se ejecuta y se maneja la respuesta. Finalmente, se incluye un ejemplo de uso de la función para crear un nuevo usuario con nombre "John Doe" y correo electrónico "john.doe@example.com".

Aquí tienes un ejemplo de código en Python utilizando la biblioteca `requests` para realizar una solicitud GET al endpoint `/users/{id}`:

```python
import requests

def get_user_by_id(user_id):
    url = f"http://api.example.com/users/{user_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print("User data:")
        print(user_data)
    else:
        print(f"Failed to retrieve user. Status code: {response.status_code}")

# Ejemplo de uso de la función
user_id = 123
get_user_by_id(user_id)
```

En este ejemplo, la función `get_user_by_id` acepta un parámetro `user_id`, construye la URL con el ID proporcionado, realiza la solicitud GET, y luego verifica si la solicitud fue exitosa o no. Si la solicitud es exitosa (código de estado 200), se imprime la información del usuario; de lo contrario, se imprime un mensaje de error.

Puedes reemplazar `http://api.example.com` con la base correcta de la API que estés utilizando. Y asegúrate de manejar las posibles excepciones según tus necesidades.

Aquí tienes un ejemplo de código en Python utilizando la biblioteca `requests` para hacer una solicitud GET al endpoint `/users` de una API que recupera una lista de usuarios:

```python
import requests

def get_users_list():
    url = 'https://api.example.com/users'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        users_list = response.json()
        return users_list
    else:
        print(f'Error al obtener la lista de usuarios. Código de estado: {response.status_code}')
        return None

# Ejemplo de uso de la función
users = get_users_list()

if users:
    print("Lista de usuarios:")
    for user in users:
        print(user)
```

En este ejemplo, la función `get_users_list` define la lógica para hacer la solicitud GET al endpoint `/users`, manejar la respuesta y devolver la lista de usuarios si la operación fue exitosa. Luego, se muestra un ejemplo de uso de esta función, donde se obtiene la lista de usuarios y se imprime en caso de que la operación sea exitosa.

Aquí tienes un ejemplo de código Python que maneja el endpoint de API DELETE para eliminar un usuario específico por su ID utilizando la biblioteca requests:

```python
import requests

def delete_user_by_id(user_id):
    url = f"https://api.example.com/users/{user_id}"
    
    response = requests.delete(url)
    
    if response.status_code == 200:
        print(f"User with ID {user_id} has been successfully deleted")
    else:
        print(f"Failed to delete user with ID {user_id}. Status code: {response.status_code}")

# Ejemplo de uso de la función
user_id_to_delete = 123
delete_user_by_id(user_id_to_delete)
```

En este código, la función `delete_user_by_id` toma como argumento el ID del usuario que se desea eliminar. Construye la URL con el ID proporcionado, realiza la solicitud HTTP DELETE a la API y luego maneja la respuesta de acuerdo al código de estado devuelto. Por último, se proporciona un ejemplo de uso de la función donde se llama a `delete_user_by_id` con un ID de usuario específico.

