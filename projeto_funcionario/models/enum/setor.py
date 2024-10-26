from enum import Enum

class Setor(Enum):
    ENGRENHARIA = "Engenharia"
    JURIDICO =  "Jurídico"
    RECURSOS_HUMANOS = "Recursos Humanos"
    MARKETING = "Marketing"
    OPERACOES = "Operações"

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome