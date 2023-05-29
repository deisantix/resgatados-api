import sqlalchemy as sql

from flask_restful import Resource
from ..database.db import db
from sqlalchemy.orm import exc

from ..models.usuario import Usuario as UsuarioModel
from ..models.animal import Animal as AnimalModel

class UsuarioPorId(Resource):
    
    def get(self, user):
        try:
            usuario = self.retornar_usuario_por_id(user)
            usuario_json = usuario.get_json()
            
            if (usuario_json['tipo'] == 'D'):
                animais_divulgados = db.session.execute(
                    sql.select(AnimalModel).where(AnimalModel.divulgador.__eq__(usuario_json['cpf']))
                ).scalars().all()
                usuario_json['divulgados'] = [animal.get_json() for animal in animais_divulgados]
            
            return usuario_json
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