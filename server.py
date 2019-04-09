from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///tembici-test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

import views
