import json

from flask import jsonify
from flask_restful import Resource

class RegistResource(Resource):
    def get(self):
        return jsonify({"data": "ok"})