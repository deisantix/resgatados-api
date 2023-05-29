import sqlalchemy as sql

from flask_restful import Resource
from ..database.db import db
from sqlalchemy.orm import exc

from ..models.usuario import Usuario as UsuarioModel

class UsuarioPorId(Resource):
    
    def get(self, user):
        try:
            usuario = self.retornar_usuario_por_id(user)
            return usuario.get_json()
        except AttributeError:
            return { "erro": "Usuário não encontrado" }, 404
    
    def delete(self, user):
        try:
            usuario = self.retornar_usuario_por_id(user)
            db.session.delete(usuario)
            db.session.commit()
        except exc.UnmappedInstanceError:
            return { "erro": "Usuário inválido ou já removido" }, 404
        
    def retornar_usuario_por_id(self, user):
        return db.session.execute(
            sql.select(UsuarioModel).where(UsuarioModel.user.__eq__(user))
        ).scalar()