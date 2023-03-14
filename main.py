from resgatados.config.api import application
from resgatados.database.db import db

import resgatados.routes.routes

from resgatados.models.usuario import Usuario

if __name__ == '__main__':
    with application.app_context():
        db.create_all()
    
    application.run(debug=True, port="3000")