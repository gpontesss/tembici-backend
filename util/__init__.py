# -*- coding: utf-8 -*-
"""
    util
    ----
    Utilities package for miscellaneous functions.
"""

from flask import jsonify

def resource_not_found(error):
    print(error)
    return jsonify({'mensagem': 'Endpoint não existe.'}), 404