from models.endereco import Endereco
from models.enum.sexo import Sexo



class Pessoa:
    def __init__(self, id, nome, datNascimento, telefone, email, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.datNascimento = datNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return f"ID: {self.id}\nNome: {self.nome}\nTelefone: {self.telefone}\nE-mail: {self.email}\nSexo: {self.sexo.texto}\n{self.endereco}"