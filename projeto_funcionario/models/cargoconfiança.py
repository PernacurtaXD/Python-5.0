#from enum.bonificacao import Bonificacao
from models.funcionario import Funcionario
from models.endereco import Endereco
from models.enum.setor import Setor
from models.enum.sexo import Sexo
from models.enum.bonificacao import Bonificacao

class CargaConfianca(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, 
                 sexo: Sexo, salario: float, datNascimento: str, bonificacao: Bonificacao):
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, datNascimento)
        self.bonificacao = bonificacao

    def salario_final(self):
        calcular_salario = self.salario * self.bonificacao.value
        return calcular_salario

    def __str__(self) -> str:
        return super().__str__()
