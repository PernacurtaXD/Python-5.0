import os 


os.system("cls || clear")

#Criando a lista / vetor 
notas = []


#Solicitando 3 notas para o usuário
for i in range (5):
   nota = int(input("Digite um número:"))
   notas.append(nota)

print(notas)   