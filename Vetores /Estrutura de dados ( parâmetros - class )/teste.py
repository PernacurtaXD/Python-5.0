import os
from dataclasses import dataclass

# Função para limpar a tela e exibir o logo do SENAI
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI ===")

# Definição da classe Valor usando dataclass
@dataclass
class Valor:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float
    resultado: str
    imc: float

# Função para calcular o IMC
def calcular(peso, altura):
    imc = peso / (altura * altura)
    return imc

# Função para determinar a situação do IMC
def situacao_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"
    return resultado

# Lista para armazenar os dados dos usuários
dados = []

while True:
    # Solicitando dados do usuário
    logoSenai()
    
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    imc = calcular(peso, altura)
    situacao = situacao_imc(imc)
    
    usuario = Valor(
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        altura=altura,
        peso=peso,
        resultado=situacao,
        imc=imc
    )
    
    dados.append(usuario)

    logoSenai()
    for i, usuario in enumerate(dados):
        print(f"\nDados do {i+1}º usuário:\n")
        print(f"Nome Completo: {usuario.nome} {usuario.sobrenome}")
        print(f"Idade: {usuario.idade}")
        print(f"Altura: {usuario.altura:.2f} metros")
        print(f"Peso: {usuario.peso:.2f} quilogramas")
        print(f"IMC: {usuario.imc:.2f}")
        print(f"Situação: {usuario.resultado}")
