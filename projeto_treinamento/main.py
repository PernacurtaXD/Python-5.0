from models.enum.sexo import Sexo
from models.enum.unidadefederativa import UnidadeFederativa
from models.endereco import Endereco
from models.pessoa import Pessoa

usuario = Pessoa("12", "Maria", "12/11/2005", "71 9985-5898", "maria@gmail.com", Sexo.MASCULINO,
                  Endereco("Rua A", 5, "1º andar", "4545452", "Salvador", UnidadeFederativa.BAHIA))

print(usuario)
