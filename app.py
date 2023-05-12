import jwt
import os
from functools import wraps
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
secret_key = os.urandom(64)
# Clave secreta para la firma de JWT
app.config['SECRET_KEY'] = secret_key
valid_api_key = '000000111111'

# Función para verificar un token de autenticación


def verify_token(token, secret_key):
    try:
        data = jwt.decode(token, secret_key, algorithms=["HS256"])
        # Verifica si el token contiene la clave correcta y es para el grupo 01
        if data['api_key'] == valid_api_key and data['group'] == 'group01':
            return True, data
    except:
        pass
    return False, None



# Decorador para requerir autenticación JWT para el grupo 01
def require_token_for_group01(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Falta token de autenticación'}), 401
        token = auth_header.split(" ")[1]
        is_valid, token_data = verify_token(token, app.config['SECRET_KEY'])

    return decorated

@app.route('/group01')
@require_token_for_group01
def group01():
    return jsonify({'result': 'este es el grupo 01'})


# Endpoint para obtener un token de autenticación
@app.route('/auth/token', methods=['POST'])
def auth_token():
    api_key = request.form.get('api_key')
    group = request.form.get('group')
    if api_key == valid_api_key and group in ['group01']:
        # Crea un token JWT con la clave de API y el grupo
        token = jwt.encode({'api_key': api_key, 'group': group}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'API key o grupo inválido'}), 401

# Endpoint no accesible sin autenticación
@app.route('/group02')
def group02():
    return jsonify({'result': 'este es el grupo 02'})

# Endpoint no accesible sin autenticación
@app.route('/group03')
def group03():
    return jsonify({'result': 'este es el grupo 03'})

# Endpoint no accesible sin autenticación
@app.route('/group04')
def group04():
    return jsonify({'result': 'este es el grupo 04'})

if __name__ == '__main__':
    app.run()
