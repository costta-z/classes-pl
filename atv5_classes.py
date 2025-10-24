import os
from dataclasses import dataclass
os.system("cls")


@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str


    def mostrar_dados(self):
        print("== Exibindo dados do usuario ==")
        print(f"Nome: {self.nome}")
        print("Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

    def dados_sms_marketing(self):
            print(f"Telefone de {self.nome}: {self.telefone}")

qtd = int(input("Quantas pessoas você deseja cadastrar? "))

pessoas = []

for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
 

    pessoa = Pessoa(nome, cpf, telefone,)
    pessoas.append(pessoa)

os.system("cls")
print("\n=== Lista de Pessoas Cadastradas ===\n")
for pessoa in pessoas:
    pessoa.mostrar_dados()
    
print()

if qtd >1:
    print("== Telefone dos usuarios==")
else:
    print("== Telefone do usuario ==")
for pessoa in pessoas:
    pessoa.dados_sms_marketing()