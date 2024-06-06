
import requests

def users_users():
    url = f'http://127.0.0.1:5000/users'
    
    response = requests.get(url)
    return response.json()

# Ejemplo de uso
print(users_users())


import requests

def users_users(data=None):
    url = f'http://127.0.0.1:5000/users'
    data = {"name": "John Doe"}
    response = requests.post(url, json=data)
    return response.json()

# Ejemplo de uso
print(users_users(data={"name": "John Doe"}))


import requests

def users_users(id):
    url = f'http://127.0.0.1:5000/users/{id}'
    
    response = requests.get(url)
    return response.json()

# Ejemplo de uso
print(users_users(id=1))

