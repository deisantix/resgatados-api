import sqlalchemy as sql

from flask_restful import Resource
from flask import request
from ..database.db import db
from sqlalchemy import exc

from ..models.animal import Animal as AnimalModel

class Animais(Resource):
    
    def get(self):
        animais = db.session.execute(
            sql.select(AnimalModel)
        ).scalars().all()
        
        animais_json = [a.get_json() for a in animais]
        return animais_json
    
    def post(self):
        try:
            req = request.get_json()
            
            novo_animal = AnimalModel()
            for coluna in AnimalModel.__table__.columns:
                obrigatorio = not coluna.nullable
                chave = coluna.key
                valor = req.get(chave, None)
                
                if obrigatorio and valor == None:
                    raise KeyError(chave)
                setattr(novo_animal, chave, valor)
            
            db.session.add(novo_animal)
            db.session.commit()
            
            return novo_animal.get_json()
        except KeyError as ke:
            return { "erro": f"Falta parâmetro obrigatório {str(ke)}" }
        except exc.StatementError as se:
            return { "erro": str(se) }