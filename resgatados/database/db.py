from flask_sqlalchemy import SQLAlchemy

from ..config.api import application

db = SQLAlchemy()
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resgatados.db'

db.init_app(application)