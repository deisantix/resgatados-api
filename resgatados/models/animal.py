from ..database.db import db
import sqlalchemy as sql

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
    raca = sql.Column(
        sql.String
    )
    especie = sql.Column(
        sql.String,
        nullable=False
    )
    