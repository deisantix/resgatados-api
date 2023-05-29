from flask import Flask
from flask_restful import Api
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

api = Api(application)
