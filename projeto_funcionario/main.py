from models.motorista import Motorista 
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.setor import Setor
from models.enum.unidadefederativa import UnidadeFederativa
import os 


os.system("cls || clear")

motorista = Motorista("Marcos", "364.121.212-56", "554848", 
                    Endereco("Rua A", "4", "1º andar","878745","Salvador", UnidadeFederativa.BAHIA), Setor.ENGRENHARIA, Sexo.MASCULINO,1512.60, "14/12/2005",
                    "20/05/2015")

print(motorista)