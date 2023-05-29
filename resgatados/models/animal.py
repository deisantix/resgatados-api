from ..database.db import db
import sqlalchemy as sql
from dataclasses import dataclass

@dataclass()
class Animal(db.Model):
    id = sql.Column(
        sql.Integer, 
        primary_key=True
    )
    nome = sql.Column(
        sql.String,
        nullable=False
    )
    data_nascimento = sql.Column(
        sql.String,
        nullable=False
    )
    descricao = sql.Column(
        sql.String
    )
    sexo = sql.Column(
        sql.String,
        nullable=False
    )
    raca = sql.Column(
        sql.String
    )
    especie = sql.Column(
        sql.String,
        nullable=False
    )
    divulgador = sql.Column(
        sql.String,
        nullable=False
    )
    
    def get_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "descricao": self.descricao,
            "raca": self.raca,
            "especie": self.especie,
            "divulgador": self.divulgador
        }
    