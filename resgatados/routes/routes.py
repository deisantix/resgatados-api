from ..config.api import api
from resgatados.controllers.usuario import Usuario

api.add_resource(Usuario, '/usuario')