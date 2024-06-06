# import requests

# def users_users():
#     url = 'http://127.0.0.1:5000/users'
#     response = requests.get(url)
#     print(response.json())
#     return response.json()


# users_users()

import requests

def users_users():
    url = 'http://127.0.0.1:5000/users'
    data = {"name": "John Doe"}
    response = requests.post(url, json=data)
    return response.json()

# Ejemplo de uso
print(users_users())