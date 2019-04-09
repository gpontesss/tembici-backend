from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Flask setup
app = Flask(__name__)
api = Api(app)

# Database setup
engine = create_engine('sqlite:///tembici-test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)
session = Session()

import views, resources

api.add_resource(resources.UserRegister, '/register')
