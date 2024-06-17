import os 
from dataclasses import dataclass

QUANT = 2

os.system("cls || clear")
@dataclass
class Usuarios:
    nome: str
    idade: int
    peso: float
    altura: float

usuarios = []
for i in range (QUANT):
    os.system("cls || clear")
    nome_usu = input("Digite seu nome:")
    idade_usu = input("Digite seu idade:")
    peso_usu = input ("Digite seu peso:")
    altura_usu = input("Digite sua altura:")

    usuario = Usuarios(
        nome =  nome_usu,
        idade = idade_usu,
        peso = peso_usu, 
        altura = altura_usu
    )

    usuarios.append(usuario)

os.system("cls || clear")
for i, usuario in enumerate(usuarios):
    print(f"{i+1}ª Usuário")
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"Peso: {usuario.peso}")
    print(f"Altura: {usuario.altura}\n")