# -*- coding: utf-8 -*-
"""
    server.py
    ---------
    Flask API for SignIn/SignUp and SearchUser
    restricted endpoint.
    Tembici backend's test completion.
"""

from flask import Flask, jsonify
from flask_restful import Api

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from util import resource_not_found

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tembici'
api = Api(app)

app.register_error_handler(404, resource_not_found)

# Database setup
engine = create_engine('sqlite:///tembici-test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)
session = Session()

# importing resources
import resources

# Registering routes
api.add_resource(resources.SignUp, '/sign_up')
api.add_resource(resources.SignIn, '/sign_in')
api.add_resource(resources.SearchUser, '/search_user/<user_id>')
