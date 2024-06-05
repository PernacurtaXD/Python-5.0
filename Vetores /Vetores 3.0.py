import os 

os.system("cls || clear")

QUANT = 6

numeros = []

for i in range (QUANT):
    nota = int(input(f"Digite sua {i+1}ª nota:"))
    numeros.append(nota)

for i, nota in enumerate(numeros):
    print(f"{i+1}ª Nota: {nota}")
