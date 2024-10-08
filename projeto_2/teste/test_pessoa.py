import pytest
from projeto_2.models.enum.sexo import Sexo
from ..models.pessoa import Pessoa 

@pytest.fixture
def cria_pessoa():
    return Pessoa("Luis", 18, Sexo.MASCULINO)

def test_nome(cria_pessoa):
    assert cria_pessoa.nome == "Luis"

def test_idade(cria_pessoa):
    assert cria_pessoa.idade == 18

def test_pessoa_alterar_nome_valido(cria_pessoa):
    cria_pessoa.nome = "Pedro"
    assert cria_pessoa.nome == "Pedro" 