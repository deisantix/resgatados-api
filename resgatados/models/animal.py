from ..database.db import db
import sqlalchemy as sql
import datetime
import math
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
        sql.Date,
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
        days_since_birth = (datetime.date.today() - self.data_nascimento).days
        months = days_since_birth / 30
        if (months < 1):
            idade = 'menos de 1 mês'
        else:
            idade = f'{math.ceil(months)} meses'
        
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": idade,
            "data_nascimento": self.data_nascimento.strftime('%y-%m-%d'),
            "descricao": self.descricao,
            "raca": self.raca,
            "especie": self.especie,
            "divulgador": self.divulgador
        }
    