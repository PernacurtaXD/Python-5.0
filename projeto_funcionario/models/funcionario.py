from abc import ABC, abstractmethod
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.setor import Setor


class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, datNascimento: str) -> None:
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.rg = rg 
        self.endereco = endereco
        self.setor = setor
        self.sexo = sexo
        self.salario = salario
        self.datNascimento = datNascimento

    @abstractmethod
    def salario_final(self):
        pass

    def __str__(self) -> str:
        return (
                f"\nNome: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nSetor: {self.setor.nome}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSalário: {self.salario}"
                f"\nData de Nascimento: {self.datNascimento}"
                #f"\n{self.endereco}"
)