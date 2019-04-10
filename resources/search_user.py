# -*- coding: utf-8 -*-
"""
    resources.search_user
    ----
    SearchUser endpoint for searching user by id found on path.
"""

from flask import request
from flask_restful import Resource

from util.auth import token_required
from util.db import user_by_uuid, user_last_login

from server import session

class SearchUser(Resource):
    """ Endpoint for searching users.

        HTTP Methods:
            GET @token_required
    """

    @token_required
    def get(self, user_id):
        """ Gets user by id found on path.
        """
        
        user = user_by_uuid(user_id)
        if user is None:
            return {
                'mensagem': 'Usuário não existe.'
            }, 400

        return user.to_obj(), 200