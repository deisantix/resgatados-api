import sqlalchemy as sql

from flask_restful import Resource
from ..database.db import db

from ..models.animal import Animal as AnimalModel
from ..models.usuario import Usuario as UsuarioModel

class AnimalPorId(Resource):
    def get(self, id):
        try:
            animal = self.retornar_animal_por_id(id)
            
            divulgador = db.session.execute(
                sql.select(UsuarioModel).where(UsuarioModel.cpf.__eq__(animal.divulgador))
            ).scalar()
            
            animal_json = animal.get_json()
            animal_json['divulgador'] = divulgador.get_json()
            return animal_json
        except AttributeError:
            return { "erro": "Animal não encontrado" }, 404
        
    def retornar_animal_por_id(self, id):
        return db.session.execute(
            sql.select(AnimalModel).where(AnimalModel.id.__eq__(id))
        ).scalar()