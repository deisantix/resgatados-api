import os
from importlib import import_module

from resgatados.config.api import application
from resgatados.database.db import db

import resgatados.routes.routes

if not os.path.exists('./instance/resgatados.db'):
    path_of_models = './resgatados/models'
    models = os.listdir(path_of_models)
    
    for file in models:
        if (file != '__init__.py') and (file != '__pycache__') and (file.endswith('.py')):
            model_path = os.path.join(path_of_models, file)
            bare_model_path = model_path[2:-3]
            model_module = bare_model_path.replace('/', '.')
            
            import_module(model_module)

if __name__ == '__main__':
    with application.app_context():
        db.create_all()
    
    application.run(debug=True, port="8080")