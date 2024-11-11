from models.enum.sexo import Sexo
from models.enum.setor import Setor
from models.enum.unidadefederativa import UnidadeFederativa
from models.endereco import Endereco
from models.funcionario import Funcionario


class Motorista(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, 
                  sexo: Sexo, salario: float, datNascimento: str, carteiraHabilitacao: str) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, datNascimento)
        self.carteiraHabilitacao = carteiraHabilitacao
    
    def salario_final(self):
        return super().salario_final()

    def __str__(self) -> str:
        return (
                f"\n\b||MOTORISTA||\nNome: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nSetor: {self.setor.nome}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSalário: {self.salario}"
                f"\nData de Nascimento: {self.datNascimento}"
                f"\nCarteira de Habilitação: {self.carteiraHabilitacao}"
                f"\n\n{self.endereco}"
    )