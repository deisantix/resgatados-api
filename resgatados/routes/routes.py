from ..config.api import api

from resgatados.controllers.usuarios import Usuarios
from resgatados.controllers.usuario_por_id import UsuarioPorId
from resgatados.controllers.animais import Animais
from resgatados.controllers.animal_por_id import AnimalPorId

api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioPorId, '/usuarios/<user>')

api.add_resource(Animais, '/animais')
api.add_resource(AnimalPorId, '/animais/<id>')