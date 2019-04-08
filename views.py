from server import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({'hello': 'world'})