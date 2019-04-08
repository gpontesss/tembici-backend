from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'hello': 'world'})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
