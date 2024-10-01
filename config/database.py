from peewee import SqliteDatabase

database = SqliteDatabase('database.db')


def conect():
    from models.livros import LivrosDB
    database.connect
    database.create_tables([LivrosDB])


def end_database():
    database.close()