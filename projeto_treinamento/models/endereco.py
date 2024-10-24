from models.enum.unidadefederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade 
        self.uf = uf
    
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro}\nNúmero: {self.numero}\nCEP: {self.cep}\nCidade:{self.cidade}\nUnidade Federativa: {self.uf.sigla}"