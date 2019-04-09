from flask import request
from flask_restful import Resource
from util.auth import token_required
from util.db import user_by_uuid, user_last_login
from server import session

class SearchUser(Resource):
    @token_required
    def get(self, user_id):

        user = user_by_uuid(user_id)
        if user is None:
            return {
                'mensagem': 'Usuário não existe.'
            }, 400

        return user.to_obj(), 200