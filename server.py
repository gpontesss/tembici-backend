from flask import Flask, jsonify
from flask_restful import Api

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tembici'
api = Api(app)

# Error handling for 404 Not Found requests
def resource_not_found(error):
    print(error)
    return jsonify({'mensagem': 'Endpoint não existe.'}), 404

app.register_error_handler(404, resource_not_found)

# Database setup
engine = create_engine('sqlite:///tembici-test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)
session = Session()

# importing resources and views
import views, resources

# Registering routes
api.add_resource(resources.SignUp, '/sign_up')
api.add_resource(resources.SignIn, '/sign_in')
