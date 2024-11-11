from enum import Enum

class Bonificacao(Enum):
    GERENTE = 0.35
    DIRETOR = 0.45

    def __init__(self, gerente: float, diretor: float) -> None:
        super().__init__()
        self.gerente = gerente 
        self.diretor = diretor