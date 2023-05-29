from ..database.db import db
import sqlalchemy as sql

class Usuario(db.Model):
    cpf = sql.Column(
        sql.String, 
        primary_key=True
    )
    user = sql.Column(
        sql.String,
        nullable=False
    )
    nome = sql.Column(
        sql.String, 
        nullable=False
    )
    email = sql.Column(
        sql.String, 
        nullable=False
    )
    senha = sql.Column(
        sql.String, 
        nullable=False
    )
    descricao = sql.Column(
        sql.Text
    )
    endereco = sql.Column(
        sql.Text
    )
    tipo = sql.Column(
        sql.String,
        nullable=False
    )
    
    def get_json(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "user": self.user,
            "email": self.email,
            "senha": self.senha,
            "descricao": self.descricao,
            "endereco": self.endereco,
            "tipo": self.tipo,
        }