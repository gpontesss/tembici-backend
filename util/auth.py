import jwt
from flask import request
from server import app, session
from model import Log
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')[7:].encode('UTF-8')

            if not session.query(Log).filter(Log.token == token).first():
                raise ValueError("ValueError: Token not registered.")

            data = Log.verify_token(token, app.config['SECRET_KEY'])

        except jwt.exceptions.ExpiredSignatureError:
            return {
                'mensagem': 'Sessão inválida.'
            }, 403

        except Exception as e:
            print(e.__class__)
            return {
                'mensagem': 'Não autorizado.'
            }, 403

        return f(*args, **kwargs)
        
    return decorated