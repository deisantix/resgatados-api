from ..config.api import api

from resgatados.controllers.usuarios import Usuarios
from resgatados.controllers.usuario_por_id import UsuarioPorId
from resgatados.controllers.animais import Animais

api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioPorId, '/usuarios/<cpf>')

api.add_resource(Animais, '/animais')