import os 
from dataclasses import dataclass

QUANT = 4
os.system("cls || clear")

@dataclass
class Usuarios:
    nome: str
    idade: int

usuarios = []
for i in range (QUANT):
    os.system("cls || clear")
    nome_usuario = input("Digite seu nome:")
    idade_usuario = input("Digite sua idade:")

    usuario = Usuarios(
        nome = nome_usuario,
        idade = int(idade_usuario)
        )
    usuarios.append(usuario)

os.system("cls || clear")
for i, usuario in enumerate (usuarios):
  
    print(f"\n{i + 1}ª Usuário")
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    