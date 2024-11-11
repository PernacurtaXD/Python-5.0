from models.motorista import Motorista 
from models.advogado import Advogado
from models.gerente import Gerente
from models.diretor import Diretor
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.setor import Setor
from models.enum.unidadefederativa import UnidadeFederativa
from models.enum.bonificacao import Bonificacao
import os 


os.system("cls || clear")

motorista = Motorista("Marcos", "364.121.212-56", "554848", 
                    Endereco("Rua A", "4", "1º andar","878745","Salvador", UnidadeFederativa.BAHIA), Setor.ENGRENHARIA, Sexo.MASCULINO,1512.60, "14/12/2005",
                    "20/05/2015")

advogado = Advogado("José", "25654545-21", "45643450", 
                    Endereco("Rua B", "12", "Casa", "5644546", "Copacabana", UnidadeFederativa.RIO_DE_JANEIRO),
                    Setor.JURIDICO, Sexo.MASCULINO, 3028.00, "11/02/1999", "15264154163")

gerente = Gerente("Maria", "5415456", "656655656", Endereco("São Luis", "12", "Apartamento", "4544564", "São Luis", UnidadeFederativa.SAO_PAULO),
                  Setor.OPERACOES, Sexo.FEMININO, 4152.60, "20/10/1998", Bonificacao.GERENTE)

diretor = Diretor("Dante", "54548889", "12686778", Endereco("Rua C", "54", "2º andar", "75775587", "Salvador", UnidadeFederativa.BAHIA),
                  Setor.RECURSOS_HUMANOS, Sexo.MASCULINO, 4152.60, "16/05/1986", Bonificacao.GERENTE)
print(motorista)
print(advogado)
print(gerente)
print(diretor)