import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    numero: str

    def mostrar_dados(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nE-mail: {self.email}\nNúmero: {self.numero}"

qtd = int(input("Quantos alunos você deseja cadastrar? "))
Alunos = []

print("Solicitando dados do aluno.")
for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    numero = input("Número: ")

    aluno = Aluno(nome, idade, email, numero)
    Alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in Alunos:
        arquivo_alunos.write(f"{aluno.mostrar_dados()}\n\n")
    print("Salvo com sucesso!")
