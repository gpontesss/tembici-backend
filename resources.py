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
        data = register_parser.parse_args()
        
        # Validate email
        if re.match("^[\w.]+@[\w]+\.[\w]+$", data.email) is None:
            return {'email': 'Not a valid email.'}, 400

        # Validate phone numbers
        for phone in data['telefones']:
            if num.match(phone['numero']) is None or num.match(phone['ddd']) is None:
                return {'telefone': '{} {} is not a valid phone number'.format(phone['ddd'], phone['numero'])}, 400

        # Create user ORM
        user = User(data['nome'], data['email'])
        for phone in data['telefones']:
            user.phones.append(Phone(phone['numero'], phone['ddd']))

        # Add to database
        session.add(user)
        session.commit()

        return data, 201