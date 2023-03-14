import sqlalchemy as sql

from flask_restful import Resource
from flask import request
from ..database.db import db
from sqlalchemy import exc

from ..models.usuario import Usuario as UsuarioModel 

class Usuarios(Resource):
    
    def get(self):
        usuarios = db.session.execute(
            sql.select(UsuarioModel)
        ).scalars().all()
        
        usuarios_json = [u.get_json() for u in usuarios]
        
        return usuarios_json
    
    def post(self):
        try:
            req = request.get_json()
            
            novo_usuario = UsuarioModel(
                cpf=req['cpf'],
                nome=req['nome'],
                email=req['email'],
                senha=req['senha'],
            )
            if req.get('descricao', -1) != -1:
                novo_usuario.descricao = req['descricao']
            if req.get('endereco', -1) != -1:
                novo_usuario.endereco = req['endereco']
                
            db.session.add(novo_usuario)
            db.session.commit()
            
            return novo_usuario.get_json()
        except KeyError as ke:
            return { "erro": f"Falta parâmetro obrigatório {str(ke)}" }, 400
        except exc.IntegrityError:
            return { "erro": "Usuário já incluso" }, 400
    
    def put(self):
        req = request.get_json()
        
        try:
            usuario = db.session.execute(
                sql.select(UsuarioModel).where(UsuarioModel.cpf.__eq__(req['cpf']))    
            ).scalar()
            usuario.get_json() # apenas para jogar erro caso não exista registro
        except KeyError as ke:
            return { "erro": f"Falta parâmetro obrigatório {str(ke)}" }, 400
        except AttributeError:
            return { "erro": "Usuário não existe" }, 404
        
        mapper = sql.inspect(usuario)
        for column in mapper.attrs:
            key = column.key
            
            valor = req.get(key, -1)
            if valor != -1:
                setattr(usuario, key, valor)
                
        db.session.commit()
        