from models.cargoconfiança import CargaConfianca
from models.endereco import Endereco
from models.cargoconfiança import CargaConfianca
from models.enum.bonificacao import Bonificacao
from models.enum.sexo import Sexo
from models.enum.setor import Setor



class Diretor(CargaConfianca):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, datNascimento: str, bonificacao: Bonificacao):
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, datNascimento, bonificacao)
       

    def salario_final(self):
            calcular_salario = self.salario * self.bonificacao.diretor
            return calcular_salario
    
    def __str__(self) -> str:
         return (
                f"\nNome: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nSetor: {self.setor.nome}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSalário: {self.salario_final()}"
                f"\nData de Nascimento: {self.datNascimento}"
                f"\n{self.endereco}"
)