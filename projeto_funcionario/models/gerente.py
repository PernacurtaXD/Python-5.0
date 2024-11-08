from models.funcionario import Funcionario
from models.enum.sexo import Sexo
from models.enum.setor import Setor
from models.endereco import Endereco 
from models.enum.bonificacao import Bonificacao
from models.enum.unidadefederativa import UnidadeFederativa
from models.cargoconfiança import CargaConfianca

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, datNascimento: str, bonificacao: Bonificacao) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, datNascimento)
        self.bonificacao = bonificacao

    def salario_final(self):
        pass
    
    def __str__(self) -> str:
        return super().__str__()