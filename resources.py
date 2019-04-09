import re
from server import api, session
from flask_restful import Resource, reqparse
from model import User, Phone

# Number regex match
num = re.compile('^[0-9]+$')

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'nome', 
    help='This field cannot be blank.', 
    required=True, 
    location='json'
)
register_parser.add_argument(
    'email', 
    help='This field cannot be blank.', 
    required=True, 
    location='json'
)
register_parser.add_argument(
    'password', 
    help='This field cannot be blank.',
    required=True, 
    location='json'
)
register_parser.add_argument(
    'telefones', 
    help='This field cannot be blank', 
    type=list, 
    required=True, 
    location='json'
)

class UserRegister(Resource):
    def post(self):
        try:
            data = register_parser.parse_args()
        except:
            return {
                'mensagem': 'Request deve conter um objeto JSON.'
            }, 400
        
        # Validate email
        if re.match("^[\w.]+@[\w]+\.[\w]+$", data.email) is None:
            return {
                'mensagem': '{} não é um email válido.'.format(data.email)
            }, 400

        # Email already registered
        if session.query(User).filter(User.email == data.email).first():
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
        user = User(data['nome'], data['email'])
        user.phones = [Phone(phone['numero'], phone['ddd']) for phone in data['telefones']]

        # Add to database
        session.add(user)
        #session.commit()

        # User registered successfully
        return {
            'id': user.uuid,
            'email': user.email,
            'data_criacao': user.creation_date.isoformat(),
            'data_atualizacao': user.update_date.isoformat(),
            'ultimo_login': user.creation_date.isoformat(),
            'token': 'not yet'
        }, 201