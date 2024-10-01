from fastapi import APIRouter

from models.livros import LivrosDB
from schemas.livrosschema import *
router = APIRouter()

@router.get(path="/livros", response_model=livroReadAll)
def get_livros():
    livros = LivrosDB.select()
    return {'livros': livros}

@router.get(path="/livros/{id}", response_model=LivroRead)
def get_livro(id: int):
    livros = LivrosDB.get_or_none(LivrosDB.id == id)
    return livros

@router.post(path="/livros", response_model=LivroRead)
def create_livro(livro: LivroCreate):
    criar = LivrosDB.create(**livro.model_dump())
    return criar

@router.delete(path="/livros/{id}", response_model=LivroRead)
def delete_livro(id: int):
    livro = LivrosDB.get_or_none(LivrosDB.id == id)
    livro.delete_instance()
    return livro

@router.patch(path="/livros", response_model=LivroRead)
def update_livro(livro: LivroUpdate, id: int):
    livros = LivrosDB.get_or_none(LivrosDB.id == id)
    livros.nome = livro.nome
    livros.preco = livro.preco
    livros.categoria = livro.categoria
    livros.edicao = livro.edicao
    livros.editora = livro.editora
    livros.save()
    return livros