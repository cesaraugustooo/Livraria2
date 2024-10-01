from pydantic import BaseModel


class LivroCreate(BaseModel):
    nome: str
    preco: float
    categoria: str
    editora: str
    edicao: str

class LivroRead(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str
    editora: str
    edicao: str


class LivroUpdate(BaseModel):
    nome: str
    preco: float
    categoria: str
    editora: str
    edicao: str

class livroReadAll(BaseModel):
    livros: list[LivroRead]