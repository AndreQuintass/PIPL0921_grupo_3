from pydantic import BaseModel

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

ListaPessoas = [Pessoa("Joao", 30), Pessoa("Maria", 38)]


class prof(BaseModel):
    nome:str
    exp: str

class UFCD(BaseModel):
    cod: str
    numero: int
    formador: prof


class Pessoa2(BaseModel):
    nome: str
    idade: int
    ufcd: list[UFCD]


class Aluno(BaseModel):
    nome: str
    num: int
    email: str
