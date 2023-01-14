from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'health': True})
