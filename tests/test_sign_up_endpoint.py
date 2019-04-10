# -*- coding: utf-8 -*-
"""
    tests.test_api_endpoints
    -----
    Package to contain application unit tests.
"""

import unittest
from .db_setup import db_setup
from server import app

class TestSignUpEndpoint(unittest.TestCase):

    tester = app.test_client()

    def setUp(self):
        db_setup()

    def test_email_not_valid_sign_up(self):
        response = self.tester.post(
            '/sign_up',
            json={
                "nome": "Guilherme Pontes",
                "email": "not valid",
                "senha": "guilherme",
                "telefones": []
            }
        )

        self.assertEqual(
            response.get_json(),
            {'mensagem': 'not valid não é um email válido.'}
        )

    def test_email_already_registered(self):
        response = ''
        for _ in range(2):
            response = self.tester.post(
                '/sign_up',
                json={
                    "nome": "Guilherme Pontes",
                    "email": "guilherme.pontes@gmail.com",
                    "senha": "guilherme",
                    "telefones": []
                }
            )

        self.assertEqual(
            response.get_json(),
            {'mensagem': 'guilherme.pontes@gmail.com já foi registrado.'}
        )

if __name__ == '__main__':
    print('Starting tests.')
    unittest.main()