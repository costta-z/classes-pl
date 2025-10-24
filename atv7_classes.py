import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    cidade: str
    logadouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Cidade: {self.endereco.cidade}")
        print(f"Logadouro: {self.endereco.logadouro}")
        print(f"Logadouro: {self.endereco.numero}")

qtd = int(input("Quantas pessoas você deseja cadastrar? "))

clientes = []

for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")
    logadouro = input("Logadouro: ")
    numero = int(input("Número: "))

    endereco = Endereco(cidade,logadouro,numero)
    cliente = Cliente(nome,email,endereco)
    clientes.append(cliente)

os.system("cls")

for cliete in clientes:
    print("\n=== Lista de clientes cadastradados ===\n")        
    cliente.mostrar_dados()