import datetime
from flask_restful import Resource, reqparse
from server import api, session, app
from model import User, Log
from util.db import email_exists, user_hash, get_user_by_email, user_last_login

# Parser for SignIn POST requests
sign_in_parser = reqparse.RequestParser()
sign_in_parser.add_argument(
    'email',
    help='Esse campo não pode estar vazio.', 
    required=True, 
    location='json'
)
sign_in_parser.add_argument(
    'senha',
    help='Esse campo não pode estar vazio.', 
    required=True, 
    location='json'
)

class SignIn(Resource):
    def post(self):
        data = sign_in_parser.parse_args()

        # Email exists/Verify password hash
        if not email_exists(data['email']) or \
        not User.verify_hash(data['senha'], user_hash(data['email'])):
            return {
                'mensagem': 'Usuário e/ou senha inválidos.'
            }, 401
        
        user = get_user_by_email(data['email'])
        token =  Log.generate_token({
            'sub': user.uuid,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        }, app.config['SECRET_KEY'])

        log = Log(user, token)

        # Registering login
        session.add(log)
        session.commit()

        # User logged in successfully
        return {
            'id': user.uuid,
            'email': user.email,
            'data_criacao': user.creation_date.isoformat(),
            'data_atualizacao': user.update_date.isoformat(),
            'ultimo_login': user_last_login(user.email).isoformat(),
            'token': token.decode('UTF-8')
        }, 201