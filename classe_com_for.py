import os
from dataclasses import dataclass
os.system("cls")


@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def somente_nome(self):
            print(f"Nome: {self.nome}")

    def mostrar_dados(self):
        print("== Exibindo dados do usuario ==")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

qtd = int(input("Quantas pessoas você deseja cadastrar? "))

pessoas = []

for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    pessoa = Pessoa(nome, email, telefone, endereco)
    pessoas.append(pessoa)

os.system("cls")
print("\n=== Lista de Pessoas Cadastradas ===\n")
for pessoa in pessoas:
    pessoa.mostrar_dados()
    
print()

if qtd >1:
    print("== Usuarios ==")
else:
    print("== Usuario ==")
for pessoa in pessoas:
    pessoa.somente_nome()