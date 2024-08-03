from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

def inicializarVariables(user, pwd):
    userLocal = 'aramirez'
    passLocal = 'unida123'
    codRes = 'NO_ERR'
    menRes = 'ok'

    try:
        print('Verificar login')

        if pwd == passLocal and user == userLocal:
            print('Usuario y contraseña ok')
            accion = 'success'
        else:
            print('Usuario o contraseña incorrecta')
            accion = 'Usuario o contraseña incorrecta'
            codRes = 'ERR_INVALID_USER_PASSWORD'
            menRes = 'Credenciales incorrectas'
    except Exception as e:
        print('Error', str(e))
        codRes = 'ERR_INTERNAL'
        menRes = f'Msg: {str(e)}'
        accion = 'internal_error'

    return codRes, menRes, accion


@login.route('/login', methods=['POST'])
def login2():
    user = request.json.get('user')
    pwd  = request.json.get('password')

    codRes, menRes, accion = inicializarVariables(user, pwd)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion
    }

    return jsonify(salida)