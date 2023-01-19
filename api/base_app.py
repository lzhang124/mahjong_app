import logging

from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS

from .src.db import migrate_db


logging.basicConfig(level=logging.INFO)


migrate_db()
app = Flask(__name__)
CORS(app)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'health': True})
