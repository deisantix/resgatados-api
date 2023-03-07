from flask_restful import Resource
from flask import request

class Usuario(Resource):
    
    def get(self):
        pass
    
    def post(self):
        print(request)