import os
from dataclasses import dataclass

os.system("cls")
@dataclass
class Cliente:
    nome: str
    data_nascimento:str
    Endereço: str

    def mostrar_dados_clientes(self):
        return f"Nome: {self.nome}\nData de nascimento: {self.data_nascimento}\nEndereço: {self.Endereço}"


qtd = int(input("Quantos clientes você deseja cadastrar? "))
Clientes = []

print("Solicitando dados do cliente.")
for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    data_nascimento =input("Data de nascimento: ")
    Endereço = input("Endereco: ")

    cliente = Cliente(nome, data_nascimento, Endereço)
    Clientes.append(cliente)

print()
print("Salvando dados.")
arquivo = "dados_Clientes.csv"

with open(arquivo, "a", encoding="utf-8") as arquivo_Clientes:
    for Cliente in Clientes:
        arquivo_Clientes.write(f"{Cliente.mostrar_dados_clientes()}\n\n")
print("Salvo com sucesso!")

print("\nExibindo todos os Clientes:\n")
try:
    with open(arquivo, "r", encoding="utf-8") as arquivo_leitura:
        lista_todos_Clientes = arquivo_leitura.readlines()
        for linha in lista_todos_Clientes:
            print(linha.strip())
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

@dataclass
class Fucionário:
    nome: str
    data_admissao: str
    matrícula: str
    Endereço: str

    def mostrar_dados_funcionarios(self):
        return f"Nome: {self.nome}\nData de admissão: {self.data_admissao}\nMatrícula: {self.matrícula}\nEndereço: {self.Endereço}"

qtd = int(input("Quantos Fucionários você deseja cadastrar? "))
Fucionários = []

print("Solicitando dados do Fucionário.")
for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    data_admissao = input("Data de nascimento: ")
    matrícula =input("matrícula: ")
    Endereço = input("Endereço: ")

    fucionário = Fucionário(nome, data_admissao, matrícula, Endereço)
    Fucionários.append(fucionário)

print()
print("Salvando dados.")
arquivo = "dados_Fucionários.csv"

with open(arquivo, "a", encoding="utf-8") as arquivo_Fucionários:
    for Fucionário in Fucionários:
        arquivo_Fucionários.write(f"{Fucionário.mostrar_dados_funcionarios()}\n\n")
print("Salvo com sucesso!")

print("\nExibindo todos os Fucionários:\n")
try:
    with open(arquivo, "r", encoding="utf-8") as arquivo_leitura:
        lista_todos_Fucionários = arquivo_leitura.readlines()
        for linha in lista_todos_Fucionários:
            print(linha.strip())
except FileNotFoundError:
    print("O arquivo não foi encontrado.")