from peewee import AutoField, CharField,FloatField,IntegerField,Model
from config.database import database

class LivrosDB(Model):
    id = AutoField()
    nome = CharField()
    preco = FloatField()
    categoria = CharField()
    editora = CharField()
    edicao = CharField()

    class Meta:
        database = database