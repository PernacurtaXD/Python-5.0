from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino", "M"
    FEMININO = "Feminino", "F"

    def __init__(self, texto: str, sigla: str) -> None:
        self.texto = texto
        self.sigla = sigla