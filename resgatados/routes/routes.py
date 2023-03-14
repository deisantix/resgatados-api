from ..config.api import api
from resgatados.controllers.usuarios import Usuarios

api.add_resource(Usuarios, '/usuarios')