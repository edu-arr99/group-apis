import requests

from app import app, verify_token

url = 'http://localhost:5000/auth/token'
api_key = '000000111111'
group = 'group01'

# Obtener un nuevo token de autenticación
response = requests.post(url, data={'api_key': api_key, 'group': group})
if response.status_code == 200:
    token = response.json().get('token')
    print('Nuevo token:', token)

    # Verificar el token de autenticación con el servidor
    secret_key = app.config['SECRET_KEY']
    if verify_token(token, secret_key):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://localhost:5000/group01', headers=headers)
        if response.status_code == 200:
            result = response.json().get('result')
            print('Respuesta del servidor:', result)
        else:
            print('Error:', response.json().get('error'))
    else:
        print('Token de autenticación inválido')
