from models.enum.sexo import Sexo
from models.enum.setor import Setor
from models.funcionario import Funcionario
from projeto_funcionario.models.endereco import Endereco

class Advogado(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, datNascimento: str, oab: str):
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, datNascimento)
        self.oab = oab

    def salario_final(self):
        return super().salario_final()


    def __str__(self) -> str:
        return (f"\n||ADVOGADO||" 
                f"\nCPF: {self.cpf}"
                f"\nSetor: {self.setor.nome}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSalário: {self.salario}"
                f"\nData de Nascimento: {self.datNascimento}"
                f"\nOAB: {self.oab}"
                f"\n\n{self.endereco}"
)