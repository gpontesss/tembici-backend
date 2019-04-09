import re, datetime
from server import api, session, app
from flask_restful import Resource, reqparse
from model import User, Phone, Log
from util.db import email_exists, user_last_login

# Number regex match
num = re.compile('^[0-9]+$')

# Parser for SignUp POST requests
sign_up_parser = reqparse.RequestParser()
sign_up_parser.add_argument(
    'nome', 
    help='Esse campo não pode estar vazio.', 
    required=True, 
    location='json'
)
sign_up_parser.add_argument(
    'email', 
    help='Esse campo não pode estar vazio.', 
    required=True, 
    location='json'
)
sign_up_parser.add_argument(
    'senha', 
    help='Esse campo não pode estar vazio.',
    required=True, 
    location='json'
)
sign_up_parser.add_argument(
    'telefones', 
    help='Esse campo não pode estar vazio', 
    type=list, 
    required=True, 
    location='json'
)

class SignUp(Resource):
    def post(self):
        data = sign_up_parser.parse_args()
        
        # Validate email
        if re.match("^[\w.]+@[\w]+\.[\w]+$", data.email) is None:
            return {
                'mensagem': '{} não é um email válido.'.format(data.email)
            }, 400

        # Email already registered
        if email_exists(data.email):
            return {
                'mensagem': '{} já foi registrado.'.format(data.email)
            }, 400

        # Validate phone numbers
        for phone in data['telefones']:
            if num.match(phone['numero']) is None or num.match(phone['ddd']) is None:
                return {
                    'mensagem': '{} {} não é um numero de telefone válido.'.format(phone['ddd'], phone['numero'])
                }, 400

        # Create user ORM
        user = User(
            data['nome'], 
            data['email'], 
            User.generate_hash(data['senha'])
        )
        user.phones = [Phone(phone['numero'], phone['ddd']) for phone in data['telefones']]

        token =  Log.generate_token({
            'sub': user.uuid,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        # Add to database
        session.add(user)
        session.add(Log(user, token))
        session.commit()

        # User registered successfully
        return {
            'id': user.uuid,
            'email': user.email,
            'data_criacao': user.creation_date.isoformat(),
            'data_atualizacao': user.update_date.isoformat(),
            'ultimo_login': user_last_login(user.email).date.isoformat(),
            'token': token.decode('UTF-8')
        }, 201